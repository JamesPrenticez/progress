import random
import threading
import time

from flask import Flask, render_template


class ExportingThread(threading.Thread):
    def __init__(self):
        self.progress = 0
        super().__init__()

    def run(self):
        # Your exporting stuff goes here ...
        for _ in range(10):
            time.sleep(1)
            self.progress += 10


exporting_threads = {}
app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    global exporting_threads

    thread_id = random.randint(0, 10000)
    exporting_threads[thread_id] = ExportingThread()
    exporting_threads[thread_id].start()

    return render_template('index.html', thread_id=thread_id)




@app.route('/progress/<int:thread_id>')
def progress(thread_id):
    global exporting_threads

    return str(exporting_threads[thread_id].progress)


if __name__ == '__main__':
    app.run()

## Threading 
## https://stackoverflow.com/questions/24251898/flask-app-update-progress-bar-while-function-runs