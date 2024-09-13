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

### main.py ###
1.)
Currently buttons will print out whatever is in the text box. Change
the button behavior so that they print out the name of every folder
in the directory of the input box.

2.)
Create a function that will take two file directories (string) as
input, and copy all folders with criteria X (defined below) from the
first directory to the second one.
Criteria X: The folder has a file named "workshop.json". In the JSON
file, it must have this field inside: "Type": "map". (This basically
restricts the program into using maps, at least until phase 5).

### operations.py ###



"""

import tkinter as tk

def workshop_loc_submit():
    entered_text = workshop_loc.get()
    print("workshop map: ", entered_text)
    pass

def usermaps_loc_submit():
    entered_text = usermaps_loc.get()
    print("usermaps: ", entered_text)
    pass

"""
This function should be called when the user presses the refresh button, the copy button, or the delete button. 
It calls get_info() to update the display with any new information.

Note: The folders seem to appear in the directory only when they are fully installed.
"""
def update_window():
    pass


# Copy button handler 
def copy_button():
    pass

#Delete button handler 
def delete_button():
    pass

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

## add some submit buttons
tk.Button(window, text="Submit", width=6, command=workshop_loc_submit) .grid(row=2, column=1, sticky="w")
tk.Button(window, text="Submit", width=6, command=usermaps_loc_submit) .grid(row=4, column=1, sticky="w")

# The window should have:
        # Two boxes (They show information about the two file directories we are concerned about)
            # Entries in each box should be selectable, and the user should be able to click and drag, or shift/ctrl click to multi-select
        # A title bar
        # An icon
        # Two buttons, one for copying to the boiii directory and one for deleting maps from it.
        # A side pane that shows the thumbnail, size in gigabytes, description, and other info. 
            # The description may need to be in a scroll box, depending on if there's limits to how long it can be.

    # Important functionality
        # If someone tries to close the window while copying is taking place, it should cancel the copy.
            # I don't know if I actually need to implement this myself or if this is already how it is with python system calls.


### Run the main loop
window.mainloop()