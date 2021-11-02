from datetime import datetime, timezone

from babel.dates import format_timedelta
from flask import Flask, render_template, abort, make_response, redirect

from data import talks_by_id, talks_at_the_same_time, coming_up_next, talks
from utils import get_css

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "home.html",
        talks=talks,
        debug=app.debug
    )


@app.route("/chat-home")
def chat_home():
    response = make_response(render_template(
        "chat-home.html",
        talks=talks
    ))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/<string:session_id>")
def talk_page(session_id):
    try:
        talk = talks_by_id[session_id]
    except KeyError:
        abort(404)
        return
    tdelta = talk.start - datetime.now(timezone.utc)
    delta_pretty = None
    if tdelta.total_seconds() > 0:
        delta_pretty = format_timedelta(tdelta, threshold=1.5, locale=talk.language)
    return render_template(
        "index.html",
        talk=talk,
        title="Test",
        others=talks_at_the_same_time(talk),
        next=coming_up_next(talk),
        delta=delta_pretty,
        debug=app.debug
    )


@app.route("/<string:session_id>/chat_room")
def chat_redirect(session_id):
    try:
        talk = talks_by_id[session_id]
    except KeyError:
        abort(404)
        return
    return redirect(talk.chat_room_url)


if app.debug:
    @app.route("/css")
    def css():
        css, sourcemap = get_css()
        response = make_response(css)
        response.headers["Content-Type"] = "text/css"
        return response
