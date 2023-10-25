import socketio
import eventlet

import middleware

middleware.init()

sio = socketio.Server(async_mode='eventlet')
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})


@sio.event
def connect(sid, environ):
    print('server connected to client with session ID =  ',sid)


@sio.event
def message(sid,data):
    print('message=>SERVER ', data)
    response_command = middleware.run()
    sio.send(response_command)

    # sio.emit(data + ' to client')

@sio.event
def response(sid,recdata):
    print(recdata)


@sio.event
def disconnect(sid):
    print('disconnect=>SERVER ', 'SID: ',sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 3000)), app)
