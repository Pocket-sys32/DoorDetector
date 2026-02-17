import threading
import serial
import tweepy
import os
import datetime
from dotenv import load_dotenv
from flask import Flask



load_dotenv()
CONSUMER = os.environ.get("CONSUMER")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

client = tweepy.Client(consumer_key = CONSUMER,
                       consumer_secret = CONSUMER_SECRET,
                       access_token = ACCESS_TOKEN,
                       access_token_secret = ACCESS_SECRET)

app = Flask(__name__)

#starting vars/dict
door_state = {"status": "unknown", "last_tweet": None}
last_state = False

def handler():
    #Reads the serial for output
    global last_state
    ser = serial.Serial('COM3', 9600)
    while True:
        try:
            dist = float(ser.readline().decode().strip())
            if dist > 15.24:
                print("Door open!")
                door_state["status"] = "Open"
                if not last_state:
                    print("Door detected Open! --> Tweeting!")
                    now = str(datetime.datetime.now())

                    try:
                        response = client.create_tweet(
                            text=f"The door has been opened. {now}")
                        print(f"https://twitter.com/user/status/{response.data['id']}")
                    except Exception as e:
                        print(f"Failed to tweet: {e}")
                    last_state = True
            elif dist < 15.24:
                door_state["status"] = "Closed"
                if last_state:
                    print("Door detected, allowing tweets.")
                    last_state = False
        except ValueError:
            pass

@app.route("/")
def dashboard():
    return f"<h1>Door Status: {door_state['status']}</h1>"

if __name__ == "__main__":
    #new thread for running in background
    x = threading.Thread(target=handler)
    # Daemon = stops on CTRL C (closing application)
    x.daemon = True
    # start the worker
    x.start()
    # start the application
    app.run(debug=True,use_reloader = False,port=5000)


