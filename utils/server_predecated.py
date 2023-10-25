import socketio
# from utils.RepeatedTimer import RepeatedTimer

# standard Python
sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")


direction = 0
import random
def foo():
    global direction
    direction = 0 if direction == 1 else 1
    print("emit", direction)
    sio.emit('signal', {'direction': direction})
# start timer
# timer = RepeatedTimer(0.01, foo)
# timer.stop()


sio.connect('http://localhost:3000/')