#!/usr/bin/python

from Tkinter import *
from ttk import *

import threading
import time

from logger import log
import settings
import util
import json

gamelist_array = []

def save_settings():
    settings.set_title_key_url(url_input.get())
    settings.save_settings()




root = Tk()
root.title("FunKiiU Frontend")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
note = Notebook(root)
note.columnconfigure(0, weight=1)
note.rowconfigure(0, weight=1)
note.grid(sticky=NSEW)

#search_tab stuff here
search_tab = Frame(note)
search_tab.columnconfigure(0, weight=1)
search_tab.columnconfigure(1, weight=1)
search_tab.rowconfigure(0, weight=1)
searchlist = Listbox(search_tab, height=20, width=80)
searchlist.config(width=80)
searchlist.grid(row=0, column=0, sticky=NSEW, columnspan=2)
searchlist.columnconfigure(0, weight=1)
searchlist.rowconfigure(0, weight=1)
downloadlist = Listbox(search_tab, height=20, width=20)
downloadlist.grid(row=0, column=3, sticky=N+S)

#players_tab stuff here
players_tab = Frame(note)
players_tab.columnconfigure(0, weight=1)
players_tab.rowconfigure(0, weight=1)
playerlist = Listbox(players_tab, height=20, width=20)
playerlist.grid(row=0, column=1, sticky=N+S)
infobox = Text(players_tab, height=10, width=80)
infobox.grid(row=0, column=0, sticky=N+E+W)

#settings_tab stuff here
settings_tab = Frame(note)
settings_tab.rowconfigure(0, weight=1)
settings_tab.rowconfigure(1, weight=1)
settings_tab.rowconfigure(2, weight=1)


url_label = Label(settings_tab, text="Title Key Website:")
url_label.grid(row=0, column=0)
url_input = Entry(settings_tab, width=20)
url_input.grid(row=0, column=1, sticky=W)
url_label_cont = Label(settings_tab, text=" (https://xxxx.xxxxxxxxx.com/)")
url_label_cont.grid(row=0, column=3)

save_btn = Button(settings_tab, text="Save", command=save_settings)
save_btn.grid(row=7, column=0, sticky=E)
spacer = Label(settings_tab).grid(row=8, column=0)

#system_tab stuff here
system_tab = Frame(note)

time_var = StringVar()
time_var.set("Time: 0m")
time_label = Label(system_tab,width=15,textvariable=time_var)
time_label.grid(row=0, column=0)


def listclick(e):
    show_player_info(str(playerlist.get(playerlist.curselection())))


def handler():
    root.destroy()

def check_tilekey_json():
    try:
        with open('titlekeys.json') as jsonfile:
            parsed_json = json.load(jsonfile)
            for game in parsed_json:
                gamelist_array.append(game)
            gamelist_array.sort()
            gamelist_array.reverse()
    except IOError as e:
        if (settings.titleKeyURL != ""):
            util.download_titlekeys_json()
        else:
            log("Title key site not set in settings")

def refresh_gamelist():
    for game in gamelist_array:
        if (game["name"] == "1001 Spikes"):
            searchlist.insert(END, game["name"] + "-" + util.decode_titleid(game["titleID"]) + "-" + util.get_title_size(game["titleID"]))

playerlist.bind('<<ListboxSelect>>', listclick)
note.add(search_tab, text="Search")


note.add(settings_tab, text= "Settings")

note.add(system_tab, text="Info")

root.protocol("WM_DELETE_WINDOW", handler)

# initialization steps
url_input.insert(0,settings.titleKeyURL)
check_tilekey_json()
refresh_gamelist()


try:
    root.mainloop()
except (KeyboardInterrupt, SystemExit):
    sys.exit()