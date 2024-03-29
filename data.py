import json
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from random import randint, random
from typing import List, Dict, Tuple, Optional
from urllib.parse import quote_plus

import pytz
from dateutil.parser import parse

from urls import chat_rooms, workshop_urls, recording_ids, archive_names, recording_ids_drafts
from utils import translated_dict_to_string, time_plusminus15min

STREAM_FALLBACKS = False
primary_stream_host = "https://stream-mtmc.cloud-ed.fr/"
alternative_stream_hosts = {
    # "Alternative Stream 1": "https://livestream-mirror1.matomocamp.org/",
    # "Alternative Stream 2": "https://stream-mtmc-2021.cloud-ed.fr/",
}
alternative_stream_hosts_names = list(alternative_stream_hosts.keys())
alternative_stream_hosts_urls = list(alternative_stream_hosts.values())

conference_timezone = pytz.timezone("Europe/Vienna")

track_colors = {
    2021: {
        "Privacy": "#F38334",
        "System administration": "#95C748",
        "Contributing": "#8E0F0F",
        "Digital Analytics": "#3152A0",
        "Using Matomo": "#35BFC0",
        "Business": "#673AB7",
        "Use Cases": "#1B5E20",
        "MatomoCamp": "#404040"
    },
    2022: {
        "Privacy": "#F38334",
        "System administration": "#95C748",
        "Integration": "#8E0F0F",
        "Digital Analytics": "#3152A0",
        "Using Matomo": "#35BFC0",
        "Business": "#673AB7",
        "Use Cases": "#1B5E20",
        "MatomoCamp": "#404040",
        "Plugin Development": "#F00DE7",
        "Contributing": "#BF360C",
        "Other Free Analytics": "#673AB7",
    },
}

track_colors[2023] = track_colors[2022]

current_year = 2023
past_years = [2021, 2022]


@dataclass
class Talk:
    id: str
    year: int
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
        elif self.language == "it":
            return "Italian"
        elif self.language == "fi":
            return "Finnish"
        else:
            return "English"

    @property
    def schedule_url(self) -> str:
        return f"https://schedule.matomocamp.org/matomocamp-{self.year}/talk/{self.id}/"

    @property
    def feedback_url(self) -> str:
        return self.schedule_url + "feedback/"

    @property
    def chat_room(self) -> str:
        try:
            return chat_rooms[self.id]
        except KeyError:
            return "CHATROOM-MISSING"

    @property
    def chat_room_id(self) -> str:
        return f"#{self.chat_room}:matomocamp.org"

    @property
    def archive_name(self) -> Optional[str]:
        try:
            return archive_names[self.id]
        except KeyError:
            return None

    @property
    def archive_name_encoded(self) -> Optional[str]:
        try:
            return quote_plus(archive_names[self.id]).replace("+", "%20")
        except KeyError:
            return None

    @property
    def chat_room_url(self) -> str:
        try:
            if self.archive_name_encoded is None:  # quick ugly workaround
                raise KeyError()
            return f"https://archive.matomocamp.org/{self.year}/{self.archive_name_encoded}/chat/"
        except KeyError:
            return "https://chat.matomocamp.org/#/room/" + self.chat_room_id

    @property
    def archive_url(self) -> Optional[str]:
        try:
            return f"https://archive.matomocamp.org/{self.year}/{self.archive_name_encoded}/"
        except KeyError:
            return None

    @property
    def subtitle_edit_url(self) -> Optional[str]:
        try:
            return f"https://github.com/MatomoCamp/recording-subtitles/tree/main/{self.year}/{self.archive_name_encoded}/"
        except KeyError:
            return None

    @property
    def random_alternative_stream_id(self) -> int:
        return randint(1, len(alternative_stream_hosts))

    def livestream_host(self, alternative_stream_id=None) -> Tuple[str, str]:
        livestream_host = primary_stream_host
        livestream_name = "Main Livestream"
        if alternative_stream_id is not None:
            if alternative_stream_id == 0:
                return livestream_host, livestream_name
            return alternative_stream_hosts_urls[alternative_stream_id - 1], \
                alternative_stream_hosts_names[alternative_stream_id - 1]

        if STREAM_FALLBACKS:
            use_original_stream = random() > 0.33
            if use_original_stream:
                return livestream_host, livestream_name
            num = randint(0, len(alternative_stream_hosts) - 1)
            return alternative_stream_hosts_urls[num], alternative_stream_hosts_names[num]
        return livestream_host, livestream_name

    def livestream_url(self, alternative_stream_id=None) -> Tuple[str, str]:
        livestream_host, livestream_name = self.livestream_host(alternative_stream_id)
        if self.room == "Livestream Room 1":
            return livestream_host + "hls/stream1.m3u8", livestream_name
        if self.room == "Livestream Room 2":
            return livestream_host + "hls/stream2.m3u8", livestream_name
        if self.room == "Livestream Room 3":
            return livestream_host + "hls/stream3.m3u8", livestream_name
        return "", "No Stream"

    @property
    def live_url(self) -> str:
        return "https://live.matomocamp.org/" + self.id

    @property
    def recording_id(self) -> Optional[str]:
        if self.id in recording_ids:
            return recording_ids[self.id]
        return None

    @property
    def recording_id_drafts(self) -> Optional[str]:
        if self.id in recording_ids_drafts:
            return recording_ids_drafts[self.id]
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
        return track_colors[self.year][self.track]

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

    @property
    def formatted_datetimerange(self) -> str:
        weekday_data = {
            4: {
                "en": "Thu",
                "de": "Do",
                "fr": "Jeu",
                "it": "Gio",
                "fi": "To"
            },
            5: {
                "en": "Fri",
                "de": "Fr",
                "fr": "Ven",
                "it": "Ven",
                "fi": "Pe"
            }
        }
        print(self.start, self.end)
        start_in_right_timezone = self.start.astimezone(conference_timezone)
        weekday = weekday_data[self.start.isoweekday()][self.language]
        return weekday \
            + " " \
            + start_in_right_timezone.strftime("%H:%M") \
            + "–" \
            + self.end.strftime("%H:%M")

    @property
    def topic(self):
        return f"{self.title} -- Watch live here: {self.live_url}"


