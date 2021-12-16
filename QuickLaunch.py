import webbrowser
import os
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as tkmsg
import subprocess
import easygui
import pickle



# Constants
BACKGROUND_MAIN = "#303030"
BACKGROUND_ALT = "#292929"
BACKGROUND_2ALT = "#252525"
DEBUG_MODE = True
VERSION = "6.1.1"
VERSION_INFO = "QuickLaunch (v"+VERSION+") by WalleNet"



# Global variables
in_settings = False
show_hints = True
show_alt_bar = True
root_width = 600
root_height = 200
settings_selected_file = ""
browser_path = ""
programs = {
}
extras = ['explorer','shutdown','restart','logoff','lock','exit']
settings = [
    'settings',
    'about settings',
    'activation settings',
    'appsfeatures settings',
    'appsforwebsites settings',
    'apps-volume settings',
    'autoplay settings',
    'backup settings',
    'recovery settings',
    'batterysaver settings',
    'batterysaver-settings settings',
    'batterysaver-usagedetails settings',
    'bluetooth settings',
    'crossdevice settings',
    'defaultapps settings',
    'developers settings',
    'display settings',
    'screenrotation settings',
    'storagesense settings',
    'maps settings',
    'connecteddevices settings',
    'devices-touchpad settings',
    'mousetouchpad settings',
    'typing settings',
    'findmydevice settings',
    'usb settings',
    'network-airplanemode settings',
    'network-cellular settings',
    'network-directaccess settings',
    'network-dialup settings',
    'network-ethernet settings',
    'network-proxy settings',
    'network-status settings',
    'network-vpn settings',
    'network-wifi settings',
    'network-wifisettings settings',
    'sync settings',
    'datausage settings',
    'network-mobilehotspot settings',
    'lockscreen settings',
    'powersleep settings',
    'multitasking settings',
    'optionalfeatures settings',
    'personalization settings',
    'personalization-background settings',
    'personalization-colors settings',
    'colors settings',
    'personalization-start settings',
    'taskbar settings',
    'themes settings',
    'printers settings',
    'proximity settings',
    'emailandaccounts settings',
    'otherusers settings',
    'workplace settings',
    'dateandtime settings',
    'regionlanguage settings',
    'signinoptions settings',
    'speech settings',
    'privacy settings',
    'privacy-accountinfo settings',
    'privacy-backgroundapps settings',
    'privacy-appdiagnostics settings',
    'privacy-callhistory settings',
    'privacy-calendar settings',
    'privacy-contacts settings',
    'privacy-email settings',
    'privacy-feedback settings',
    'privacy-location settings',
    'privacy-messaging settings',
    'privacy-microphone settings',
    'privacy-motion settings',
    'notifications settings',
    'privacy-notifications settings',
    'privacy-customdevices settings',
    'privacy-radios settings',
    'privacy-speechtyping settings',
    'privacy-tasks settings',
    'privacy-webcam settings',
    'yourinfo settings',
    'easeofaccess-closedcaptioning settings',
    'easeofaccess-highcontrast settings',
    'easeofaccess-keyboard settings',
    'easeofaccess-magnifier settings',
    'easeofaccess-mouse settings',
    'easeofaccess-narrator settings',
    'easeofaccess-otheroptions settings',
    'project settings',
    'tabletmode settings',
    'windowsdefender settings',
    'windowsinsider settings',
    'troubleshoot settings',
    'windowsupdate settings',
    'windowsupdate-action settings',
    'windowsupdate-history settings',
    'windowsupdate-options settings',
    'windowsupdate-restartoptions settings'
]
# Fill all settings into the 'extras' list
for i in range(len(settings)):
    extras.append(settings[i])



