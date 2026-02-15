import serial
import tweepy
import datetime
import os
from flask import Flask
from dotenv import load_dotenv
load_dotenv()

CONSUMER = os.environ.get("CONSUMER")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

client = tweepy.Client(consumer_key = CONSUMER,
                       consumer_secret = CONSUMER_SECRET,
                       access_token = ACCESS_TOKEN,
                       access_token_secret = ACCESS_SECRET)


#starting code
last_state = False


app = Flask(__name__)

def readserial(comport, baudrate):
    ser = serial.Serial(comport, baudrate, timeout=0.1)
    while True:
        data = ser.readline().decode().strip()
        if data:
            print(data)
            return data


@app.route("/")
def tweet():
    global last_state
    readserial('COM3', 9600)
    now = str(datetime.datetime.now())
    dist = float(readserial('COM3', 9600))
    if dist > 15.24:
        door_open = True
    else:
        door_open = False
    if door_open and not last_state:
        last_state = True
        response = client.create_tweet(
        text=f"The wall has been detected. {now}")
        print(f"https://twitter.com/user/status/{response.data['id']}")
        return f"<p>https://twitter.com/user/status/{response.data['id']}</p>"
    last_state = door_open
    return "No data"

