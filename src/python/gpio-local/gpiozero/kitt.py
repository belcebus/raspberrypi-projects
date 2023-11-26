from gpiozero import LED
from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()

frequency = 80

leds = [
        PWMLED("GPIO17",initial_value=False,pin_factory=factory,frequency=frequency,active_high=False),
        PWMLED("GPIO18",initial_value=False,pin_factory=factory,frequency=frequency,active_high=False),
        PWMLED("GPIO27",initial_value=False,pin_factory=factory,frequency=frequency,active_high=False),
        PWMLED("GPIO22",initial_value=False,pin_factory=factory,frequency=frequency,active_high=False),
        PWMLED("GPIO23",initial_value=False,pin_factory=factory,frequency=frequency,active_high=False),
        PWMLED("GPIO24",initial_value=False,pin_factory=factory,frequency=frequency,active_high=False),
        PWMLED("GPIO25",initial_value=False,pin_factory=factory,frequency=frequency,active_high=False),
        PWMLED("GPIO05",initial_value=False,pin_factory=factory,frequency=frequency,active_high=False),
        PWMLED("GPIO06",initial_value=False,pin_factory=factory,frequency=frequency,active_high=False),
        PWMLED("GPIO12",initial_value=False,pin_factory=factory,frequency=frequency,active_high=False)
]

def setup():
    print("Initializing...")

def destroy():
    print("Exiting...")
    for led in leds:
        led.close()

def loop():

    fade_in=0.25
    fade_out=fade_in * 1.75
    frec = fade_in / 2

    while True:

        indice = 0

        while indice < 10:
            leds[indice].pulse(fade_in_time=fade_in,fade_out_time=fade_out,n=1)
            indice = indice + 1 
            sleep(frec)

        leds.reverse()

if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()
