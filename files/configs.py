# Wartezeiten
SLEEP_TIME = 60 * 30
LOOK_BEHIND = 60 * 45

# Stationsverwaltung
STATIONEN = "files/stations.csv"
OUTPUT = "out/Daten.csv"

# JSON TAGGS
# NAME = ([HEADDER KEY], [[KEY 1], [KEY 2], [KEY 3], ...., [KEY N]])
TAG_STATION = (["currentStation"], ["title", "id"])
TAG_GENERAL = ([], ["o", "initialDeparture", "scheduledDestination", "lineNumber", "id", "rawId", "mediumId", "destination", "platform", "scheduledPlatform", "cancelled"])
TAG_ANKUNFT = (["arrival"], ["scheduledTime", "time", "platform", "scheduledPlatform", "hidden", "cancelled", "delay"])
TAG_ABFAHRT = (["departure"],["scheduledTime", "time", "platform", "scheduledPlatform", "hidden", "cancelled", "delay"])
TAG_ZUG     = (["train"],["longDistance", "name", "number", "type"])

TAGS = [TAG_STATION, TAG_GENERAL, TAG_ANKUNFT, TAG_ABFAHRT, TAG_ZUG]

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