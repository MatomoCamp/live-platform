from flask import Flask, render_template, abort

from data import talks_by_id, talks_at_the_same_time, coming_up_next

app = Flask(__name__)

app.config


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
        next=coming_up_next(talk)
    )
