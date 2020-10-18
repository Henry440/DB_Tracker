#Projekt
from files.configs import LOG_TOP_LEN, LOG_FILE, LOG_LEVELS, LOG_LVL_CONS, LOG_LVL_FILE, LOG_TO_CONSOLE, LOG_TO_FILE
#Libarys
import datetime

class logger():

    def __init__(self, source):
        self.source = source
        self.enable = True

    def _msg_builder(self, msg, lvl):
        headder = ""
        zeit = datetime.datetime.now()
        form = zeit.strftime("%Y.%m.%d-%H:%M:%S ")
        headder = headder + form
        if lvl > len(LOG_LEVELS) or lvl < 0:
            lvl = "UNDEFINED"
            headder = headder + f"[{self.source.upper()}] [{lvl}] : "
        else:
            headder = headder + f"[{self.source.upper()}] [{LOG_LEVELS[lvl]}] : "

        while len(headder) < LOG_TOP_LEN:
            headder = headder + " "

        headder = headder + msg 

        return headder

    def log(self, msg, lvl = 1):
        if(self.enable):
            msg = self._msg_builder(msg, lvl)
            if(not(LOG_TO_CONSOLE or LOG_TO_FILE)):
                print("LOGGING ist DEAKTIVIERT")
                self.enable = False
            if(LOG_TO_FILE):
                if(lvl >= LOG_LVL_FILE):
                    log_file = open(LOG_FILE, "a")
                    log_file.write(msg + "\n")
                    log_file.close()

            if(LOG_TO_CONSOLE):
                if(lvl >= LOG_LVL_CONS):
                    print(msg)
