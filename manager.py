from files.configs import USE_TOR, STATIONEN, UPDATE_TOR, RELOADTIME_TOR
from abfrage import abfrage
if USE_TOR:
    import os

from logger import logger
from jsonParser import parser
import emergencyMailere
from writer import writer

from time import sleep
import requests

class manager():

    def __init__(self):
        SOURCE = "Manager"
        self.LOGGER = logger(SOURCE)
        self.LOGGER.log("Manager wird Inizialisiert")

        self.zyklus = 0

        file = open(STATIONEN, "r", encoding="utf-8")
        content = file.read()
        file.close()

        zeilen = content.split("\n")[1:]
        self.abfragen = []
        for i in zeilen:
            args = i.split(", ")
            self.LOGGER.log(f"Erstelle Abfrage {args[0]}", 0)
            f = abfrage(str(args[0]), str(args[1]), int(args[2]))
            self.abfragen.append(f)

        self.LOGGER.log("Inizialisierung Abgeschlossen")
            
    def run(self):
        self.LOGGER.log("Starte Durchlauf")
        try:
            for x in self.abfragen:
                content = x.abfrage()
                if(content == -1):
                    self.LOGGER.log(f"Überspringe Auswertung für {x.station}")
                else:
                    handler = parser(content, x.station)
                    try:
                        datas = handler.manage()
                        wr = writer(x.station)
                        wr.writer(datas)
                    except Exception as e:
                        self.LOGGER.log(f"Fehler beim Verarbeiten : {e}", 2)
            self.zyklus = self.zyklus + 1
            if(USE_TOR):
                if(self.zyklus >= UPDATE_TOR):
                    try:
                        self.LOGGER.log(f"Änderung der IP wird begonnen das Dauer {RELOADTIME_TOR}s")
                        os.system("sudo service tor restart")
                        sleep(RELOADTIME_TOR)
                        self.LOGGER.log("Die IP wurde geändert", 2)

                        s = requests.session()
                        s.proxies['http'] = 'socks5h://localhost:9050'
                        r = s.get("http://httpbin.org/ip")
                        self.LOGGER.log(f"Neue IP : {r.content}")

                        self.zyklus = 0
                    except Exception as e:
                        self.LOGGER.log("Tor konnte nicht neugestartet werden um die IP zu ändern", 4)
                        self.LOGGER.log(str(e),4)
                        self.LOGGER.log("Beende das Programm", 4)
                        emergencyMailere.mail2()
                        exit()
        except Exception as e:
            self.LOGGER.log("Etwas bei dem Abfragezyklus ist schiefgelaufen",3)
            self.LOGGER.log(str(e),3)
            emergencyMailere.mail2()