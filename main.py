# This program is designed to make it easy to sync maps to the Boiii client's folder, and to delete maps from that folder.
"""
Here's the gist of how it will run.
1. Try to find the steam workshop folder, and the boiii client folder. If it can't, prompt the user for the
directory locations before letting them copy/transfer anything
2. For the steam workshop folder (left side) and the boiii client folder (right side), display one of the following:
    a. An indicator that this is either the wrong folder, or that no maps are in this folder
    b. A list of installed maps with their thumbnail and info
3. The user will then select maps on the left side and click on a button to copy them.
4. When the user is done, they may select maps on the right side to delete them.
5. The user can close the program at any time.


Issues: Python is slow, and these custom maps range from 5 to 30 gigabytes. So, we will use system calls so that Windows
        will copy/delete the files for us. 

TODO: 
Implement get_info()
Implement create_window()
Add tracking for which items are selected. Alternatively only let one item be selected.
"""

"""
The purpose of this function is to feed information about the files in the Steam Workshop folder into the window function,
so that it can be displayed to the user. Called in several places.
"""
def get_info():
    # print("Getting info...")
    # Get some useful info, and return it. If any entries do not have the expected information, then don't store them.
    # First, open the "..steamapps\workshop\content\311210" folder in read mode (this does not lock the file on Windows)
        # Figure out how many maps are in the steam workshop folder
        
        # Iterate over each subfolder and make a record for:
            # The name of the folder itself
            # The map's total file size
            # The location of previewimage.png
            # In workshop.json:
                # Description
                # FolderName (map name)
                # Tags (?)
                # Title
    # Close the folder
    pass

"""
Open a window for the user to interact with. It will try to make sure that the directories are correct, and if they aren't,
the program will demand the user to set them before it will function.
"""
def create_window():

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
    pass

"""
This function should be called by the window when the user presses the refresh button, the copy button, or the delete button. 
It calls get_info() to update the display with any new information.

I don't think I need to worry about maps being downloaded while this function executes, because they seem to appear in the
directory only when they are fully installed.
"""
def update_window():
    pass

"""
This function is called by the copy button. It gets a list of selected items and calls the "copy_selected_maps()" function below with
them as an argument. 
"""
def copy_button():
    pass

"""
This function should be called by a helper function. It takes in an array of folder names, and for each name, it copies the folder with that name.

There will be an error popup if the file name does not exist.
"""

def copy_selected_maps():
    pass


"""
This function is called by the delete button. It gets a list of selected items and calls the "delete_selected_maps()" function below with
them as an argument. 
"""
def copy_button():
    pass

"""
This function should be called by a helper function. It takes in an array of folder names, and for each name, it deletes the folder with that name.

There will be an error popup if the file name does not exist.
"""
def delete_selected_maps():
    pass