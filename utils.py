import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Dict, Set

import sass

basedir = Path(__file__).resolve().parent

inputdir = basedir / "style/"
inputfile = inputdir / "main.scss"
outputfile = basedir / "static/main.css"
sourcemap = outputfile.with_suffix(".css.map")


def get_css():
    sourcemap_name = str(sourcemap)
    css, sourcemap_text = sass.compile(
        filename=str(inputfile),
        output_style="compressed",
        include_paths=[str(inputdir), str(basedir)],
        source_map_filename=sourcemap_name,
        source_map_contents=True
    )
    return css, sourcemap_text


def save_css():
    css, sourcemap_text = get_css()
    with outputfile.open("w") as f:
        f.write(css)
    with sourcemap.open("w") as f:
        f.write(sourcemap_text)


def translated_dict_to_string(data: Dict[str, str]) -> str:
    """
    get first value of dictionary
    {"de":"test"} -> "test"
    {"en":"test"} -> "test"
    """
    return next(iter(data.values()))


def time_plusminus15min(time: datetime) -> Set[datetime]:
    times = {time}
    min15 = timedelta(minutes=15)
    times.add(time + min15)
    times.add(time - min15)
    return times

def print_diff_call(str1: str, str2: str, title: str) -> None:
    with NamedTemporaryFile(delete=True, mode="w", suffix=title) as tmp1:
        with NamedTemporaryFile(delete=True, mode="w", suffix=title) as tmp2:
            tmp1.write(str1)
            tmp1.flush()
            tmp2.write(str2)
            tmp2.flush()
            subprocess.run(["git", "--no-pager", "diff", "--color-words=.", tmp1.name, tmp2.name])

if __name__ == '__main__':
    save_css()
