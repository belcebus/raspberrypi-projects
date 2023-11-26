from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import time

factory = PiGPIOFactory(host="192.168.0.172")

led = LED(21,pin_factory=factory)

start = time()
for i in range(1000000):
    led.on()
    led.off()
end = time()

frequency = 1000000 / (end - start)
print(f'Frequency: {frequency} Hz')