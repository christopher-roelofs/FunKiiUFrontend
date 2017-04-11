#!/usr/bin/python

from Tkinter import *
from ttk import *

import threading
import time

from logger import *
import settings
import util



def toggle_verbose():
    pass

def toggle_debug():
    pass

def toggle_server():
    pass

def save_settings():
    pass

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
searchlist.grid(row=0, column=0, sticky=NSEW, columnspan=2)
searchlist.columnconfigure(0, weight=1)
searchlist.rowconfigure(0, weight=1)
playerbox = Listbox(search_tab, height=20, width=20)
playerbox.grid(row=0, column=3, sticky=N+S)

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
settings_tab.rowconfigure(3, weight=1)
settings_tab.rowconfigure(4, weight=1)
settings_tab.rowconfigure(5, weight=1)
settings_tab.rowconfigure(6, weight=1)

verbose_chk = IntVar()
verbose_checkbox = Checkbutton(settings_tab,text = "Verbose Logging",command = toggle_verbose,variable=verbose_chk)
verbose_checkbox.grid(row=0, column=0, sticky=W)


debug_chk = IntVar()
debug_checkbox = Checkbutton(settings_tab,text = "Debug Logging",command = toggle_debug,variable=debug_chk)
debug_checkbox.grid(row=1, column=0, sticky=W)


server_chk = IntVar()
server_checkbox = Checkbutton(settings_tab,text = "Server",command = toggle_server,variable=server_chk)
server_checkbox.grid(row=2, column=0, sticky=W)


motd_label = Label(settings_tab, width=10, text="MOTD: ")
motd_label.grid(row=3, column=0)
motd_input = Entry(settings_tab, width=30)
motd_input.grid(row=3, column=1, sticky=W)


host_label = Label(settings_tab, width=10, text="Host: ")
host_label.grid(row=4, column=0)
host_input = Entry(settings_tab, width=15)
host_input.grid(row=4, column=1, sticky=W)


port_label = Label(settings_tab, width=10, text="Port: ")
port_label.grid(row=5, column=0)
port_input = Entry(settings_tab, width=15)
port_input.grid(row=5, column=1, sticky=W)


claim_label = Label(settings_tab, width=10, text="Claim Radius: ")
claim_label.grid(row=6, column=0)
claim_input = Entry(settings_tab, width=15)
claim_input.grid(row=6, column=1, sticky=W)






save_btn = Button(settings_tab,text = "Save",command = save_settings)
save_btn.grid(row=7, column=0, sticky=E)
spacer = Label(settings_tab).grid(row=8,column=0)

#system_tab stuff here
system_tab = Frame(note)

time_var = StringVar()
time_var.set("Time: 0m")
time_label = Label(system_tab,width=15,textvariable=time_var)
time_label.grid(row=0, column=0)

def show_player_info(name):
    infobox.delete("1.0", END)
    player = memorydb.get_player_from_name(name)
    infobox.insert(END, "Name:"+ player.name+ "\n")
    infobox.insert(END, "SteamID:"+ str(player.steamid)+ "\n")
    infobox.insert(END, "IP:"+ player.ip+ "\n")
    infobox.insert(END, "Last Location:"+ player.location+ "\n")

def addInfo(info):
    textbox.insert(END, info + '\n')
    textbox.see(END)

def refreshPlayerList():
    if int(playerbox.index('end-1c').split(".")[0])-1 != len(memorydb.online_players):
        playerbox.delete("1.0", END)
        online_players = memorydb.get_online_players()
        for player in online_players:
            playerbox.insert("1.0", player + "\n")

def refreshInfoList():
    if int(playerlist.index('end')) != len(memorydb.player_array):
        playerlist.delete(0, END)
        for player in memorydb.player_array:
            playerlist.insert(1, player.name)

def func(event):
    cmd = input.get()
    telconn.write_out(cmd)
    logger.log("Command sent: " + cmd)
    input.delete(0, END)

def listclick(e):
    show_player_info(str(playerlist.get(playerlist.curselection())))

def set_motd(e):
    runtime.motd = motd_input.get()

def handler():
    root.destroy()

playerlist.bind('<<ListboxSelect>>', listclick)
note.add(players_tab, text = "Search")

motd_input.bind('<KeyRelease>',set_motd)

note.add(settings_tab, text = "Settings")

note.add(system_tab, text = "Info")

root.protocol("WM_DELETE_WINDOW", handler)




try:
    root.mainloop()
except (KeyboardInterrupt, SystemExit):
    sys.exit()