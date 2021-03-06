from logger import logger
from files.configs import TAG_ZUG, TAG_ABFAHRT, TAG_ANKUNFT, TAG_GENERAL, TAGS, TAG_STATION

import json

class parser():

    def __init__(self, content, name):
        self.LOGGER = logger(f"LG {name}")
        self.LOGGER.log("Parser wird gestartet", 1)
        self.name = name
        self.content = content["lookbehind"] #Alle Daten einer Station 
        self.zuege = []                      #Beinhaltet Daten sortiert nach zug
        try:
            for i in self.content:
                self.zuege.append(i)
        except Exception as e:
            try:
                self.zuege.append(self.content[0])
            except Exception as fat:
                self.LOGGER.log("Harter Fehler", 3)
                self.LOGGER.log(str(e),3)
                self.LOGGER.log(str(fat),3)
        self.LOGGER.log(f"Gefundene Abfahrten/Ankünfte {len(self.zuege)}",1)
        

    def fixMissing(self, tag):
        self.LOGGER.log("Fix Fehlende einträge", 0)
        ret = []
        for i in range(len(tag[1])):
            ret.append("NA")
            i = i
        return ret

    def getKeys(self, tag, zug):
        ret = []
        if(tag[0] != []):
            try:
                zug = zug[tag[0][0]]
            except Exception:
                return self.fixMissing(tag)#Der Headdertag existiert nicht!!!!, Alles als NA buchen
        for i in tag[1]:
            try:
                ret.append(zug[i])
            except Exception:
                ret.append("NA")
        return ret

    def manage(self):
        out = []
        for zug in self.zuege:
            zeile = []
            for i in TAGS:
                datas = []
                datas = self.getKeys(i, zug)
                for dat in datas:
                    zeile.append(dat)
            out.append(zeile)
        self.LOGGER.log("Verarbeitung abgeschlossen")
        return out