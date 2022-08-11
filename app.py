import random
import threading
import time

from flask import Flask, render_template, send_file


class ExportingThread(threading.Thread):
    def __init__(self):
        self.progress = 0
        self.text = ""
        super().__init__()

    def run(self):
        # Your exporting stuff goes here ...
        for _ in range(1, 120):
            time.sleep(0.1)
            self.progress += 1
        
exporting_threads = {}
app = Flask(__name__)
app.debug = True


@app.route('/file')
def file():
    return send_file('./data/test.xlsx')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    global exporting_threads

    thread_id = random.randint(0, 10000)
    exporting_threads[thread_id] = ExportingThread()
    exporting_threads[thread_id].start()

    response = {"thread_id": thread_id}

    return response


@app.route('/progress/<int:thread_id>')
def progress(thread_id):
    global exporting_threads

    print(exporting_threads[thread_id].progress)

    if exporting_threads[thread_id].progress < 101:
        result = str(exporting_threads[thread_id].progress)
    else:
        result = send_file('./data/test.xlsx')

    return result


if __name__ == '__main__':
    app.run()

## Threading 
## https://stackoverflow.com/questions/24251898/flask-app-update-progress-bar-while-function-runs