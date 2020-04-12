import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess
from PIL import ImageTk, Image

root = tk.Tk()
root.title('Multi-App Opener 3000')
root.configure(background='white')
apps = []
clearAll_ran = 0

from pics import *

# Funtion for Add App button Action
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    #Gets filename and adds it to apps list as directory, for opening later.
    filename = filedialog.askopenfilename(initialdir="/Applications", title="Select File")
    filetypes=(("executables","*.app"), ("all files", "*.*"))
    apps.append(filename)

    # For app in apps: Check name and assign it a picture: Otherwise assign it a name
    for app in apps:

        #Keeps track of items in list(apps) it there are duplicates, remove what you just asked to select
        counts = apps.count(app)
        items = []
        items.append(counts)
        for num in items:
            if num >=2:
                apps.pop()

        #If the app you selected matches the file location - Add the picture and pack to screen
        if app == '/Applications/Discord.app':
            label = tk.Label(frame, image=disc)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Google Chrome.app':
            label = tk.Label(frame, image=chrome)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Old School RuneScape.app':
            label = tk.Label(frame, image=rs)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/League of Legends.app':
            label = tk.Label(frame, image=lol)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Minecraft.app':
            label = tk.Label(frame, image=minecraft)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app== '/Applications/Adobe Photoshop 2020/Adobe Photoshop 2020.app':
            label = tk.Label(frame, image=photoshop)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Mail.app':
            label = tk.Label(frame, image=mail)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Notes.app':
            label = tk.Label(frame, image=notepad)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Spotify.app':
            label = tk.Label(frame, image=spotify)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Final Cut Pro.app':
            label = tk.Label(frame, image=finalcut)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Photos.app':
            label = tk.Label(frame, image=photo)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Xcode.app':
            label = tk.Label(frame, image=xcode)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/PyCharm CE.app':
            label = tk.Label(frame, image=pycharm)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Zoom.us.app':
            label = tk.Label(frame, image=zoom)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Visual Studio Code 2.app':
            label = tk.Label(frame, image=vscode2)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Safari.app':
            label = tk.Label(frame, image=safari)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Sublime Text.app':
            label = tk.Label(frame, image=subtxt)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/iTunes.app':
            label = tk.Label(frame, image=itunes)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/News.app':
            label = tk.Label(frame, image=news)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Messages.app':
            label = tk.Label(frame, image=messages)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Automator.app':
            label = tk.Label(frame, image=automator)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Books.app':
            label = tk.Label(frame, image=books)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Calculator.app':
            label = tk.Label(frame, image=calculator)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Calendar.app':
            label = tk.Label(frame, image=calendar)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Chess.app':
            label = tk.Label(frame, image=chess)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Contacts.app':
            label = tk.Label(frame, image=contacts)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Dashboard.app':
            label = tk.Label(frame, image=dashboard)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Dictionary.app':
            label = tk.Label(frame, image=dictionary)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/FaceTime.app':
            label = tk.Label(frame, image=facetime)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Home.app':
            label = tk.Label(frame, image=home)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Keynote.app':
            label = tk.Label(frame, image=keynote)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Launchpad.app':
            label = tk.Label(frame, image=launchpad)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Siri.app':
            label = tk.Label(frame, image=siri)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()
        elif app == '/Applications/Steam.app':
            label = tk.Label(frame, image=steam)
            label.configure(borderwidth=0, bg='#276157')
            label.pack()

        #If no picture available - Assign it a name instead.... Looks ugly, but it's better than adding 100000 pictures
        else:
            label = tk.Label(frame, text=apps[-1], bg='#276157')
            label.pack()
        
        #Counts the numeber of apps selected, if more than 4, pop the list at -1
        count = 0
        for app in apps:
            count+=1
        if count >=5:
            apps.pop(-1)

        #If cancel is hit, it makes an empty string at the end of the list. If null: pop the list...
        for widget in frame.winfo_children():
            if apps[-1] == '':
                apps.pop()  

# Multi-platform run option (If win32 us os.startfile. For MacOS, Linux, Etc use second forloop)
def runApps():
    if sys.platform == "win32":
        for app in apps:
            os.startfile(apps)
    else:
        for app in apps:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, app])


# Clears the list and calls if function below
def clearAll():
    global clearAll_ran
    clearAll_ran +=1
    for widget in frame.winfo_children():
        widget.destroy()
    apps.clear()
    
# Background of box (Outside Frame)
canvas = tk.Canvas(root, height=600, width=400, bg='#1F4D45',)
canvas.pack()

# Inside Box where apps get added to (Inside Frame)
frame = tk.Frame(root, bg='#276157')
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

label3 = tk.Label(frame, text='Select up tp 4 Apps to run!\nAll Apps will be saved', bg='#276157',font = '-weight bold', fg='#DADBDB')
label3.pack()

