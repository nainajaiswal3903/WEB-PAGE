from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import subprocess
import threading

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('page1.html')

@app.route('/start_friday')
def start_friday():
    socketio.start_background_task(target=run_script)
    return '', 204

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

def run_script():
    process = subprocess.Popen(['python', 'C:/Users/shyam/Desktop/FRIDAY/friday.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in iter(process.stdout.readline, b''):
        socketio.emit('script_output', {'data': line.decode('utf-8')})
    process.stdout.close()
    process.wait()

if __name__ == '__main__':
    socketio.run(app, debug=True)
