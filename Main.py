from logger import logger
from manager import manager
from files.configs import SLEEP_TIME
import emergencyMailere

from time import sleep

SOURCE = "Main"
LOGGER = logger(SOURCE)

if __name__ == "__main__":
    LOGGER.log("Programmstart",0)
    m = manager()
    LOGGER.log("Inizialisierung beendet")
    try:
        while True:
            m.run()
            LOGGER.log("Abfrage Erfolgreich das Programm legt sich schlafen")
            LOGGER.log("Alles läuft perfekt")
            sleep(SLEEP_TIME)
    except KeyboardInterrupt as e:
        LOGGER.log("Beende das Programm")
    except Exception as e:
        LOGGER.log("Main Schleife konnte nicht gestartet werden!!!", 4)
        LOGGER.log(str(e),4)
        emergencyMailere.mail2()
else:
    LOGGER.log("Main kann nicht Importiert werden!", 4)
    exit()