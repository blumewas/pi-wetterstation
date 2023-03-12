from machine import Pin, Timer
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        print("Button pressed")
        led.toggle()

        print(led.value())
        time.sleep(0.5)
