# Bibliotheken laden
from machine import Pin
from utime import sleep
from dht import DHT22

log_datei = "wetter_daten.txt"

# Name der Log Datei
log_zeile = "{} - {}°C - {}% \n"

# Anzahl der Zeilen in Log Datei
num_lines=sum(1 for line in open(log_datei))

count=1

# Initialisierung GPIO und DHT22
sleep(1)
dht22_sensor = DHT22(Pin(15, Pin.IN, Pin.PULL_UP))

def print_messung(temperatur, luft_feuchte):
    print(log_zeile.format(count, temperatur, luft_feuchte))


def log_messung(temperatur, luft_feuchte):

    with open(log_datei, 'a') as f:
        f.write(log_zeile.format(num_lines + count, temperatur, luft_feuchte))

        f.flush()

# Wiederholung (Endlos-Schleife)
while True:
    # Messung durchführen
    dht22_sensor.measure()
    # Werte lesen
    temp = dht22_sensor.temperature()
    humi = dht22_sensor.humidity()
    # Werte ausgeben
    print_messung(temp, humi)

    # Werte Datei schreiben
    log_messung(temp, humi)

    count+=1
    sleep(3)
