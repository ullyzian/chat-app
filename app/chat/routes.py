from flask import render_template, make_response
from . import bp
import requests


@bp.route("/")
def index():
    response = make_response(render_template("index.html"))
    username = requests.get("http://names.drycodes.com/1").json()[0]
    response.set_cookie('username', username)
    return response


@bp.route("/chats/<int:room>")
def chat(room):
    response = make_response(render_template(
        "chat.html", data={"chat": room}))
    username = requests.get("http://names.drycodes.com/1").json()[0]
    response.set_cookie('username', username)
    return response
