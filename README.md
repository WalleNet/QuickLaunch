# QuickLaunch
QuickLaunch is a simple program that allows you to find and launch programs with a keyboard shortcut. Just add programs and launch away!

QuickLaunch (6.0.0) by WalleNet
All Rights Reserved

*All steps not marked '(OPTIONAL)' are crucial to the function of the program and should not be omitted.
**To see all available features, see 'FEATURES.txt' in main directory.

#### REQUIRED MODULES (Installable via PIP or PIP3) ###
PROGRAM WILL NOT RUN WITHOUT THE FOLLOWING MODULES:
-tkinter
-webbrowser
-pyinstaller
-PIL
-tkinter.messagebox
-easygui
-pickle
Other modules (built-in with Python 3.*)
-os
-subprocess

#### INITIAL SETUP ####
Visit http://wallenet.net/QuickLaunch#how-it-works

#### INSTALL AS APPLICATION (.EXE) ####
1. Open a terminal window and navigate to the 'QuickLaunch' folder (containing 'config.py','QuickLaunch.py',etc.)
2. Run the command `pyinstaller -w --onedir QuickLaunch.py`
3. After the sequence finishes, you will see some additional folders. The .exe is located in the 'Dist' folder.
4. Move the logo.png file from the main folder to the folder with the .exe.

#### CREATING A KEY-BINDING (OPTIONAL, RECOMMENDED) ####
1. In the 'Dist' folder, right-click the .exe and create a shortcut
2. Right-click the newly-created shortcut, click 'Properties', and rename it if necessary.
3. You can type a key-binding under 'Shortcut', but it is faster to pin it to your taskbar.
4. Move it to the very left of the taskbar. Now pressing Win+1 will launch the program much faster.

Thank you for using QuickLaunch.
For Questions, email us at rohand.wallenet@gmail.com
