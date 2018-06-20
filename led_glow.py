#!bin/python3
import RPi.GPIO as GPIO
import time

# Pin definition
ledPin = 18
pwmLed = 16

duty = 70

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(pwmLed, GPIO.OUT)

pwm = GPIO.PWM(pwmLed, 200) # set pwm freq = 200Hz
GPIO.output(ledPin, GPIO.HIGH)
pwm.start(duty)

# Infinite loop
try:
    while 1:
        time.sleep(0.5)
        pwm.ChangeDutyCycle(duty)
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(100 - duty)
        GPIO.output(ledPin, GPIO.HIGH)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()