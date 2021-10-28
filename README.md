# QuickLaunch
QuickLaunch is a simple program that allows you to find and launch programs with a keyboard shortcut. Just add programs and launch away!

QuickLaunch (6.0.0) by WalleNet
All Rights Reserved

*All steps not marked '(OPTIONAL)' are crucial to the function of the program and should not be omitted.
**To see all available features, see 'FEATURES.txt' in main directory.

## Required Modules (Installable via PIP or PIP3)
PROGRAM WILL NOT RUN WITHOUT THE FOLLOWING MODULES:
1. tkinter
2. webbrowser
3. pyinstaller
4. PIL
5. tkinter.messagebox
6. easygui
7. pickle
Other modules (built-in with Python 3.*)
1. os
2. subprocess

## Setup
Visit http://wallenet.net/quicklaunch#how-it-works

## Installation
1. Open a terminal window and navigate to the 'QuickLaunch' folder (containing 'config.py','QuickLaunch.py',etc.)
2. Run the command `pyinstaller -w --onedir QuickLaunch.py`
3. After the sequence finishes, you will see some additional folders. The .exe is located in the 'Dist' folder.
4. Move the logo.png file from the main folder to the folder with the .exe.
5. For more info visit http://wallenet.net/quicklaunch#installation-instructions

## Creating a key binding (Optional, recommended)
1. In the 'Dist' folder, right-click the .exe and create a shortcut
2. Right-click the newly-created shortcut, click 'Properties', and rename it if necessary.
3. You can type a key-binding under 'Shortcut', but it is faster to pin it to your taskbar.
4. Move it to the very left of the taskbar. Now pressing Win+1 will launch the program much faster.

## Thank you
Thank you for using QuickLaunch.
For Questions, email us at rohand.wallenet@gmail.com
