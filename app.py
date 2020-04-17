from flask import Flask, request, jsonify
import os
from flask_cors import CORS
import csv
from apscheduler.schedulers.background import BackgroundScheduler

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#cron scheduler to fetch records
sched = BackgroundScheduler(daemon=True)

def fetch():
    os.system('python run.py')

sched.add_job(fetch, 'cron', minute='*', jitter=120)
sched.start()

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/test', methods=['GET'])
def ping_pong():
    return jsonify('Flask Background Scheduler Cron Job')

if __name__ == '__main__':
    app.run()
