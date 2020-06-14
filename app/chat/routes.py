from flask import render_template, make_response
from . import bp
import requests
import datetime


@bp.route("/")
def session():
    response = make_response(render_template("session.html"))
    username = requests.get("http://names.drycodes.com/1").json()[0]
    expire_date = datetime.datetime.now() + datetime.timedelta(minutes=1)
    response.set_cookie('username', username, expires=expire_date)
    return response
