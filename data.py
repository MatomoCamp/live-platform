import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict

from dateutil.parser import parse

track_colors = {
    "Privacy": "#F38334",
    "System Administration": "#95C748",
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
    def chat_room_url(self) -> str:
        return "https://example.com"

    @property
    def livestream_url(self) -> str:
        if self.room == "Livestream Room 1":
            return "https://stream-mtmc-2021.cloud-ed.fr/hls/stream.m3u8"
        return ""

    @property
    def track_color(self) -> str:
        return track_colors[self.track]


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
    print(talk.start.time().hour)
    if talk.start.time().hour == 11 - 1:
        delta = timedelta(hours=2)
    else:
        delta = timedelta(hours=1)
    for t in talks:
        if t.start == talk.start + delta:
            others.append(t)
    return others
