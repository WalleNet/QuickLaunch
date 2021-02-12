import webbrowser
import os
from config import *
from tkinter import *
import subprocess

f = open("QL-savedata.txt","w")

def call(event=""): # Decide what to do with current typed text
    data = e.get().lower();
    word_list = data.split()
    destroy = True

    # Show All Programs (Only works with Shell)
    if ('showall' in data):
        programlist = []
        programitems = list(programs.items())

        # Get all extras and programs and append them to the programlist
        for i in range(len(extras)):
            programlist.append(extras[i])
        for i in range(len(programitems)):
            programlist.append(programitems[i][0])
        print(programlist)

    # Settings (Must be before calculation)
    elif ("settings" in data):
        page = word_list[0]
        os.system("start ms-settings:"+page)

    elif ("explorer" in data):
        page = word_list[0]
        os.system("explorer")

    # Calculations
    elif ("+" in data or "-" in data or "/" in data or "*" in data):
        try:
            data = data.replace(" ","")
            data = data.replace("+"," + ")
            data = data.replace("-"," - ")
            data = data.replace("*"," * ")
            data = data.replace("/"," / ")
            word_list = data.split()
            answer = calculate(data)
            print(str(answer))
            destroy = False
            e.delete(0,END)
            e.insert(0,str(answer))
            e.selection_range(0,END)
        except Exception as j:
            print("calculation failed:\n"+str(j))

    # Open Website
    elif ('.com' in data or '.org' in data or '.net' in data or '.io' in data):
        if ('.com' in data):
            dtype = ".com"
        elif ('.org' in data):
            dtype = ".org"
        elif ('.net' in data):
            dtype = '.net'
        elif ('.io' in data):
            dtype = '.io'
        res = list(filter(lambda x: dtype in x, word_list))
        res = " ".join(res)
        url = res
        print("Opening "+res+" in browser...")
        webbrowser.get(BROWSER_PATH).open(url)

    # Google Search
    elif (word_list[0] == "g"):
        search = data[2:]
        search = search.replace(" ","+")
        webbrowser.get(BROWSER_PATH).open("https://google.com/search?q="+search)

    # YouTube Search
    elif (word_list[0] == "yt"):
        search = data[2:]
        search = search.replace(" ","+")
        webbrowser.get(BROWSER_PATH).open("https://youtube.com/search?q="+search)

    # Shutdown Options
    elif (word_list[0] == "shutdown"):
        subprocess.call("shutdown /s")
    elif (word_list[0] == "lock"):
        subprocess.call("rundll32.exe user32.dll,LockWorkStation")
    elif (word_list[0] == "restart"):
        subprocess.call("shutdown /r")
    elif (word_list[0] == "logoff"):
        subprocess.call("shutdown /l")

    # Quit
    elif (word_list[0] == "exit"): 
        destroy = True

    # Open Program
    else:
        word_list = data.split()
        program_name = word_list[0].lower()
        if (program_name in programs):
            file = programs[program_name]
            print('Opening '+word_list[0])
            os.startfile(file)
        else:
            print("No program or website found called '"+str(data)+"'")
            destroy = False
            
    # Close Program if not a calculation, etc.
    if (destroy):
        f = open("QL-savedata.txt","w")
        if (e.get() != "exit"):
            f.write(str(e.get()))
        else:
            f.write("QuickLaunch")
        f.close()
        root.destroy()



def calculate(data): # Handles calculations
    word_list = data.split()
    if("+" in data):
        numOne = float(word_list[0])
        numTwo = float(word_list[2])
        answer = numOne + numTwo
    elif("-" in data):
        numOne = float(word_list[0])
        numTwo = float(word_list[2])
        answer = numOne - numTwo
    elif("*" in data):
        numOne = float(word_list[0])
        numTwo = float(word_list[2])
        answer = numOne * numTwo
    elif("/" in data):
        numOne = float(word_list[0])
        numTwo = float(word_list[2])
        answer = numOne / numTwo
    return(answer)



def autofill(event=""): # Autofill to any programs or extras when any key is pressed
    currenttext = e.get()
    currentlength = len(currenttext)
    programlist = []
    programitems = list(programs.items())
    matching = []
    # Get all extras and programs and append them to the programlist
    for i in range(len(extras)):
        programlist.append(extras[i])
    for i in range(len(programitems)):
        programlist.append(programitems[i][0])

    # Shorten all values of programlist to length of the current typed text
    programlistshortened = []
    for i in range(len(programlist)):
        programshortened = programlist[i][:currentlength]
        programlistshortened.append(programshortened)
    
    # If a shortened value matches what is typed, add it to 'matching' list
    if currentlength != 0:
        for i in range(len(programlistshortened)):
            if currenttext == programlistshortened[i]:
                matching.append(programlist[i])
    
    p = min(matching,key=len)
    e.insert(currentlength,p[currentlength:])
    e.select_range(currentlength,END)



"""

------------------------------------- Main Program Starts Here -------------------------------------

"""



# Setup window
root = Tk()
root.title("QuickLaunch")
root.iconphoto(False, PhotoImage(file = 'C:\\Users\\rohan\\OneDrive\\Desktop\\RohanDhar\\photos\\WN_logo\\wn-clear.png'))
root.overrideredirect(1)

# Create entry and fill with any saved text
e = Entry(root,width=40,font="Bahnschrift 24",bg="#303030",fg="#ffffff")
e.pack()
try:
    s = open("QL-savedata.txt","r")
    savedtext = s.read()
except:
    savedtext = "QuickLaunch"
e.insert(0,savedtext)
e.focus_set()
e.bind("<FocusIn>", e.selection_range(0,END))

# Call the 'call' function when <Return> is pressed
root.bind('<Return>',call)

# Call the 'autofill' function when any key in 'keys' is pressed
keys="abcdefghijklmnopqrstuvwxyz-"
keys = list(keys)
for key in keys:
    root.bind(key,autofill)

# Run Tk
root.mainloop()