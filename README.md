# Boiii Usermaps manager
### Automates a manual step required when playing custom maps on the Boiii client for Call of Duty Black Ops 3.

The plan is to have easily buildable python code with instructions, as well as an executable file for those who cannot code (If you've come this far, you probably have what it takes).
<br>It will use tkinter for a GUI.<br><br>

## Here's the plan so far
### Phase 0
Define the other phases in detail and set expectations for what should be implemented in each phase.
### Phase 1
#### Barebones functionality. (we are here as of 13 Sep 2024)
+ Copying and Deleting of the maps are implemented. One of the buttons are clicked to copy/delete all of the maps.
+ The ui looks like this: Two text input bars for the folder directories. Two buttons, one for copying everything (from the steam workshop folder) and one for deleting everything (from the usermaps folder).
### Phase 2
#### Give the user visual feedback
+ Here, three boxes are added:
    + One to display maps in the steam workshop folder.
    + One to display maps in the usermaps folder.
    + One to display information about any map that is selected by clicking it.
+ One button is added:
    + Rescan for new/removed maps.
### Phase 3
#### Increasing Usability
+ The file path bars are supplemented with a button that opens a menu to select a file (done via Windows file handling).
+ Try to guess where the folders are, when the project is launched for the first time.
+ The file locations are saved persistently for convenience.
+ We can click on the maps in the folder to select them.
    + shift click and control click will behave in a way that one would expect them to.
+ We have buttons for copying/deleting the selected maps mentioned above.
### Phase 4
#### Exe release
+ Write detailed build instructions
+ Make an executable
### Phase 5
#### Bonus features
+ Check to see if the map in the usermaps folder is out of date (compared to one in the workshop folder)
    + Notify the user / highlight the map
    + Copy all button will update the map
    + Copy one button will say "update map" when selecting a map that is out of date.
## Disclaimer
<br><br><br>
This is not done yet.<br><br>
I am not affiliated with Activision, Treyarch, Black Ops 3, or any other franchises or copyrights connected to this project.
