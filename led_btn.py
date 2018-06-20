#!bin/python3

import RPi.GPIO as GPIO
import time

# Pin definition
ledPin = 18
btnPin = 24

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(ledPin, GPIO.LOW)

# Infinite loop
try:
    while True:
        if GPIO.input(btnPin) == 0:  #not pressed
            print("button pressed")
            GPIO.cleanup()
except KeyboardInterrupt:
    GPIO.cleanup()
    