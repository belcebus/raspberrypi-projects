from gpiozero import LED
from time import time

led = LED(21)

start = time()
for i in range(1000000):
    led.on()
    led.off()
end = time()

frequency = 1000000 / (end - start)
print(f'Frequency: {frequency} Hz')