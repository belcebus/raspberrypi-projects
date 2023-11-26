from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()
blue_led = LED(pin="GPIO21",pin_factory=factory)
red_led = LED(pin="GPIO12",pin_factory=factory)


def loop():
    while True:
        if not red_led.is_active :
            blue_led.on()
            sleep(1)
            blue_led.off()

def destroy():
    blue_led.close()

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        