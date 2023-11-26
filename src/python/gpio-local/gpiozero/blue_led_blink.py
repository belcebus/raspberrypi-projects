from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()
blue_led = LED(pin="GPIO21",pin_factory=factory)


def loop():
    while True:
        print(">>>>>> Led on")
        blue_led.on()
        sleep(1)
        print(">>>>>> Led off")
        blue_led.off()
        sleep(1)

def destroy():
    blue_led.close()

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()