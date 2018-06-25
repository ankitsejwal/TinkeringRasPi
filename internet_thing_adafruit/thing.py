import RPi.GPIO as GPIO 

LED_PIN     = 23
SWITCH_PIN  = 24

class PiThing(object):

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT) # led as an output
        GPIO.setup(SWITCH_PIN, GPIO.IN)  # switch as an input

    def read_switch(self):
        ''' read the state of the switch '''
        return 'The switch is ON' if GPIO.input(SWITCH_PIN) else 'The swtich is OFF'

    def set_led(self, value):
        ''' turn led on or off by setting a value '''
        GPIO.output(LED_PIN, value)
