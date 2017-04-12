#!/usr/bin/python

from Tkinter import *
from ttk import *

import threading
import time

from logger import log
from util import *
from settings import *
import json
from unidecode import unidecode

gamelist_array = []

def save_settings():
    settings.set_title_key_url(url_input.get())
    settings.save_settings()
    refresh_gamelist()

def toggle_ticket_only():
    if ticketonly_chk.get() == 1:
        settings.ticketOnly = True
    else:
        settings.ticketOnly = False

def toggle_patch_demo():
    if patchdemo_chk.get() == 1:
        settings.patchDEMO = True
    else:
        settings.patchDEMO = False

def toggle_show_usa():
    if showusa_chk.get() == 1:
        if "USA" not in settings.filters:
            settings.filters.append("USA")
    else:
        if "USA" in settings.filters:
            settings.filters.remove("USA")

def toggle_show_jpn():
    if showjpn_chk.get() == 1:
        if "JPN" not in settings.filters:
            settings.filters.append("JPN")
    else:
        if "JPN" in settings.filters:
            settings.filters.remove("JPN")

def toggle_show_eur():
    if showeur_chk.get() == 1:
        if "EUR" not in settings.filters:
            settings.filters.append("UER")
    else:
        if "EUR" in settings.filters:
            settings.filters.remove("EUR")

def toggle_show_dlc():
    if showdlc_chk.get() == 1:
        if "DLC" not in settings.filters:
            settings.filters.append("DLC")
    else:
        if "DLC" in settings.filters:
            settings.filters.remove("DLC")

def toggle_show_update():
    if showupdate_chk.get() == 1:
        if "UPDATE" not in settings.filters:
            settings.filters.append("UPDATE")
    else:
        if "UPDATE" in settings.filters:
            settings.filters.remove("UPDATE")

def toggle_show_demo():
    if showdemo_chk.get() == 1:
        if "DEMO" not in settings.filters:
            settings.filters.append("DEMO")
    else:
        if "DEMO" in settings.filters:
            settings.filters.remove("DEMO")

def toggle_show_game():
    if showgame_chk.get() == 1:
        if "GAME" not in settings.filters:
            settings.filters.append("GAME")
    else:
        if "GAME" in settings.filters:
            settings.filters.remove("GAME")

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


#settings_tab stuff here
settings_tab = Frame(note)
settings_tab.rowconfigure(0, weight=1)
settings_tab.rowconfigure(1, weight=1)
settings_tab.rowconfigure(2, weight=1)
settings_tab.rowconfigure(3, weight=1)
settings_tab.rowconfigure(4, weight=1)
settings_tab.rowconfigure(5, weight=1)
settings_tab.rowconfigure(6, weight=1)
settings_tab.rowconfigure(7, weight=1)
settings_tab.rowconfigure(8, weight=1)
settings_tab.rowconfigure(9, weight=1)
settings_tab.rowconfigure(10, weight=1)
settings_tab.rowconfigure(11, weight=1)
settings_tab.rowconfigure(12, weight=1)

url_label = Label(settings_tab, width=20,  text="Title Key Website:")
url_label.grid(row=0, column=0,sticky=W)
url_input = Entry(settings_tab, width=20)
url_input.grid(row=0, column=1, sticky=W)
url_label_cont = Label(settings_tab, text=" (https://xxxx.xxxxxxxxx.com/)")
url_label_cont.grid(row=0, column=3, sticky=W)

downloaddir = Label(settings_tab, text="Download Folder:")
downloaddir.grid(row=1, column=0, sticky=W)
downloaddir_input = Entry(settings_tab, width=20)
downloaddir_input.grid(row=1, column=1, sticky=W)

ticketonly_chk = IntVar()
ticketonly_checkbox = Checkbutton(settings_tab,text = "Legitimate tickets only",command = toggle_ticket_only,variable=ticketonly_chk)
ticketonly_checkbox.grid(row=2, column=0, sticky=W)
if settings.ticketOnly:
    ticketonly_chk.set(1)

