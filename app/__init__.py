from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(debug=False):
    app = Flask(__name__)
    from . import chat
    app.register_blueprint(chat.bp)
    socketio.init_app(app)
    return app
