#!bin/python3

import RPi.GPIO as GPIO
from time import sleep

# Pin definition
ledPin = 18
btnPin = 17

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# set led off
GPIO.output(ledPin, GPIO.LOW)

# Infinite loop
try:
    while True:
        GPIO.output(ledPin, not GPIO.input(btnPin))
        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