def call(event=""): # Decide what to do with current typed text (make sure to also update alt_call)
    if (not in_settings):
        data = e.get().lower()
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
            debug(programlist)

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
                destroy = False
                e.delete(0,END)
                e.insert(0,str(answer))
                e.selection_range(0,END)
            except Exception as j:
                debug("calculation failed:\n"+str(j))

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
            debug("Opening "+res+" in browser...")
            webbrowser.get(browser_path).open(url)

        # Google Search
        elif (word_list[0] == "g"):
            search = data[2:]
            search = search.replace(" ","+")
            webbrowser.get(browser_path).open("https://google.com/search?q="+search)

        # YouTube Search
        elif (word_list[0] == "yt"):
            search = data[2:]
            search = search.replace(" ","+")
            webbrowser.get(browser_path).open("https://youtube.com/search?q="+search)

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
                debug('Opening '+word_list[0])
                os.startfile(file)
            else:
                debug("No program or website found called '"+str(data)+"'")
                destroy = False
                
        # Close Program if not a calculation, etc.
        if (destroy):
            s = open("QL-savedata-launchRecent.txt","r")
            savedtext = s.read()
            s.close()
            f = open("QL-savedata-launchRecent.txt","w")
            if (e.get() != "exit"):
                f.write(str(e.get()))
            else:
                f.write(savedtext)
            f.close()
            root.destroy()



def alt_call(event=""): # Decide what to do with current typed text in ALT
    if (not in_settings):
        data = altProgram.cget("text")
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
            debug(programlist)

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
                debug(str(answer))
                destroy = False
                e.delete(0,END)
                e.insert(0,str(answer))
                e.selection_range(0,END)
            except Exception as j:
                debug("calculation failed:\n"+str(j))

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
            debug("Opening "+res+" in browser...")
            webbrowser.get(browser_path).open(url)

        # Google Search
        elif (word_list[0] == "g"):
            search = data[2:]
            search = search.replace(" ","+")
            webbrowser.get(browser_path).open("https://google.com/search?q="+search)

        # YouTube Search
        elif (word_list[0] == "yt"):
            search = data[2:]
            search = search.replace(" ","+")
            webbrowser.get(browser_path).open("https://youtube.com/search?q="+search)

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
                debug('Opening '+word_list[0])
                os.startfile(file)
            else:
                debug("No program or website found called '"+str(data)+"'")
                destroy = False
                
        # Close Program if not a calculation, etc.
        if (destroy):
            s = open("QL-savedata-launchRecent.txt","r")
            savedtext = s.read()
            s.close()
            f = open("QL-savedata-launchRecent.txt","w")
            if (altProgram.cget("text") != "exit"):
                f.write(str(altProgram.cget("text")))
            else:
                f.write(savedtext)
            f.close()
            root.destroy()

def last_call(event=""): # Open last program
    if (not in_settings):
        e.delete(0,END)
        e.insert(0,lastCommand.lower())
        call()


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
    if (not in_settings):
        currenttext = e.get()
        if (currenttext != currenttext.lower()):
            currenttext = currenttext.lower()
            e.delete(0,END)
            e.insert(0,currenttext)
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
                    indexStop = i

        matchingLengthOrder = sorted(matching, key=len)
        try:
            p = matchingLengthOrder[0]
        except:
            altProgram.configure(text="")
        try:
            e.insert(currentlength,p[currentlength:])
        except UnboundLocalError:
            debug("no autofill options found, allowing user continue to type...")
        e.select_range(currentlength,END)
        if (len(matchingLengthOrder) > 1):
            p = matchingLengthOrder[1]
            altProgram.configure(text=p)
        else:
            altProgram.configure(text="")
            debug("no programs with exact match. looking for other loosely related programs...")
            programlistsorted = sorted(programlist,key=len)
            programlistsorted.reverse()
            for program in programlistsorted:
                debug(program)
                if (currenttext in program):
                    try:
                        if (program != p):
                            altProgram.configure(text=program)
                    except UnboundLocalError as err:
                        altProgram.configure(text=program)


