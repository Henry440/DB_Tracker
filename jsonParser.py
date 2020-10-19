from logger import logger
from files.configs import TAG_ZUG, TAG_ABFAHRT, TAG_ANKUNFT, TAG_GENERAL, TAGS

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

    def fixMissing(self, tag):
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
            except Exception as e:
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
        return out