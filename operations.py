"""
The purpose of this file (operations.py) is to handle any file operations in this program. For window management, see main.py. 

Issues: Python is slow, and these custom maps range from 5 to 30 gigabytes. So, we will use system calls so that Windows
        will copy/delete the files for us. 

        # Important functionality
        # If someone tries to close the window while copying is taking place, it should cancel the copy.
            # I don't know if I actually need to implement this myself or if this is already how it is with python system calls.
"""
import os
import json

json_file_path = "config.json"

def save_text(workshop, usermaps):
    data = {
        "steam_workshop_directory": workshop.get(),
        "usermaps_directory": usermaps.get()
    }
    with open(json_file_path, "w") as file:
        json.dump(data, file)

def load_text(workshop, usermaps):
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as file:
            data = json.load(file)
            workshop.insert(0, data.get("steam_workshop_directory", ""))
            usermaps.insert(0, data.get("usermaps_directory", ""))

def get_maps(text_bar):
    entered_text = text_bar.get()
    maps = []
    try:
        #list all entries in the directory using list comprehension
        subfolders = [ f.name for f in os.scandir(entered_text) if f.is_dir() ]

        # List comprehension to filter subfolders that contain 'workshop.json'
        maps = [f for f in subfolders if os.path.isfile(os.path.join(entered_text, f, 'workshop.json'))]
        return maps
    except Exception as e:
        print(f"Error: {e}")
    return False
    
# TODO: 
# Make it so that this function copies the folders.

def workshop_copy(workshop):
    maps = get_maps(workshop)
    try:
        # print the names of the entries
        for entry in maps:
            print("Folder ", entry, "copied")
    except Exception as e:
        print(f"Error: {e}")
    
# TODO: 
# Make it so that this function deletes the folders.

def usermaps_delete(usermaps):
    maps = get_maps(usermaps)
    try:
        # print the names of the entries
        for entry in maps:
            print("Folder ", entry, "deleted")
    except Exception as e:
        print(f"Error: {e}")

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


