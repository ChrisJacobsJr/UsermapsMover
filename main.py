"""
This program is designed to make it easy to sync maps to the Boiii client's folder, and to delete maps from that folder.

Here's the gist of how it will run.
1. Try to find the steam workshop folder, and the boiii client folder. If it can't, prompt the user for the
directory locations before letting them copy/transfer anything
2. For the steam workshop folder (left side) and the boiii client folder (right side), display one of the following:
    a. An indicator that this is either the wrong folder, or that no maps are in this folder
    b. A list of installed maps with their thumbnail and info
3. The user will then select maps on the left side and click on a button to copy them.
4. When the user is done, they may select maps on the right side to delete them.
5. The user can close the program at any time.

This file (main.py) serves as the window handler for the program. For file-related operations, see operations.py


TODO: #### PHASE 1 ####

### main.py (this file) ###
1.) (FINISHED)
Currently buttons will print out whatever is in the text box. Change
the button behavior so that they print out the name of every folder
in the directory of the input box, with "copied" or "deleted", based
on the button. Also, change the button text to reflect this behavior.

3.) (FINISHED)
Call the function in operations.py (via the copy-all button) that was
created in step 2, using strings obtained by reading the file
directory from the text boxes. If necessary, change the text input 
(file directory) so that it will work with python.

5.) (FINISHED)
move anything file related to operations.py

6.)
Conclude Phase 1


### operations.py ###
2.)
Create a function that will take two file directories (string) as
input, and copy all folders with criteria X (defined below) from the
first directory to the second one.
Criteria X: The folder has a file named "workshop.json". In the JSON
file, it must have this field inside: "Type": "map". (This basically
restricts the program into using maps, at least until phase 5).

4.)
Create a function similar to the one in step 2. It has 2 differences:
First, it only takes one variable, the directory of the usermaps
folder. Second, it deletes the folders instead of copying them
elsewhere.



"""

import tkinter as tk
import os
import json
import operations   # file operations are handled here

'''
Event handlers
'''
def copy_button():
    operations.workshop_copy(workshop_loc)
def delete_button():
    operations.usermaps_delete(usermaps_loc)

def on_closing():
    operations.save_text(workshop_loc, usermaps_loc)
    window.destroy()

'''
Window management
'''
### Make the window
window = tk.Tk()
window.title("Usermaps Mover")
window.geometry("800x400")
# window.resizable(False, False)

## Create some labels:
# Steam workshop location:
tk.Label (window, text="Steam Workshop Folder", bg="white", fg="black", font="none 12 bold", ) .grid(row=1, column=0, sticky="w")
# Usermaps folder location:
tk.Label (window, text="Usermaps Folder", bg="white", fg="black", font="none 12 bold", ) .grid(row=3, column=0, sticky="w")

## create some text entry boxes
# Steam workshop location:
workshop_loc = tk.Entry(window, width=20, bg="white")
workshop_loc.grid(row=2, column=0, sticky="w")
# Usermaps folder location:
usermaps_loc = tk.Entry(window, width=20, bg="white")
usermaps_loc.grid(row=4, column=0, sticky="w")

## add some buttons
tk.Button(window, text="Copy", width=6, command=copy_button) .grid(row=2, column=1, sticky="w")
tk.Button(window, text="Delete", width=6, command=delete_button) .grid(row=4, column=1, sticky="w")


### Initialize the window
## load in the file directories to the text boxes before the window opens
operations.load_text(workshop_loc, usermaps_loc)

## Set the protocol for the window close event
window.protocol("WM_DELETE_WINDOW", on_closing)

### Run the main loop
window.mainloop()