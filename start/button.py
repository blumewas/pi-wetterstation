from machine import Pin, Timer
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Enlosschleife die den Druck auf den Knopf erkennt
while True:
    if button.value():
        led.toggle()
        time.sleep(0.5)
