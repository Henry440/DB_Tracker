from logger import logger

import json

class parser():

    def __init__(self, content, name):
        self.LOGGER = logger(f"LG {name}")
        self.content = content["lookbehind"] #Alle Daten einer Station 
        self.zuege = []                      #Beinhaltet Daten sortiert nach zug
        for i in self.content:
            self.zuege.append(i)
        self.LOGGER.log(f"Gefundene Abfahrten/Ankünfte {len(self.zuege)}",1)
        if(len(self.zuege) == 0):
            self.LOGGER.log(str(content))

    def manage(self):
        pass