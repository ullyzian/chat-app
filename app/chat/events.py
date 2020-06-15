from .. import socketio
from .. import database


def messageReceived(methods=["GET", "POST"]):
    print("Message received")


@socketio.on("send")
def handle_event(json, methods=["GET", "POST"]):
    if ("message" in json.keys()):
        database.run_query("""
            INSERT INTO chat (username, message, room) VALUES (%s, %s, %s)
            """, (json["username"], json["message"], json["room"]))

    print("Received: " + str(json))

    if ("room" in json.keys()):
        records = database.run_query("""
            SELECT * FROM chat WHERE room = %s ORDER BY date DESC LIMIT 100
            """, json["room"])

        history = {"history": []}

        for username, message, room, date in records[::-1]:
            history["history"].append(
                {"message": message, "username": username, "date": date.strftime("%H:%M:%S")})

        if ("data" in json.keys()):
            history["data"] = json['data']

        socketio.emit('response', history, callback=messageReceived)
    else:
        socketio.emit('response', json, callback=messageReceived)
