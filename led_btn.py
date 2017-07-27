import RPi.GPIO as GPIO
import time

# Pin definition

ledPin = 18
btnPin = 16

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(ledPin, GPIO.LOW)

# Infinite loop
try:
    while 1:
        if GPIO.input(btnPin):  #not pressed
            GPIO.output(ledPin, GPIO.LOW)
        else:
            GPIO.output(ledPin, GPIO.HIGH)
except KeyboardInterrupt:
    GPIO.cleanup()
    