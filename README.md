# DoorDetector
Doordetector is a project created for those with strict parents (like me!),
you essentially have an UNO3 hooked up to a HC-SR04 Ultrasonic Sensor and when the door isn't detected (placed 6 inches away), it uses the serial from your UNO3 and processes it into a tweet if parameters are met.
it would post a tweet! 

- Created using Arduino IDE + PyCharm (C++ & Python)
- Uses Flask + Tweepy

To use: download the requirements.txt and run it:
py install -r requirements.txt

Upload the code from /DoorDetector/ultrasound-sens/ultrasound-sens.ino

Then run using py /DoorDetector/checker.py

Thank you for checking out my basic but functional project!
