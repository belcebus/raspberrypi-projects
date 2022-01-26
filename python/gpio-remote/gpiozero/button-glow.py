from gpiozero import PWMLED
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host="192.168.0.172")
red_led = PWMLED(pin="GPIO17",pin_factory=factory)
button = Button(pin="GPIO18", pin_factory=factory)

def setup():
    print("setup ...")

def destroy():
    print("Saliendo ... ")
    red_led.off()

def loop():
    print("Looping")
    valor = 0.0
    incremento = 0.025
    while True:
        if button.is_active: 
            print(f">>>>>>>> Button pressed {valor}")
            valor = round(valor + incremento,3)
            if valor > 1:
                valor = 1
            red_led.value = valor
        else:
            print(f"<<<<<<<< Off {valor}")
            valor = round(valor - incremento,3)
            if valor < 0:
                valor = 0
            red_led.value = valor
        sleep(0.01)

if __name__ == "__main__":
    print("---- Inicializando programa -----\n---- Button Glow ----")
    setup()
    try:
            loop()
    except KeyboardInterrupt:
        destroy()

