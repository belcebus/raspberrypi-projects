from gpiozero import LEDBarGraph
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()
bar = LEDBarGraph("GPIO17","GPIO18","GPIO27","GPIO22","GPIO23","GPIO24","GPIO25","GPIO05","GPIO06","GPIO12",pin_factory=factory,pwm=True)

def destroy():
    print("\nSaliendo")
    bar.close()

def loop():
    decremento=0.1
    valor = 10
    while True:
        #bar.off()
        valor=valor - decremento
        if valor <= 0 or valor >=10:
            decremento = -1 * decremento
        bar.value=-valor/10

if __name__ == "__main__": 
    try:
        loop()
    except KeyboardInterrupt:
        destroy()