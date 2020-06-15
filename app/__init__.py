import os
from flask import Flask
from flask_socketio import SocketIO
from .database import Database

socketio = SocketIO()

database = Database(os.environ.get("USER"), os.environ.get("PASSWORD"),
                    os.environ.get("HOST"), os.environ.get("PORT"), os.environ.get("DATABASE"))


def create_tables():
    commands = (
        """
            CREATE TABLE chat (
                username VARCHAR(100) NOT NULL,
                message VARCHAR(255) NOT NULL,
                room INTEGER NOT NULL,
                date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            """,
    )
    database.create_tables(commands)


def create_app(debug=False):
    app = Flask(__name__)
    from . import chat
    app.register_blueprint(chat.bp)
    socketio.init_app(app)
    return app