talks = []
for year in [2021, 2022, 2023]:
    with open(f"matomocamp-{year}_sessions.json") as f:
        data: List[Dict] = json.load(f)
    for t in data:
        if t["Proposal state"] in {"withdrawn"}:
            continue
        talk = Talk(
            id=t["ID"],
            year=year,
            title=t["Title"] if "Title" in t else t["Proposal title"],
            session_type=translated_dict_to_string(t["Session type"]),
            track=t["Track"]["en"],
            abstract=t["Abstract"],
            description=t["Description"],
            duration=t["Duration"],
            language=t["Language"],
            speaker_names=t["Speaker names"],
            room=t["Room"]["en"],
            start=parse(t["Start"]),
            end=parse(t["End"])
        )
        talks.append(talk)
    del data

talks.sort(key=lambda t: (t.start, t.title))

talks_of_this_year = [t for t in talks if t.year == current_year]

talks_by_id = {}

for t in talks:
    talks_by_id[t.id] = t


def talks_at_the_same_time(talk: Talk) -> List[Talk]:
    others = []
    for t in talks:
        if t == talk:
            continue
        if t.start in time_plusminus15min(talk.start):
            others.append(t)
    return others


def coming_up_next(talk: Talk) -> List[Talk]:
    others = []
    if talk.start.time().hour == 11 - 1:
        delta = timedelta(hours=2)
    else:
        delta = timedelta(hours=1)
    for t in talks:
        if t.start in time_plusminus15min(talk.start + delta):
            others.append(t)
    return others


if __name__ == '__main__':
    for talk in talks:
        if talk.id not in chat_rooms:
            print(f"missing chatroom: {talk.id} ({talk.title})")

    with open("/home/lukas/tmp/stats.json") as f:
        data = json.load(f)
    data_dict = {}
    for e in data:
        data_dict[e["label"].lstrip("/")] = e
    for talk in talks:
        if talk.year != 2022 or talk.id == "389UYH":
            continue
        num_pageviews = data_dict[talk.id]["nb_visits"]
        print(f"{talk.title};{', '.join(talk.speaker_names)};{num_pageviews}")
