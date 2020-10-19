from logger import logger
from files.configs import OUTPUT

class writer():

    def __init__(self, name):
        self.LOGGER = logger(f"WR {name}")

    def writer(self, data):
        self.LOGGER.log("Starte schreiben", 0)
        for x in data:
            out = ""
            for i in range(len(x) - 1):
                out = out + str(x[i]) + ", "
            out = out + str(x[-1]) + "\n"

            file = open(OUTPUT, "a", encoding="utf-8")
            file.write(out)
            file.close
        self.LOGGER.log("Schreiben erfolgreich")
