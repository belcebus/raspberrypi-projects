from gpiozero import PWMLED
from gpiozero import Button
import signal
from gpiozero.pins.pigpio import PiGPIOFactory

factory=PiGPIOFactory(host="192.168.0.172")

led_red = PWMLED(pin="GPIO17", pin_factory=factory)
button = Button(pin="GPIO18",pin_factory=factory)


def destroy():
    print("\nFinalizando")
    led_red.off()
    led_red.close()

def pulse():
    print(">>>>>>> pulsating")
    led_red.pulse(fade_out_time=0.25)

def off():
    print("<<<<<<< off")
    led_red.off()

def loop():
    button.when_activated = pulse
    button.when_deactivated = off
    signal.pause()

if __name__=="__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()