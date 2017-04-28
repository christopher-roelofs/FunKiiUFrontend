try:
    import FunKiiU as fnk
except Exception:
    pass

import thread
import threading
import settings
import os
import time
from logger import log

download_list = []
downloading = 0

def download_games():
    global downloading
    global download_list
    while 1:
        time.sleep(1)
        if len(download_list) > 0:
            game = download_list[-1]
            if downloading < settings.maxDownloads:
                downloading += 1
                thread.start_new_thread(download_game, (game,))
                download_list.remove(game)


def add_game(game):
    download_list.append(game)

def cancel_download(game):
    for download in downloading:
        if game == download.getGame().listname + " - " + download.getGame().status:
            #download.stop()
            pass



class threaded_download(threading.Thread):
    def __init__(self):
        super(threaded_download, self).__init__()
        self._stop = threading.Event()
        self.game = ""

    def setGame(self,game):
        self.game = game

    def getGame(self):
        return self.game

    def stop(self):
        self._stop.set()
        self.game.status = "Canceled"
        self.game.downloadcallback()
        log("canceled download:" + self.game.listname)
        downloading.remove(self)

    def stopped(self):
        return self._stop.isSet()

    def start(self):
        global downloading
        log("downloading:" + self.game.listname)
        self.game.status = "Downloading"
        self.game.downloadcallback()
        try:
            fnk.process_title_id(self.game.titleid, self.game.titlekey, self.game.name, self.game.region, settings.downloadDir, settings.retry,
                                 self.game.ticket, settings.patchDEMO, settings.patchDLC, False, False)
            self.game.status = "Complete"
            self.game.downloadcallback()
            log("done downloading:" + self.game.listname)
            downloading.remove(self)
        except Exception as e:
            self.game.status = "Failed"
            self.game.downloadcallback()
            downloading.remove(self)
            log("download failed:" + self.game.listname)

def download_game(game):
    global downloading
    log("downloading:" + game.listname)
    game.status = "Downloading"
    game.downloadcallback()
    try:
        fnk.process_title_id(game.titleid, game.titlekey, game.name, game.region, os.curdir, 3, game.ticket,settings.patchDEMO, settings.patchDLC, False, False)
        game.status = "Complete"
        game.downloadcallback()
        log("done downloading:" + game.listname)
        downloading -= 1
    except Exception as e:
        game.status = "Failed"
        game.downloadcallback()
        downloading -= 1
        log("download failed:" + game.listname)


try:
    thread.start_new_thread(download_games,())
except:
    log("Error: unable to start thread")