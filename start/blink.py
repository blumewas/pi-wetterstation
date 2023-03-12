from machine import Pin, Timer

# PIN an dem die LED angeschlossen ist
led = Pin(15, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

# Alle 2,5s die angeschlossene LED blinken lassen
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
