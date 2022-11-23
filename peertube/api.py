import inspect
import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Tuple, Literal, Dict, List, Union

from requests import Session

technology_category = 15
license_id_sa = 2


class PeertubeAPI:

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.api_url = self.base_url + "/api/v1"
        self.s = Session()
        self.s.max_redirects = 0
        try:
            with open("token.json") as f:
                data = json.load(f)
            self.access_token = data["access_token"]

        except FileNotFoundError:
            self.access_token = None

    def get_client(self) -> Tuple[str, str]:
        r = self.s.get(self.api_url + "/oauth-clients/local")
        r.raise_for_status()
        data = r.json()
        return data["client_id"], data["client_secret"]

    def login(self, username: str, password: str):
        client_id, client_secret = self.get_client()
        now = datetime.now().timestamp()
        r = self.s.post(self.api_url + "/users/token", data={
            "client_id": client_id,
            "client_secret": client_secret,
            "username": username,
            "password": password,
            "grant_type": "password"
        })
        r.raise_for_status()
        data = r.json()
        data["expires_in_ts"] = now + data["expires_in"]
        data["refresh_token_expires_in_ts"] = now + data["refresh_token_expires_in"]
        with open("token.json", "w") as f:
            json.dump(data, f)

    @property
    def headers(self):
        return {
            "Authorization": f"Bearer {self.access_token}"
        }

    def get_video(self, id: str) -> "Video":
        r = self.s.get(self.api_url + f"/videos/{id}")
        r.raise_for_status()
        data = r.json()
        r2 = self.s.get(self.api_url + f"/videos/{id}/description")
        r2.raise_for_status()
        data["description"] = r2.json()["description"]

        return Video.from_dict(data, self)

    def get_captions(self, id: str) -> Dict[str, Dict[str, Union[str, int]]]:
        r = self.s.get(self.api_url + f"/videos/{id}/captions")
        r.raise_for_status()
        subtitles = {}
        for entry in r.json()["data"]:
            entry["timestamp"] = datetime.fromisoformat(entry["updatedAt"].replace("Z", "+00:00")).timestamp()
            subtitles[entry["language"]["id"]] = entry

        return subtitles

    def upload_caption(self, id: str, lang: str, caption_file: Path):
        r = self.s.put(
            self.api_url + f"/videos/{id}/captions/{lang}",
            headers=self.headers,
            files={
                "captionfile": caption_file.open("rb")
            }
        )
        r.raise_for_status()

    def update_video(self, id: str, data: Dict) -> None:
        del data["api"]
        r = self.s.put(self.api_url + f"/videos/{id}", json=data, headers=self.headers)
        # print(r.json())
        r.raise_for_status()

    def update_thumbnail(self, id: str, file: Path) -> None:
        print(file)
        r = self.s.put(self.api_url + f"/videos/{id}", files={
            "thumbnailfile": ("thumb.png", file.open("rb"), "image/png")
        }, headers=self.headers)
        r.raise_for_status()


@dataclass
class Video:
    shortUUID: str
    api: PeertubeAPI
    category: int
    description: str
    language: str
    licence: int
    name: str
    originallyPublishedAt: str
    privacy: Literal[1, 2, 3, 4]
    support: str
    tags: List[str] = field()

    @classmethod
    def from_dict(cls, env, api: PeertubeAPI):
        """
        https://stackoverflow.com/a/55096964/4398037
        """
        bla = {}
        for k, v in env.items():
            if k not in inspect.signature(cls).parameters:
                continue
            if isinstance(v, dict):
                v = v["id"]
            bla[k] = v
        return cls(api=api, **bla)

    def save(self) -> None:
        self.api.update_video(self.shortUUID, self.__dict__)