def open_settings(event=""): # opens the settings frame
    global in_settings
    global show_hints
    debug("open settings")
    in_settings = True
    e.configure(state="disabled")
    # Frame
    settingsFrame = Frame(root,width=600,height=200,bg=BACKGROUND_MAIN,bd=7)
    settingsFrame.place(anchor="center",relx=0.5,rely=0.5)
    # Version Label
    versionLabel = Label(settingsFrame,text=VERSION_INFO,font="Bahnschrift 8",bg=BACKGROUND_MAIN,fg="white")
    versionLabel.place(anchor="ne",relx=0.95,rely=0)
    # Help Button
    helpButton = Button(settingsFrame,text="?",font="Bahnschrift 8 bold",width=2,bg=BACKGROUND_2ALT,activebackground="#202020",fg="#ffffff",activeforeground="#ffffff",bd=1,command=open_help)
    helpButton.place(relx=1,rely=0,anchor="ne")
    # New Program Label
    newProgramHeaderLabel = Label(settingsFrame,text="Add an Application",font="Bahnschrift 13 bold",bg=BACKGROUND_MAIN,fg="white")
    newProgramHeaderLabel.place(anchor="nw",relx=0,rely=0)
    # New Program Name
    newProgramNameLabel = Label(settingsFrame,text="QuickLaunch Name",font="Bahnschrift 12",bg=BACKGROUND_MAIN,fg="white")
    newProgramNameLabel.place(anchor="nw",relx=0,rely=0.12)
    newProgramNameEntry = Entry(settingsFrame,width=30,font="Bahnschrift 12",bg=BACKGROUND_ALT,fg="#ffffff",bd="2",relief=FLAT)
    newProgramNameEntry.place(anchor="nw",relx=0,rely=0.27)
    # 'Choose File' Button
    pickFileButton = Button(settingsFrame,text="Choose File...",font="Bahnschrift 10",width=12,bg=BACKGROUND_2ALT,activebackground="#202020",fg="#ffffff",activeforeground="#ffffff",bd=1,command=lambda: select_exe_explorer(selectedFileLabel))
    pickFileButton.place(relx=0.5,rely=0.27,anchor="nw")
    selectedFileLabel = Label(settingsFrame,text="[No file selected]",font="Bahnschrift 12",bg=BACKGROUND_MAIN,fg="white")
    selectedFileLabel.place(anchor="nw",relx=0.67,rely=0.27)
    # 'Add App' button
    addAppButton = Button(settingsFrame,text="Add App",font="Bahnschrift 10",width=10,bg=BACKGROUND_2ALT,activebackground="#202020",fg="#ffffff",activeforeground="#ffffff",bd=1,command=lambda: add_app(newProgramNameEntry.get(),selectedFileLabel,newProgramNameEntry))
    addAppButton.place(anchor="nw",relx=0,rely=0.45)
    # 'Remove App' button
    removeAppButton = Button(settingsFrame,text="Remove App...",font="Bahnschrift 10",width=12,bg=BACKGROUND_2ALT,activebackground="#202020",fg="#ffffff",activeforeground="#ffffff",bd=1,command=lambda: remove_app(newProgramNameEntry.get(),selectedFileLabel))
    removeAppButton.place(anchor="nw",relx=0.15,rely=0.45)
    # Toggle Hints button
    hintsLabel = Label(settingsFrame,text="Hints",font="Bahnschrift 13 bold",bg=BACKGROUND_MAIN,fg="white")
    hintsLabel.place(anchor="nw",relx=0,rely=0.7)
    hintsButton = Button(settingsFrame,text="Hide Hints",font="Bahnschrift 10",width=10,bg=BACKGROUND_2ALT,activebackground="#202020",fg="#ffffff",activeforeground="#ffffff",bd=1,command=lambda: toggle_hints(hintsButton))
    if (not show_hints):
        hintsButton.configure(text="Show Hints")
    hintsButton.place(anchor="nw",relx=0.005,rely=0.85)
    # Delete Save Button
    deleteSaveHeaderLabel = Label(settingsFrame,text="Erase Data",font="Bahnschrift 13 bold",bg=BACKGROUND_MAIN,fg="white")
    deleteSaveHeaderLabel.place(anchor="nw",relx=0.18,rely=0.7)
    deleteSaveButton = Button(settingsFrame,text="Delete Save...",font="Bahnschrift 10",width=12,bg=BACKGROUND_2ALT,activebackground="#202020",fg="#ffffff",activeforeground="#ffffff",bd=1,command=delete_save)
    deleteSaveButton.place(anchor="nw",relx=0.185,rely=0.85)
    # Select Browser button
    browserHeaderLabel = Label(settingsFrame,text="Select Browser",font="Bahnschrift 13 bold",bg=BACKGROUND_MAIN,fg="white")
    browserHeaderLabel.place(anchor="nw",relx=0.39,rely=0.7)
    selectedBrowserLabel = Label(settingsFrame,text="[No browser selected]",font="Bahnschrift 12",bg=BACKGROUND_MAIN,fg="white")
    if (browser_path):
        selectedBrowserLabel.configure(text="Selected: "+browser_path.split("/")[-1].replace(".exe","").upper().replace(" %S",""))
    selectedBrowserLabel.place(anchor="nw",relx=0.56,rely=0.85)
    selectBrowserButton = Button(settingsFrame,text="Choose File...",font="Bahnschrift 10",width=12,bg=BACKGROUND_2ALT,activebackground="#202020",fg="#ffffff",activeforeground="#ffffff",bd=1,command=lambda: select_browser_explorer(selectedBrowserLabel))
    selectBrowserButton.place(anchor="nw",relx=0.395,rely=0.85)
    # Close settings button
    closeSettingsButton = Button(settingsFrame,text="\u2715",font="Bahnschrift 18 bold",width=4,bg=BACKGROUND_ALT,activebackground="#202020",fg="#ffffff",activeforeground="#ffffff",bd=0,command=lambda: close_settings(settingsFrame))
    closeSettingsButton.place(anchor="se",relx=1,rely=1)

