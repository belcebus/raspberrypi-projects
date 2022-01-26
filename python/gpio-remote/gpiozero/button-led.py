from gpiozero import LED
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory('192.168.0.172')

red = LED("GPIO17",pin_factory=factory)
but = Button("GPIO18",pin_factory=factory)


def setup():
    print("Setup components")

def loop():
    print("Entering the loop")
    while True:
        if but.is_active:
            red.on()
            print(">>>>>> Button pressed")
        else: 
            print(">>>>>> led off")
            red.off()
        sleep(0.1)
        
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