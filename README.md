# QuickLaunch
QuickLaunch is a simple program that allows you to find and launch programs with a keyboard shortcut. Just add the programs to the config file and launch away!

QuickLaunch (5.1) by WalleNet
All Rights Reserved

*All steps not marked '(OPTIONAL)' are crucial to the function of the program and should not be omitted.
**To see all available features, see 'FEATURES.txt' in main directory.

#### REQUIRED MODULES (Installable via PIP or PIP3) ###
PROGRAM WILL NOT RUN WITHOUT THE FOLLOWING MODULES:
-tkinter
-webbrowser
-pyinstaller
Other modules (built-in with Python 3.*)
-os
-subprocess

#### INITIAL SETUP ####
Initial setup will require you to modify the 'config.py' file. This is also how you will add programs.

1. Set your default browser path at the top of the file. Chrome is recommended and tested. Other 
browsers should be considered experimental to this program and therefore may not function as planned.
Do not delete the ' %s' after the browser path. 
2. Add Programs
	a) edit the dictionary 'programs'
	b) as the key (<PROGRAM NAME HERE>) enter the name of the program IN LOWERCASE
	c) as the value (<PROGRAM PATH HERE>) enter the FULL path of the program, ending with .exe,.py, etc.
	d) for all entries but the last add a comma at the end-of-line (demonstrated by placeholders)
	e) !IMPORTANT! delete the two test values already stored in 'programs'
3. Edit/Remove any of the Windows settings or extras you don't want, stored in 'settings' 
and 'extras', respectively.

#### INSTALL AS APPLICATION (.EXE) ####
1. Open a terminal window and navigate to the 'QuickLaunch' folder (containing 'config.py','QuickLaunch.py',etc.)
2. Run the command 'pyinstaller -w --onedir QuickLaunch.py'
3. After the sequence finishes, you will see some additional folders. The .exe is located in the 'Dist' folder.
4. If it doesn't already exist, create a blank .txt file named 'QL-savedata.txt' in the 'Dist' folder.

#### CREATING A KEY-BINDING (OPTIONAL, RECOMMENDED) ####
1. In the 'Dist' folder, right-click the .exe and create a shortcut
2. Right-click the newly-created shortcut, click 'Properties', and rename it if necessary.
3. Assign an icon by clicking 'Change Icon...' under 'Shortcut' and assign it the 'icon.ico' file
found in the base directory.
4. You can type a key-binding under 'Shortcut', but it is faster to pin it to your taskbar.
5. Move it to the very left of the taskbar. Now pressing Win+1 will launch the program much faster.

Thank you for using QuickLaunch.
For Questions, email us at rohand.wallenet@gmail.com
