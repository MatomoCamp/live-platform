import json
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from random import randint, random
from typing import List, Dict, Tuple, Optional

from dateutil.parser import parse

from urls import chat_rooms, workshop_urls, recording_ids

STREAM_FALLBACKS = False

alternative_stream_hosts = {
    "Alternative Stream 1": "https://stream-fallback1.matomocamp.org/",
    "Alternative Stream 2": "https://matomocamp-stream.lw1.at/",
}
alternative_stream_hosts_names = list(alternative_stream_hosts.keys())
alternative_stream_hosts_urls = list(alternative_stream_hosts.values())

track_colors = {
    "Privacy": "#F38334",
    "System administration": "#95C748",
    "Contributing": "#8E0F0F",
    "Digital Analytics": "#3152A0",
    "Using Matomo": "#35BFC0",
    "Business": "#673AB7",
    "Use Cases": "#1B5E20",
    "MatomoCamp": "#404040"
}


@dataclass
class Talk:
    id: str
    title: str
    session_type: str
    track: str
    abstract: str
    description: str
    duration: int
    language: str
    speaker_names: List[str]
    room: str
    start: datetime
    end: datetime

    @property
    def full_language(self) -> str:
        if self.language == "de":
            return "German"
        elif self.language == "fr":
            return "French"
        else:
            return "English"

    @property
    def schedule_url(self) -> str:
        return f"https://schedule.matomocamp.org/matomocamp-2021/talk/{self.id}/"

    @property
    def feedback_url(self) -> str:
        return self.schedule_url + "feedback/"

    @property
    def chat_room(self) -> str:
        return chat_rooms[self.id]

    @property
    def chat_room_id(self) -> str:
        return f"#{self.chat_room}:matomocamp.org"

    @property
    def chat_room_url(self) -> str:
        return "https://chat.matomocamp.org/#/room/" + self.chat_room_id

    def livestream_host(self) -> Tuple[str, str]:
        livestream_host = "https://stream-mtmc-2021.cloud-ed.fr/"
        livestream_name = "Main Livestream"
        if STREAM_FALLBACKS:
            use_original_stream = random() > 0.33
            if use_original_stream:
                return livestream_host, livestream_name
            num = randint(0, len(alternative_stream_hosts) - 1)
            return alternative_stream_hosts_urls[num], alternative_stream_hosts_names[num]
        return livestream_host, livestream_name

    @property
    def livestream_url(self) -> Tuple[str, str]:
        livestream_host, livestream_name = self.livestream_host()
        if self.room == "Livestream Room 1":
            return livestream_host + "hls/stream.m3u8", livestream_name
        if self.room == "Livestream Room 2":
            return livestream_host + "hls/stream2.m3u8", livestream_name
        return "", "No Stream"

    @property
    def recording_id(self) -> Optional[str]:
        if self.id in recording_ids:
            return recording_ids[self.id]
        return None

    @property
    def recording_url(self) -> Optional[str]:
        if self.recording_id:
            return "https://video.matomocamp.org/w/" + self.recording_id
        return None

    @property
    def recording_embed_url(self) -> Optional[str]:
        if self.recording_id:
            return "https://video.matomocamp.org/videos/embed/" + self.recording_id
        return None

    @property
    def track_color(self) -> str:
        return track_colors[self.track]

    @property
    def is_workshop(self) -> bool:
        return self.room == "Workshop Room"

    @property
    def workshop_url(self) -> str:
        if not self.is_workshop:
            return "#"
        return workshop_urls[self.id]

    @property
    def has_already_started(self):
        return datetime.now(timezone.utc) > talk.start


talks = []
with open("matomocamp-2021_sessions.json") as f:
    data: List[Dict] = json.load(f)
for t in data:
    talk = Talk(
        id=t["ID"],
        title=t["Title"],
        session_type=t["Session type"]["en"],
        track=t["Track"]["en"],
        abstract=t["Abstract"],
        description=t["Description"],
        duration=t["Duration"],
        language=t["Language"],
        speaker_names=t["Speaker names"],
        room=t["Room"]["en"],
        start=parse(t["Start"]),
        end=parse(t["Start"])
    )
    talks.append(talk)
del data

talks.sort(key=lambda t: (t.start, t.title))

talks_by_id = {}

for t in talks:
    talks_by_id[t.id] = t


def talks_at_the_same_time(talk: Talk) -> List[Talk]:
    others = []
    for t in talks:
        if t == talk:
            continue
        if t.start == talk.start:
            others.append(t)
    return others


def coming_up_next(talk: Talk) -> List[Talk]:
    others = []
    if talk.start.time().hour == 11 - 1:
        delta = timedelta(hours=2)
    else:
        delta = timedelta(hours=1)
    for t in talks:
        if t.start == talk.start + delta:
            others.append(t)
    return others
