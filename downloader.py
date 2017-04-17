import FunKiiU as fnk
import thread
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
    #pass
except:
    log("Error: unable to start thread")