patchdemo_chk = IntVar()
patchdemo_checkbox = Checkbutton(settings_tab,text = "Patch demos",command = toggle_patch_demo,variable=patchdemo_chk)
patchdemo_checkbox.grid(row=3, column=0, sticky=W)
if settings.patchDEMO:
    patchdemo_chk.set(1)
    

region_label = Label(settings_tab, text="Region Filters:")
region_label.grid(row=4, column=0 ,sticky=W)

showusa_chk = IntVar()
showusa_checkbox = Checkbutton(settings_tab,text = "USA",command = toggle_show_usa,variable=showusa_chk)
showusa_checkbox.grid(row=5, column=0, sticky=W)
if "USA" in settings.filters:
    showusa_chk.set(1)

showjpn_chk = IntVar()
showjpn_checkbox = Checkbutton(settings_tab,text = "JPN",command = toggle_show_jpn,variable=showjpn_chk)
showjpn_checkbox.grid(row=5, column=1, sticky=W)
if "JPN" in settings.filters:
    showjpn_chk.set(1)

showeur_chk = IntVar()
showeur_checkbox = Checkbutton(settings_tab,text = "EUR",command = toggle_show_eur,variable=showeur_chk)
showeur_checkbox.grid(row=5, column=2, sticky=W)
if "EUR" in settings.filters:
    showeur_chk.set(1)

region_label = Label(settings_tab, text="Type Filters:")
region_label.grid(row=6, column=0 ,sticky=W)

showdlc_chk = IntVar()
showdlc_checkbox = Checkbutton(settings_tab,text = "DLC",command = toggle_show_dlc,variable=showdlc_chk)
showdlc_checkbox.grid(row=7, column=0, sticky=W)
if "DLC" in settings.filters:
    showdlc_chk.set(1)

showupdate_chk = IntVar()
showupdate_checkbox = Checkbutton(settings_tab,text = "Update",command = toggle_show_update,variable=showupdate_chk)
showupdate_checkbox.grid(row=7, column=1, sticky=W)
if "UPDATE" in settings.filters:
    showupdate_chk.set(1)

showdemo_chk = IntVar()
showdemo_checkbox = Checkbutton(settings_tab,text = "Demo",command = toggle_show_demo,variable=showdemo_chk)
showdemo_checkbox.grid(row=7, column=2, sticky=W)
if "DEMO" in settings.filters:
    showdemo_chk.set(1)

showgame_chk = IntVar()
showgame_checkbox = Checkbutton(settings_tab,text = "GAME",command = toggle_show_game,variable=showgame_chk)
showgame_checkbox.grid(row=7, column=4, sticky=W)
if "GAME" in settings.filters:
    showgame_chk.set(1)





save_btn = Button(settings_tab, text="Save", command=save_settings)
save_btn.grid(row=12, column=0, sticky=E)
spacer = Label(settings_tab).grid(row=12, column=0)

#players_tab stuff here
players_tab = Frame(note)
players_tab.columnconfigure(0, weight=1)
players_tab.rowconfigure(0, weight=1)
playerlist = Listbox(players_tab, height=20, width=20)
playerlist.grid(row=0, column=1, sticky=N+S)
infobox = Text(players_tab, height=10, width=80)
infobox.grid(row=0, column=0, sticky=N+E+W)






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
            #gamelist_array.reverse()
    except IOError as e:
        if (settings.titleKeyURL != ""):
            download_titlekeys_json()
        else:
            log("Title key site not set in settings")

def refresh_gamelist():
    searchlist.delete(0, END)
    for game in gamelist_array:
        if game["region"] in filters and decode_titleid(game["titleID"]) in filters:
            searchlist.insert(END, game["name"])

#playerlist.bind('<<ListboxSelect>>', listclick)
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