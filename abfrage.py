import requests
from time import sleep

from files.configs import USE_TOR, BASE_URL
from logger import logger

class abfrage():

    def __init__(self, station, evaId, retrys):
        SOURCE = f"AF {station}"
        self.LOGGER = logger(SOURCE)
        self.LOGGER.log("Inizialisiere Abfrage")
        self.station = station
        self.evaId = evaId
        self.retrys = retrys

    def abfrage(self):
        self.LOGGER.log("Starte Abfrage", 0)
        errors = 0
        s = requests.session()
        if(USE_TOR):
            s.proxies['http'] = 'socks5h://localhost:9050'
            s.proxies['https'] = 'socks5h://localhost:9050'
        else:
            s.proxies = {}

        erfolg = False
        params = {"lookbehind":30}
        while not(erfolg):
            try:
                r = s.get(f"{BASE_URL}{self.evaId}", params=params)
                self.LOGGER.log(f"Abfrage Erfolgreich im Anlauf {errors + 1}", 0)
                erfolg = True
                data = r.json()
            except Exception as e:
                errors = errors + 1
                if errors >= self.retrys:
                    self.LOGGER.log("Bei der Abfrage trat ein Fehler auf Maximale Retrys", 3)
                    self.LOGGER.log(str(e), 3)
                    return -1
                
                
        self.LOGGER.log(f"Abfrage Beendet {r}",1)
        return data
    