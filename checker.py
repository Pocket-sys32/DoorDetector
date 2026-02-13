import serial
import tweepy
import time
import os
from dotenv import load_dotenv
load_dotenv()

CLIENTID_SECRET = os.environ.get("CLIENTID_SECRET")
CLIENTID = os.environ.get("CLIENTID")

oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id=CLIENTID,
    redirect_uri="http://127.0.0.1",
    scope=["tweet.read", "tweet.write", "users.read"],
    # Client Secret is only necessary if using a confidential client
    client_secret=CLIENTID_SECRET
)

print(oauth2_user_handler.get_authorization_url())


auth = input("Give me the link!")
access_token = oauth2_user_handler.fetch_token(
    auth
)
client = tweepy.Client(access_token["access_token"])




def readserial(comport, baudrate):
    ser = serial.Serial(comport, baudrate, timeout=0.1)
    while True:
        data = ser.readline().decode().strip()
        if data:
            print(data)
            return data

while True:
    readserial('COM3', 9600)
    distance = readserial('COM3', 9600)
    if float(distance) > 15.24:
        response = client.create_tweet(
        text="The door has opened!",
        user_auth=False)
        print(f"https://twitter.com/user/status/{response.data['id']}")

    time.sleep(300)



