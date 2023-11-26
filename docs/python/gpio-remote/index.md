# gpio-remote

## gpiozero (GPIO Zero)

    man remote-gpio

A simple interface to GPIO devices with Raspberry Pi. The library includes interfaces to many simple everyday components, as well as some more complex things like sensors, analogue-to-digital converters, full colour LEDs, robotics kits and more.

GPIO Zero builds on a number of underlying pin libraries, including RPi.GPIO and pigpio, each with their own benefits. You can select a particular pin library to be used, either for the whole script or per-device, according to your needs. 

PIN Factories

* __rpigpio__
* lgpio
* rpio
* pigpio
* native

PiGPIO

Uses the pigpio library to interface to the Pi’s GPIO pins. The pigpio library relies on a daemon (pigpiod) to be running as root to provide access to the GPIO pins, and communicates with this daemon over a network socket.

While this does mean only the daemon itself should control the pins, the architecture does have several advantages:

* Pins can be remote controlled from another machine (the other machine doesn’t even have to be a Raspberry Pi; it simply needs the pigpio client library installed on it)
* The daemon supports hardware PWM via the DMA controller
* Your script itself doesn’t require root privileges; it just needs to be able to communicate with the daemon.



```
pip list
```

Control node:

* __gpiozero 1.6.2__ -> interfaz para unificar las diferentes librerías para interactuar con el puerto GPIO.
* __pigpio 1.78__ -> Librería usada para comunicarse con el demonio pigpiod en la raspberry, tiene la peculariedad de que permite el acceso remoto al puerto GPIO.

Raspberrypi:

* Activate the __remote access__ to the GPIO (raspi-comnfig -> Interfaces)
* Enable the __pigpiod__ (pigpio daemon)
* (optional) gpiozero 1.6.2 
* (Optional) RPi.GPIO 0.7.0

### Projects

* [Red led](projects/gpio-remote-red-led.md)

