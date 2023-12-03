from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory('raspberrypi.local')

red = LED("GPIO13",pin_factory=factory)

def setup():
    print("Setup components")

def loop():
    print("Entering the loop")
    while True:
        print(">>>>>>> turn on")
        red.on()
        sleep(0.5)
        print(">>>>>>> turn off")
        red.off()
        sleep(0.5)

def destroy():
    print("Keyboard interrupted, switcing off and finish")
    red.off()

if __name__ == '__main__': # Program entrance
    print("Program starting ... \n")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()