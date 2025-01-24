from flask import Flask, render_template, make_response
from flask_socketio import SocketIO
import inputs
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Global variables for controller state
controller_active = False
controller_thread = None

def get_gamepad_events():
    global controller_active
    while controller_active:
        try:
            # Get a list of all gamepads
            gamepads = inputs.devices.gamepads
            
            if not gamepads:
                print("No gamepad detected. Please connect your Xbox controller.")
                time.sleep(1)
                continue
                
            events = inputs.get_gamepad()
            for event in events:
                print(f"Controller Event - Code: {event.code}, State: {event.state}, Type: {event.ev_type}")  # Debug print
                socketio.emit('controller_event', {
                    'code': event.code,
                    'state': event.state,
                    'type': event.ev_type
                })
        except inputs.UnpluggedError:
            print("Controller unplugged. Waiting for controller...")
            time.sleep(1)
        except Exception as e:
            print(f"Controller error: {e}")
            time.sleep(0.1)

@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    # Disable caching
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@socketio.on('start_controller')
def start_controller():
    global controller_active, controller_thread
    if not controller_active:
        print("Starting controller monitoring...")  # Debug print
        controller_active = True
        controller_thread = threading.Thread(target=get_gamepad_events)
        controller_thread.start()
        return {'status': 'started'}

@socketio.on('stop_controller')
def stop_controller():
    global controller_active, controller_thread
    if controller_active:
        print("Stopping controller monitoring...")  # Debug print
        controller_active = False
        if controller_thread:
            controller_thread.join()
        return {'status': 'stopped'}

@socketio.on('connect')
def handle_connect():
    print("Client connected")  # Debug print

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")  # Debug print

if __name__ == '__main__':
    print("Starting server... Please connect to http://localhost:5000")
    print("Available gamepads:", inputs.devices.gamepads)  # Debug print
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