# Open File Button Design and call to command
openFile = tk.Button(root, text="Open Files", padx=10, pady=5, bg='#263D42',fg='black',command=addApp)
openFile.pack()

# Button Configs for Running the apps
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5,bg='#263D42', fg='black', command=runApps)
runApps.pack()

# Button Configs for Open
clearAll = tk.Button(root, text="Clear Selections", padx=10, pady=5, bg='#263D42',fg='black',command=clearAll)
clearAll.pack()

# When program is open (if any data is saved from last session - Open the previous session)
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
    
    for app in apps:
        if app == '/Applications/Discord.app':
            label = tk.Label(frame, image=disc)
            label.pack()
        elif app == '/Applications/Google Chrome.app':
            label = tk.Label(frame, image=chrome)
            label.pack()
        elif app == '/Applications/Old School RuneScape.app':
            label = tk.Label(frame, image=rs)
            label.pack()
        elif app == '/Applications/League of Legends.app':
            label = tk.Label(frame, image=lol)
            label.pack()
        elif app == '/Applications/Minecraft.app':
            label = tk.Label(frame, image=minecraft)
            label.pack()
        elif app== '/Applications/Adobe Photoshop 2020/Adobe Photoshop 2020.app':
            label = tk.Label(frame, image=photoshop)
            label.pack()
        elif app == '/Applications/Mail.app':
            label = tk.Label(frame, image=mail)
            label.pack()
        elif app == '/Applications/Notes.app':
            label = tk.Label(frame, image=notepad)
            label.pack()
        elif app == '/Applications/Spotify.app':
            label = tk.Label(frame, image=spotify)
            label.pack()
        elif app == '/Applications/Final Cut Pro.app':
            label = tk.Label(frame, image=finalcut)
            label.pack()
        elif app == '/Applications/Photos.app':
            label = tk.Label(frame, image=photo)
            label.pack()
        elif app == '/Applications/Xcode.app':
            label = tk.Label(frame, image=xcode)
            label.pack()
        elif app == '/Applications/PyCharm CE.app':
            label = tk.Label(frame, image=pycharm)
            label.pack()
        elif app == '/Applications/zoom.us.app':
            label = tk.Label(frame, image=zoom)
            label.pack()
        elif app == '/Applications/Visual Studio Code 2.app':
            label = tk.Label(frame, image=vscode2)
            label.pack()
        elif app == '/Applications/Safari.app':
            label = tk.Label(frame, image=safari)
            label.pack()
        elif app == '/Applications/Sublime Text.app':
            label = tk.Label(frame, image=subtxt)
            label.pack()
        elif app == '/Applications/iTunes.app':
            label = tk.Label(frame, image=itunes)
            label.pack()
        elif app == '/Applications/News.app':
            label = tk.Label(frame, image=news)
            label.pack()
        elif app == '/Applications/Messages.app':
            label = tk.Label(frame, image=messages)
            label.pack()
        elif app == '/Applications/Automator.app':
            label = tk.Label(frame, image=automator)
            label.pack()
        elif app == '/Applications/Books.app':
            label = tk.Label(frame, image=books)
            label.pack()
        elif app == '/Applications/Calculator.app':
            label = tk.Label(frame, image=calculator)
            label.pack()
        elif app == '/Applications/Calendar.app':
            label = tk.Label(frame, image=calendar)
            label.pack()
        elif app == '/Applications/Chess.app':
            label = tk.Label(frame, image=chess)
            label.pack()
        elif app == '/Applications/Contacts.app':
            label = tk.Label(frame, image=contacts)
            label.pack()
        elif app == '/Applications/Dashboard.app':
            label = tk.Label(frame, image=dashboard)
            label.pack()
        elif app == '/Applications/Dictionary.app':
            label = tk.Label(frame, image=dictionary)
            label.pack()
        elif app == '/Applications/FaceTime.app':
            label = tk.Label(frame, image=facetime)
            label.pack()
        elif app == '/Applications/Home.app':
            label = tk.Label(frame, image=home)
            label.pack()
        elif app == '/Applications/Keynote.app':
            label = tk.Label(frame, image=keynote)
            label.pack()
        elif app == '/Applications/Launchpad.app':
            label = tk.Label(frame, image=launchpad)
            label.pack()
        elif app == '/Applications/Siri.app':
            label = tk.Label(frame, image=siri)
            label.pack()
        elif app == '/Applications/Steam.app':
            label = tk.Label(frame, image=steam)
            label.pack()

        #If no picture available - Assign it a name instead.... Looks ugly, but it's better than adding 100000 pictures
        else:
            for app in apps:
                label = tk.Label(frame, text=app, bg='white')
                label.pack()


root.mainloop()

# When closed, save apps to .txt file
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
