"""
The purpose of this file (operations.py) is to handle any file operations in this program. For window management, see main.py. 

Issues: Python is slow, and these custom maps range from 5 to 30 gigabytes. So, we will use system calls so that Windows
        will copy/delete the files for us. 
"""


"""
The purpose of this function is to return information about the files in a given folder,
so that it can be displayed to the user. 
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
This function should be called by a helper function. It takes in an array of folder names, and for each name, it copies the folder with that name.

There will be an error popup if the file name does not exist.
"""

def copy_selected_maps():
    pass




"""
This function should be called by a helper function. It takes in an array of folder names, and for each name, it deletes the folder with that name.

There will be an error popup if the file name does not exist.
"""
def delete_selected_maps():
    pass