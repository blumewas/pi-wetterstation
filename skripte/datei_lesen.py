import os

# wetter log daten auslesen
file = open('wetter_daten.txt', 'r')
print(file.read())
file.close()
