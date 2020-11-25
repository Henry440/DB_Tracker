# DB Tracker V2

Dies ist ein Projekt um zu überprüfen wie pünktlich die Deutsche Bahn tatsächlich ist.
Ich übernehme keine Haftung dafür das die Datensammlung mit dem Script zulässig ist.

## Wieso?

Inspirirt ist diese Projekt durch den Vortrag beim CCC von David Kriesel "Pünktlichkeit ist eine Zier".
Wo die Pünktlichkeit der DB im Fernverkehr geprüft wurde.

## Zu Ändern
In der Datei Emergency Mailer muss das Kennwort geändert werden. Ebenfalls kann der Nachichteninhalt angepasst werden. Auch die Sendene und Empfangende E-Mail muss geändert werden.

## Requirements
1. Python3.8 or newer
2. Internetconnection

## Installation
### Linux

Getestet auf Ubuntu 18.04LTS und Raspberry Pi

Linux aktuallisieren und Tor sowie Proxychains Installieren
```shell
sudo apt update -y && sudo apt upgrade -y
sudo apt install tor proxychains4
```
Optimal SQLite3 für die CLI installieren
```shell
sudo apt install sqlite3
```
Tor nach der Installation aktivieren
```shell
sudo service start tor
```

Pythonpackages Installieren
```shell
pip3 install requests
pip3 install requests[socks]
```

Sourcecode Herrunterladen
```shell
git clone https://github.com/Henry440/DB_Tracker.git
cd DB_Tracker
```

Programm Starten
```shell
python3 Main.py
```
#### Für requests über Tor
Für Requests mit Tor werden Root Rechte benötigt!
```shell
nano ./files/configs.py
```
Ändere
```python
USE_TOR = False
UPDATE_TOR = 2
RELOADTIME_TOR = 30
```
ZU
```python
USE_TOR = True
UPDATE_TOR = 1 #1 Ändert nach jedem Request 
RELOADTIME_TOR = 30 #Nach geschwindigkeit vom Netzwerkk und Hostsystem zu wählen Ideal 30 - 60 
```
