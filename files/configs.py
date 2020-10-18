# Wartezeiten
SLEEP_TIME = 60 * 30
LOOK_BEHIND = 60 * 45

# Stationsverwaltung
STATIONEN = "files/stations.csv"
OUTPUT = "out/Daten.csv"

# Requests
USE_TOR = False
UPDATE_TOR = 2 #Restart Tor nach n Zyklusen (Linux Only)
RELOADTIME_TOR = 30
BASE_URL = "https://marudor.de/api/iris/v1/abfahrten/"

# Logging
LOG_FILE = "out/log.txt"
LOG_TO_FILE = True
LOG_TO_CONSOLE = True
LOG_LEVELS = ["DEBUG", "INFO", "WARN", "ERROR", "FATAL"]
LOG_LVL_FILE = 0
LOG_LVL_CONS = 1
LOG_TOP_LEN = 44