def close_settings(settingsFrame):
    global in_settings
    global settings_selected_file
    in_settings = False
    debug("close settings")
    e.configure(state="normal")
    e.focus_set()
    settingsFrame.destroy()

def select_exe_explorer(selectedFileLabel):
    global settings_selected_file
    file = easygui.fileopenbox(msg='Select a program to add to QuickLaunch', title='Select File', default='C:\\Program Files\\*.exe', filetypes='*.exe')
    try:
        clean_filename = file.split("\\")[-1]
        selectedFileLabel.configure(text=clean_filename)
        settings_selected_file = file
        debug("selected file: "+file)
    except AttributeError:
        debug("no file selected. continuing...")
    finally:
        root.lift()

def select_browser_explorer(selectedBrowserLabel):
    global browser_path
    file = easygui.fileopenbox(msg='Select a default browser', title='Select File', default='C:\\Program Files\\*.exe', filetypes='*.exe').replace("\\","/")+" %s"
    try:
        clean_filename = file.split("/")[-1].replace(".exe","").upper().replace(" %S","")
        selectedBrowserLabel.configure(text="Selected: "+clean_filename)
        browser_path = file
        debug("selected browser: "+file)
        save("QL-savedata-browser.pickle",file)
    except AttributeError:
        debug("no browser selected. continuing...")
    finally:
        root.lift()

def add_app(name,file_label,file_entry):
    global settings_selected_file
    global programs
    name = name.lower().strip()
    if (len(name) == 0 or len(settings_selected_file) == 0):
        debug("missing name or file. no bindings updated.")
        tkmsg.showwarning(title=" Notice",message="Missing name or file. No bindings have been updated.")
        return None
    # Config file entry and name to blank here
    file_entry.delete(0,END)
    debug("new binding:\n"+name+" -> "+settings_selected_file)
    if (not name in programs and not name in extras):
        programs[name] = settings_selected_file
        debug("new binding:\n"+name+" -> "+settings_selected_file)
        debug("updated 'programs' dict:")
        debug(programs)
        file_label.configure(text="[No file selected]")
        settings_selected_file = ""
    elif (name in programs):
        debug("binding already exists in programs!")
        overwrite = tkmsg.askyesno(title=" Binding already exists",message="Binding to '"+name+"' already exists. Overwrite binding?")
        if (overwrite):
            programs[name] = settings_selected_file
            debug("new binding:\n"+name+" -> "+settings_selected_file)
            debug("updated 'programs' dict:")
            debug(programs)
        else:
            debug("no bindings overwritten.")
            tkmsg.showinfo(title=" Notice",message="No bindings updated.")
    else:
        tkmsg.showinfo(title=" Notice",message="Binding already exists and cannot be overwritten.")
    save("QL-savedata-programs.pickle",programs)

