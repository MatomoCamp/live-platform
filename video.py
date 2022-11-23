import sys
import time
from getpass import getpass
from pathlib import Path

from data import talks, Talk
from peertube import PeertubeAPI
from peertube.api import license_id_sa, technology_category
from utils import print_diff_call

a = PeertubeAPI(base_url="https://video.matomocamp.org")

projects_dir = Path("/media/ssd/MatomoCamp Recordings/Projects/")


def description_of_talk(talk: Talk):
    text = talk.description
    text += "\n\n"
    text += f"by {', '.join(talk.speaker_names)}\n"
    text += "\n"
    text += f"View in Schedule: {talk.schedule_url}\n"
    text += f"Audio-only: {talk.archive_url}output.opus\n"
    text += f"High-Quality Video: {talk.archive_url}output.mp4\n"
    text += f"Help improve the subtitles: {talk.subtitle_edit_url}\n"

    return text


if not a.access_token:
    username = input("username: ")
    password = getpass()

    a.login(username, password)

for talk in talks:
    if not talk.recording_id_drafts:
        continue

    if talk.year != 2022:
        continue
        time.sleep(1)

    if sys.argv[1] and talk.id!=sys.argv[1]:
        continue
    print(talk)

    video = a.get_video(talk.recording_id_drafts)

    project_dir = projects_dir / str(talk.year) / talk.archive_name
    print(project_dir)
    assert project_dir.exists()

    subtitles = {}
    subtitle_en = project_dir / "output.srt"
    if subtitle_en.exists():
        subtitles["en"] = subtitle_en
    for lang in ["de", "en", "it", "fr"]:
        subtitle_lang = project_dir / f"output.{lang}.srt"
        if subtitle_lang.exists():
            subtitles[lang] = subtitle_lang
    remote_captions = a.get_captions(talk.recording_id_drafts)
    for lang, subtitle in subtitles.items():
        if lang not in remote_captions or subtitle.stat().st_mtime > remote_captions[lang]["timestamp"]:
            print("upload")
            a.upload_caption(talk.recording_id_drafts, lang, subtitle)

    if talk.year != 2022:
        continue

    starttime = talk.start.isoformat().replace('+00:00', '.000Z')
    video.tags = ["MatomoCamp", talk.track]
    video.language = talk.language
    video.licence = license_id_sa
    video.category = technology_category
    video.originallyPublishedAt = starttime
    video.name = talk.title
    if video.privacy == 2:
        video.name = "Draft - " + video.name
    if not video.description:
        a.update_thumbnail(talk.recording_id_drafts, project_dir / "title-page.png")
        video.description = description_of_talk(talk)

    print_diff_call(video.description, description_of_talk(talk), video.shortUUID)
    assert talk.year == 2022
    video.save()
    time.sleep(.8)

    # assert talk.title == video.name
    # if video.shortUUID == "gqEzAyzDJz4KLR9gwygVK2":
    #     video.originallyPublishedAt = starttime
    #     video.name = talk.title
    #     video.save()
    print("\n\n")
# video.licence = license_id_sa
# video.category = technology_category
# if "MatomoCamp" not in video.tags:
#     video.tags.append("MatomoCamp")
# if not video.language:
#     video.language = "en"
# print(video)
# video.description = "test"
# video.save()
