from logger import logger
from files.configs import OUTPUT, DATABASE, TABLE_NAME

import sqlite3

class writer():

    def __init__(self, name):
        self.LOGGER = logger(f"WR {name}")
        self.conn = sqlite3.connect(DATABASE)

    def fileWriter(self, data):
        for x in data:
            out = ""
            for i in range(len(x) - 1):
                out = out + str(x[i]) + ", "
            out = out + str(x[-1]) + "\n"

            file = open(OUTPUT, "a", encoding="utf-8")
            file.write(out)
            file.close

    def dbWriter(self, data):
        pass

    def writer(self, data):
        self.LOGGER.log("Starte schreiben", 0)
        self.fileWriter(data)
        self.dbWriter(data)
        self.LOGGER.log("Schreiben erfolgreich")