def remove_app(name,file_label):
    try:
        f = programs[name]
    except:
        if (len(name) > 0):
            tkmsg.showwarning(title=" Notice",message="No binding exists with name '"+name+"'")
        else:
            tkmsg.showwarning(title=" Notice",message="Please enter a name of the binding to remove.")
        return False
    if (tkmsg.askyesno(title=" Warning",message="Are you sure you want to delete the following binding?\n"+name+" ->\n"+f)):
        debug("binding: '"+name+"' -> "+f+" deleted.")
        del programs[name]
        save("QL-savedata-programs.pickle",programs)
    else:
        tkmsg.showinfo(title=" Notice",message="Action Cancelled. No bindings deleted.")
        debug("no bindings deleted.")

def debug(string):
    if (DEBUG_MODE):
        print(str(string)+"\n")

def save(save_file,item_to_save):
    with open(save_file,"wb") as f:
        pickle.dump(item_to_save,f)
    debug("saved item:\n"+str(item_to_save)+" -> "+save_file)

def load(file_name):
    if (os.path.exists(file_name)):
        with open(file_name,'rb') as f:
            l = pickle.load(f)
            return l
    else:
        debug("no save exists at location: "+str(file_name))

def toggle_hints(hintsButton):
    global show_hints
    global hintsLabel
    global root_height
    show_hints = not show_hints
    if (not show_hints):
        hintsLabel.configure(text=VERSION_INFO)
        hintsButton.configure(text="Show Hints")
        debug("show_hints turned OFF")
        save("QL-savedata-showHints.pickle",False)
    else:
        hintsLabel.configure(text="[Return] Launch 1        [Shift-Return] Launch 2        [Alt-Return] Launch Recent        [Ctrl] Switch")
        hintsButton.configure(text="Hide Hints")
        debug("show_hints turned ON")
        save("QL-savedata-showHints.pickle",True)

def delete_save():
    if (tkmsg.askyesno(title=" WARNING",message="Are you sure you want to delete ALL save data? This includes any programs you may have added, and/or your selected browser.\nNOTE: To remove a single program, type its QuickLaunch Name into the 'QuickLaunch Name' field and press 'Remove App...'")):
        debug("deleting all save files...")
        if (os.path.exists("QL-savedata-browser.pickle")):
            os.remove("QL-savedata-browser.pickle")
            debug("removed file: QL-savedata-browser.pickle")
        if (os.path.exists("QL-savedata-programs.pickle")):
            os.remove("QL-savedata-programs.pickle")
            debug("removed file: QL-savedata-programs.pickle")
        if (os.path.exists("QL-savedata-showHints.pickle")):
            os.remove("QL-savedata-showHints.pickle")
            debug("removed file: QL-savedata-showHints.pickle")
        if (os.path.exists("QL-savedata-launchRecent.txt")):
            os.remove("QL-savedata-launchRecent.txt")
            debug("removed file: QL-savedata-launchRecent.txt")
        tkmsg.showinfo(title=" Notice",message=" All save data has been deleted. QuickLaunch will now close.")
        quit()
        debug("save data successfully deleted")
        close_settings()
    else:
        tkmsg.showinfo(title=" Notice",message="Action cancelled. No save data deleted.")
        debug("no save data deleted.")

def open_help():
    try:
        webbrowser.get(browser_path).open("http://wallenet.net/quicklaunch#how-it-works")
        quit()
    except IndexError:
        tkmsg.showinfo(title=" Notice",message=" Please select a browser first.")

def fill_main_with_alt(event=""):
    if (not in_settings):
        alt_program_text = altProgram.cget("text")
        if len(alt_program_text) > 0:
            e.delete(0,END)
            e.insert(0,alt_program_text)
            autofill()
            
"""

------------------------------------- Main Program Starts Here -------------------------------------

"""

# Create an empty savefile if one doesn't exist already
if (not os.path.exists("QL-savedata-launchRecent.txt")):
    debug("save file does not exist, creating a new empty save file...")
    f = open("QL-savedata-launchRecent.txt", "w")
    f.close()



# Load programs
try:
    saved_programs = load("QL-savedata-programs.pickle")
    for program_name in saved_programs:
        programs[program_name] = saved_programs[program_name]
