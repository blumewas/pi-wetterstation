# Raspberry Pi Wetterstation

Dieses Repo beinhaltet den Inhalt für einen Kurs, um gemeinsam mit Schülern ein Wetterstation basierend auf
dem Raspberry Pico zu bauen. Der Kurs hat eine ungefähre Dauer von drei Tagen á 4 Std.

Diese README dient soll der anleitenden Person einen Überblick über den Inhalt und die Lernziele der einzelnen
Tage verschaffen sowie die benötigten Materialien aufzählen.

## Materialliste

Für die Tage bzw. Schritte werden die folgenden Materialien benötigt.

### Allgemein:
- Raspberry Pi Pico (Anm.: Die Variante ohne WLan ist ausreichend. Um Frust beim Löten zu vermeiden, sollte dieser mit Headern gekauft werden)
- Breadboards (das von mir verwendete Board hat 400 Kontakte (aufgeteilt auf 14 Spalten und 30 Reihen). Die Abmessungen lauten 83 x 55mm)
- Jumperkabel o. Krokoklemmen o. Kupferlitze
- USB auf Micro-USB Kabel
- Ein Computer mit VS Code o. Thonny Python IDE

### Einführung:
- LEDs
- Widerstand 100 Ohm
- Druckknopf

- (weitere Programme mit Helligkeit?)

### Wetterstation:
- DHT 22 (Temperatur und Luftfeuchtigkeits Sensor)
- A3144 (Hall Effekt Sensor)
- Kugellager
- Magnete (hier kreisförmig - Durchmesser 10mm)
- Plastikstab
- Weihnachtskugel Bastelhälften

## Kurstage

### Tag 1

Am ersten Tag sollen die Teilnehmer erste kleine Programme schreiben und verstehen lernen.
Beispiel Skripte sind im Ordner start/ zu finden. Auch sollen sie lernen Schaltungen mit Hilfe
des Breadboards zu entwickeln.

Zu erst sollen die Teilnehmer das Skript **flash.py** entwickeln. Dieses schaltet die LED auf
dem Raspberry Pi ein.

Als zweites sollen sie eine LED mit Hilfe des Breadboards an den Raspberry Pi anschließen. Über das
Ansteuern der entsprechenden PINs eine LED zum leuchten bringen. Diese soll anschließend mit Hilfe
eines Timers zum blinken gebracht werden.

Zum Schluss soll ein Schalter in die Schaltung eingbaut werden, der die LED auf Knopfdruck einschaltet.

### Tag 2

Anschließen der Sensoren - Bauen des Anemometer - Schreiben von Log Dateien

### Tag 3

Auswertung der Logs mit Python und Graphenerstellung
