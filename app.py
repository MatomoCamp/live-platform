from datetime import datetime, timezone

from babel.dates import format_timedelta
from flask import Flask, render_template, abort, make_response

from data import talks_by_id, talks_at_the_same_time, coming_up_next, talks
from utils import get_css

app = Flask(__name__)


@app.route("/chat-home")
def chat_home():
    return render_template(
        "chat-home.html",
        talks=talks
    )


@app.route("/<string:session_id>")
def talk_page(session_id):
    try:
        talk = talks_by_id[session_id]
    except KeyError:
        abort(404)
        return
    return render_template(
        "index.html",
        talk=talk,
        title="Test",
        others=talks_at_the_same_time(talk),
        next=coming_up_next(talk),
        delta=format_timedelta(datetime.now(timezone.utc) - talk.start, threshold=1.5, locale=talk.language),
        debug=app.debug
    )


if app.debug:
    @app.route("/css")
    def css():
        css, sourcemap = get_css()
        response = make_response(css)
        response.headers["Content-Type"] = "text/css"
        return response
