from thing import PiThing
from time import sleep

# Create an instance of PiThing
pi_thing = PiThing()

while True:
    pi_thing.set_led(True)
    sleep(2)
    pi_thing.set_led(False)
    sleep(2)