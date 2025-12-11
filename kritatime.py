# THIS CODE WILL CRASH KRITA. IT RUNS AN INFINITE LOOP ONCE YOU SELECT IT IN TOOLS > SCRIPT. 
from krita import Krita
from krita import Extension


import os
import time
import base64
import urllib.request
import urllib.error
import json
# import psutil - doesn't work and doesn't seem to impact anything?
import datetime # had issues with UTC timezone so instead of importing datetime from datetime, just imported datetime instead

WAKATIME_API_KEY = 'API key found on hackatime'
WATCH_FOLDER = "FOLDER PATH NAME (on linux using / is fine. needs to start with / to work. e.g. /home/name/Documents/art/)"
HEARTBEAT_INTERVAL = 60
CHECK_INTERVAL = 30


def send_heartbeat(file_path, project_name):
    encoded_key = base64.b64encode(WAKATIME_API_KEY.encode()).decode()
    headers = {
        "User-Agent": "user agent here", # not sure if this is actually necessary. should test that
        "Authorization": f"Bearer {WAKATIME_API_KEY}", # didn't work when I used the encoded_key
        "Content-Type": "application/json"
    }
    payload = {
        "time": str(datetime.datetime.now(datetime.timezone.utc)),
        "entity": file_path,
        "type": "file",
        "category": "coding",
        "is_write": True,
        "project": project_name,
        "language": "arting",
        "plugin": "kritatime"
    }
    req = urllib.request.Request(
        url='https://hackatime.hackclub.com/api/hackatime/v1/users/current/heartbeats',
        data=json.dumps(payload).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    try:
        with urllib.request.urlopen(req) as response:
            print(f"[{datetime.datetime.now()}] Sent heartbeat: {response.status}")
    except urllib.error.HTTPError as e:
        print(f"[{datetime.datetime.now()}] Error sending heartbeat: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print("[{}] Network error: {}".format(datetime.datetime.now(), e.reason))

class myExtension(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass


    def uhh(self):
        last_sent = 0
        last_mod_time = 0

        while True:
            most_recent_file = None 
            most_recent_time = 0

            for root, _, files in os.walk(WATCH_FOLDER):
                for file in files:
                    if file.endswith(".kra"):
                        full_path = os.path.join(root, file)
                        try:
                            mod_time = os.path.getmtime(full_path)
                        except FileNotFoundError:
                            continue
                        if mod_time > most_recent_time:
                            most_recent_time = mod_time
                            most_recent_file = full_path

            now = time.time()
            if most_recent_file and most_recent_time > last_mod_time and now - last_sent > HEARTBEAT_INTERVAL:
                project_name = os.path.basename(os.path.dirname(most_recent_file))
                send_heartbeat(most_recent_file, project_name)
                last_sent = now
                last_mod_time = most_recent_time

            time.sleep(CHECK_INTERVAL)


    def createActions(self, window):
        action = window.createAction("theAction","krita time")
        action.triggered.connect(self.uhh)
        

Krita.instance().addExtension(myExtension(Krita.instance()))
