from logger import logger
from files.configs import TAG_ABFAHRT, TAG_ANKUNFT, TAG_GENERAL, TAGS

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

    def fixMissing(self, tag, datas):
        ret = []
        return ret

    def getKeys(self, tag):
        ret = []
        return ret

    def manage(self):
        json_datas_raw = []
        for i in TAGS:
            datas = []
            datas = self.getKeys(i)
            datas = self.fixMissing(i, datas)
            json_datas_raw.append(datas)