import serial
import tweepy
import time
import os
from dotenv import load_dotenv
load_dotenv()

BEARER_KEY = os.environ.get("BEARER_KEY")
ACCESS_KEY = os.environ.get("ACCESS_KEY")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")


api = tweepy.Client(bearer_token=BEARER_KEY,
                    access_token=ACCESS_KEY,
                    access_token_secret=ACCESS_SECRET,
                    consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET)

auth = tweepy.OAuth1UserHandler(
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
)

def readserial(comport, baudrate):
    ser = serial.Serial(comport, baudrate, timeout=0.1)
    while True:
        data = ser.readline().decode().strip()
        if data:
            print(data)

while True:
    readserial('COM3', 9600)
    distance = readserial('COM3', 9600)
    if distance > 15.24:
        api.create_tweet(text='Pockets mouse has moved!')
    time.sleep(300)




