from machine import Pin

# LED auf Raspberry Pi einschalten
led = Pin(25, Pin.OUT)
led.toggle()
