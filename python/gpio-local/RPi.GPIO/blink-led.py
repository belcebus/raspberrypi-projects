import RPi.GPIO as GPIO
from time import sleep

ledPin = 21

def setup():
    print("Setup system")
    print(GPIO.VERSION)
    GPIO.setmode(GPIO.BCM) # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT) # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW) # make ledPin output LOW level
    print ('using pin %d'%ledPin)

def loop():
    print("Executing main function")

    print(GPIO.getmode())
    while True: 
        print(">>>>> led on")
        GPIO.output(ledPin,GPIO.HIGH)
        sleep(1)
        print("<<<<< led off")
        GPIO.output(ledPin,GPIO.LOW)
        sleep(1)

def destroy():
    print("Exiting...")
    GPIO.cleanup()

if __name__ == "__main__" :
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()