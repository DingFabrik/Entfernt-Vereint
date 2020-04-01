#!/usr/bin/env python3

"""
Uwe Ziegenhagen, ziegenhagen@gmail.com
Simple tkinter GUI to start a Jitsi Meeting
"""

import tkinter as tk # https://www.delftstack.com/de/howto/python-tkinter/how-to-create-dropdown-menu-in-tkinter/
import webbrowser
import configparser
from urllib.request import urlopen 
from urllib.error import HTTPError, URLError
import os.path


def internet_on():
    """
     Check online status by opening github.com
    """
    try:
        urlopen('https://github.com', timeout=2)
        return True
    except HTTPError as error: 
        print(error)
        return False
    except URLError as error: 
        print(error)
        return False 

def openweb():
    """
       Open default browser
       based on https://gist.github.com/RandomResourceWeb/93e887facdb98937ab5d260d1a0df270
    """
    global url
    url = currentServer.get() + '/' + standort + '-' + currentName.get().replace(' ','').lower()
    print(url)
    webbrowser.open(url,new=1)
    

# some global variables    
url = ""
this_version = 0.1
standort = ''

# read URLs from Einstellungen.conf
Config = configparser.ConfigParser()
Config.read('Einstellungen.conf', encoding='utf-8')

# get list of servers from Einstellungen.conf file
servers = Config.items('Server')
serverList = []
for server in servers:
    serverList.append(server[1])

###################################
# Name handling
###################################
    
# check if name file exists, create one if necessary
# https://linuxize.com/post/python-check-if-file-exists/
if os.path.isfile('namen.txt'):
    print ("Namensdatei existiert")
else:
    print ("Namensdatei existiert nicht, wird angelegt")
    with open('namen.txt', 'wt') as names:
        names.write('[Standort]\nStandort=Theo Burauen\n')
        names.write('[Namen]\n')
        names.write('Name1=Max Frisch\n')
        names.write('Name2=Heinrich Heine\n')        
        names.write('Name3=Theodor Storm\n')        
        names.write('Name4=Vivi Bach\n')        
        names.write('Name5=Senta Berger\n')        
        names.write('Name6=Marlene Dietrich\n')    
    

nameList = [] # empty array for the names
nameConfig = configparser.ConfigParser() # another config parser for the names
nameConfig.read('namen.txt', encoding='utf-8')
standort = nameConfig.get('Standort', 'Standort').replace(' ','').lower()

# fill names list with names from the config file
names = nameConfig.items('Namen')
for name in names:
    nameList.append(name[1])


# check internet connection
onlineCheck = internet_on()
if onlineCheck == True:
    onlineString = 'Mit dem Internet verbunden'
else:
    onlineString = 'Keine Verbindung zum Internet!'

# Check the version
# https://stackoverflow.com/questions/1393324/in-python-given-a-url-to-a-text-file-what-is-the-simplest-way-to-read-the-cont
if internet_on():
    version_online = urlopen('https://raw.githubusercontent.com/UweZiegenhagen/pyJitsiopen/master/latest_version')
    version_online = float(version_online.read())
else:
    version_online = 0


app = tk.Tk() # the tkinter panel
app.title('Dingfabrik.de Jitsi-Zugang ' + str(this_version) + ': ' + onlineString)

# 800x400 should be fine for all laptops
w=800
h=400
ws = app.winfo_screenwidth()
hs = app.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
app.geometry('%dx%d+%d+%d' % (w, h, x, y))


# currentServer and currentName take the values of the dropdowns
currentServer = tk.StringVar(app) 
currentServer.set(serverList[0])

currentName = tk.StringVar(app) 
currentName.set(nameList[0])

serverLabel = tk.Label(master=app, font=('Helvetica', 16), text='Server:')
serverLabel.grid(row=0, column=0, padx='5', pady='5', sticky='e')

serverDropdown = tk.OptionMenu(app, currentServer, *serverList) # dropdown for the server
serverDropdown.config( font=('Helvetica', 16))
serverDropdown.grid(row=0,column=1,sticky='w')

nameLabel = tk.Label(master=app, font=('Helvetica', 16), text='Name:')
nameLabel.grid(row=2, column=0, sticky='e',padx='5', pady='5')

nameDropdown = tk.OptionMenu(app, currentName, *nameList) # dropdown for the names
nameDropdown.config( font=('Helvetica', 16))
nameDropdown.grid(row=2,column=1, sticky='w')

# with currentServer and currentName we can build the url
url = currentServer.get() + '/' + currentName.get().replace(' ','')

#if version_online > this_version:
#    urlText.insert(tk.END,'Eine neue Version ist online verfügbar')
#    # TODO: https://www.freecodecamp.org/forum/t/git-pull-how-to-override-local-files-with-git-pull/13216
#else:
#        urlText.insert(tk.END,'Diese Version ist aktuell!')

urlLabel = tk.Label(master=app, font=('Helvetica', 16), text='URL:')
urlLabel.grid(row=3, column=0, padx='5', pady='5', sticky='e')

# a label for the server url
greenUrl = tk.Label(text="", font=('Helvetica', 16), fg='green')
greenUrl.grid(row=3,column=1, sticky='w')
greenUrl.bind("<Button-1>", lambda e: openweb())


# the button to initiate the Jitsi session
# https://www.delftstack.com/de/howto/python-tkinter/how-to-create-a-new-window-with-a-button-in-tkinter/
buttonBrowser = tk.Button(app, text="Starte Jitsi",font=('Helvetica', '20'), command=openweb) 
buttonBrowser.grid(row=4,column=1, sticky='w', padx='5', pady='5')

#buttonUpdate = tk.Button(app, text="Aktualisieren",command=update, state=tk.DISABLED, font=('Helvetica', '20')) # https://www.delftstack.com/de/howto/python-tkinter/how-to-create-a-new-window-with-a-button-in-tkinter/

# https://www.delftstack.com/de/howto/python-tkinter/how-to-make-tkinter-text-widget-read-only/
helpText = tk.Text(app, font=('Helvetica', 20)) 
helpText.delete(1.0, tk.END)
helpText.insert(tk.END,'1. Server im obersten Menü auswählen\n')
helpText.insert(tk.END,'2. Darunter den Namen der Konferenz auswählen\n')
helpText.insert(tk.END,'3. Grünen Link an Gesprächspartner geben\n')
helpText.insert(tk.END,'4. "Starte Jitsi" drücken')

if not internet_on():
    helpText.insert(tk.END, '\n\n!!!Keine Verbindung zum Internet!!!')

helpText.grid(row=8,column=1, sticky='e', padx='5', pady='5') # columnspan=2
helpText.configure(state='disabled') # read-only

#infoText = tk.Text(app, font=('Helvetica', 20), fg='red') 
#infoText.delete(1.0, tk.END)
#infoText.grid(row=9,column=1, sticky='e', padx='5', pady='5') # columnspan=2
#infoText.configure(state='disabled') # read-only



def callback(*args):
    global url
    url = currentServer.get() + '/' + standort + '-' + currentName.get().replace(' ','').lower()
    print(url)
    greenUrl.configure(text=url[8::])

# call the callback() function if server or name dropdown is used.
currentName.trace("w", callback)
currentServer.trace("w", callback)

app.mainloop()