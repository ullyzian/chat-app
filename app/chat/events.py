from .. import socketio
from ..connection import create_connection


def messageReceived(methods=["GET", "POST"]):
    print("Message received")


@socketio.on("send")
def handle_event(json, methods=["GET", "POST"]):
    cur, conn = create_connection()
    if ("message" in json.keys()):
        cur.execute(
            """
            INSERT INTO history (username, message) VALUES (%s, %s)
            """, (json["username"], json["message"])
        )
        conn.commit()
    print("Received: " + str(json))
    cur.execute(
        """
        SELECT * FROM history ORDER BY date DESC LIMIT 100
        """
    )
    history = {"history": []}
    query = cur.fetchall()
    for username, message, date in query[::-1]:
        history["history"].append(
            {"message": message, "username": username, "date": date.strftime("%H:%M:%S")})
    
    if ("data" in json.keys()):
        history["data"] = json['data']
    conn.close()
    socketio.emit('response', history, callback=messageReceived)
