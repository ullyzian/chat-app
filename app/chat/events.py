from .. import socketio
from .. import database


@socketio.on("send")
def handle_event(json, methods=["GET", "POST"]):
    if ("message" in json.keys()):
        database.run_query("""
            INSERT INTO chat (username, message, room) VALUES (%s, %s, %s)
            """, (json["username"], json["message"], json["room"]))

    print("Received: " + str(json))

    if ("room" in json.keys()):
        records = database.run_query(
            """
            SELECT username, message, room, to_char(date, 'HH12:MI:SS')
            FROM chat WHERE room = %s ORDER BY date DESC LIMIT 100;
            """, json["room"])

        history = {"history": records}

        if ("data" in json.keys()):
            history["data"] = json['data']

        socketio.emit('response', history)
    else:
        socketio.emit('response', json)