except TypeError:
    debug("no saved programs found. continuing...")
finally:
    debug("current contents of 'programs':\n"+str(programs))

# Load hints
try:
    prev_show_hints = load("QL-savedata-showHints.pickle")
    if (os.path.exists("QL-savedata-showHints.pickle")):
        if (not show_hints == prev_show_hints):
            show_hints = not show_hints
except TypeError as e:
    debug("no saved hints preferences; assuming hints are wanted.")
    show_hints = True
finally:
    debug("current show_hints status: "+str(show_hints))

# Load browser
try:
    browser_path = load("QL-savedata-browser.pickle")
    if (not os.path.exists("QL-savedata-browser.pickle")):
        raise TypeError("No file exists: QL-savedata-browser.pickle")
except TypeError as e:
    debug("no saved browser path; will use default browser...")
    browser_path = ""
finally:
    debug("current browser_path: "+str(browser_path))




# Setup window
root = Tk()
root.title("QuickLaunch")
root.iconphoto(False, PhotoImage(file = 'logo.png'))
root.geometry("600x200")
root.configure(bg="red")
root.resizable(width=False,height=False)
root.overrideredirect(1)

mainFrame = Frame(root,width=600,height=200,bg=BACKGROUND_MAIN,bd=7)
mainFrame.place(relx=0.5,rely=0.5,anchor="center")

# Create entry and fill with any saved text
e = Entry(mainFrame,width=32,font="Bahnschrift 24",bg=BACKGROUND_ALT,fg="#ffffff",bd="5",relief=FLAT)
e.place(anchor="s",relx=0.5,rely=0.27)
try:
    s = open("QL-savedata-launchRecent.txt","r")
    savedtext = s.read()
    s.close()
except:
    savedtext = "QuickLaunch"
e.insert(0,savedtext)
e.focus_set()
e.bind("<FocusIn>", e.selection_range(0,END))

# Alt Program
altProgram = Label(mainFrame,text="",anchor="w",width=32,font="Bahnschrift 24",bg=BACKGROUND_2ALT,fg="#ffffff",bd=5,relief=FLAT)
altProgram.place(anchor="n",relx=0.5,rely=0.27)

# Create hints label
hintsLabel=Label(mainFrame,text="[Return] Launch 1        [Shift-Return] Launch 2        [Alt-Return] Launch Recent        [Ctrl] Switch",font="Bahnschrift 8",bg="#303030",fg="#ffffff",bd=10)
if (not show_hints):
    hintsLabel.configure(text=VERSION_INFO)
hintsLabel.place(anchor="center",relx=0.5,rely=0.65)

# Last Command button
lastCommand = "-"
if (savedtext != ""):
    lastCommand = savedtext
    lCList = list(lastCommand)
    lCList[0] = lCList[0].upper()
    lastCommand = "".join(lCList)
lastActionButton = Button(mainFrame,text="Launch Recent: "+lastCommand,font="Bahnschrift 18",width=44,bg=BACKGROUND_ALT,activebackground="#202020",fg="#ffffff",activeforeground="#ffffff",bd=0,command=last_call)
lastActionButton.place(anchor="sw",relx=0,rely=1)

# Settings button
settings_image = PhotoImage(file="logo.png")
settingsButton = Button(mainFrame,image=settings_image,bg=BACKGROUND_ALT,activebackground=BACKGROUND_ALT,bd=0,command=open_settings)
settingsButton.place(anchor="se",relx=1,rely=1)

# Call the 'callAlt' function when <Shift-Return> is pressed
root.bind('<Shift-Return>',alt_call)

# Call the 'callLast' function when <Alt-Return> is pressed
root.bind('<Alt-Return>',last_call)

# Call the 'call' function when <Return> is pressed
root.bind('<Return>',call)

# Call the 'fill_main_with_alt' function when <Ctrl> is pressed
root.bind('<Control_L>',fill_main_with_alt)

# Call the 'autofill' function when any key in 'keys' is pressed
keys="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-"
keys = list(keys)
for key in keys:
    root.bind(key,autofill)
root.bind("<space>",autofill)

# Run Tk
root.mainloop()