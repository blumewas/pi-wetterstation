from machine import Pin, Timer
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

timer = Timer()

def blink(timer):
    led.toggle()

# LED leuchtet solange man den Knopf drückt
while True:
    if button.value():
        print("Button pressed")
        timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
        time.sleep(0.5)
    else:
        timer.deinit()
        time.sleep(0.5)
