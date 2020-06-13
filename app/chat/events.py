from .. import socketio


def messageReceived(methods=["GET", "POST"]):
    print("Message received")


@socketio.on("send")
def handle_event(json, methods=["GET", "POST"]):
    print("received: " + str(json))
    socketio.emit('response', json, callback=messageReceived)
