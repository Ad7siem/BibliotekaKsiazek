# Biblioteka Książek - Library app version 0.1.3 (BETA)

A simple program of the library of books for scouts from the city of Pabianice

The program is to facilitate the work of the library. The library will have a program to list and borrow books.
The database has three tables: listofbook, category and personalrental

## Status:
Cconstruction:
- settings window

Testing:
- creating entries in the list of books, people, categories

### Planing:
- convert code from functions to classes
- Done! - (add a tab with information about the app in the settings)
- Done! - (add functions in the data tab: creating a database copy, loading a database copy)
- will complete the colors tab in the settings window
- add the application start condition only from the main file
- Done! - (complete the tab with the size of the table)

### Developer information

Language:
- python 3.9
- SQLite

Library:
- sqlite
- tkinter
- configparser
- openpyxl
- os
- pathlib
- shutil
- own

### Changes made

0.1.4
Fixed:
- Correct search for people from the database
- Buttons for adding a person to the borrowers database are visible again



0.1.3
Add:
- Extract from menu.py class settings and put it in new file settings.py
- Colors Text have been added in the .ini file
- Added a function to search for people from the personal library in database.py
- Custom library has been added to colory.py
- Two text color changing functions have been added to the colory.py file
- A change to two variables has been added to the colory.py file in the reset method
- Descriptions of variables and functions / methods have been added to the colory.py file
- Some needed libraries have been added to the setting.py file 
- Two new LabelFrame have been added to the setting.py file
- In the setting.py file, a variable with help info has been added to find the file
- In the setting.py file in the method of indicating the location of database, moving it to the new location, if it exists, has been added
- In the setting.py file, a method for converting the database to an excel file has been created
- New widgets have been added to the setting.py file
- A method to create a copy of the database has been added to the setting.py file
- Descriptions have been added to the size_tab.py file
- Widgets for person search have been added in the persons.py file
- Added methods for clearing the board and for finding and displaying a person in the persons.py file
- Two variables have been added to treeview.py that retrieve data from the .ini file

Edit:
- The style variable was removed from main.py and placed in treeview.py
- Database gets the path from the .ini file
- Comment all items in view / Menu / auxialary.py
- Changed the way data is retrieved from the .ini file in the colory.py file
- In colory.py, variables from color_text (...) have been renamed to text_color (...)
- The main LabelFrame variable in setting.py has been renamed

Remove:
- Removed unnecessary library references from main.py
- Unnecessary libraries have been removed from menu.py
- An unnecessary library has been removed from the colory.py file
- An unnecessary library has been removed from the setting.py file
- Removed unnecessary function in treeview.py

### Planned changes
- Adding descriptions to the database.py file
- Removal of auxialary.py file from .view / Menu folder
- In treeview.py, changes to get variables from .ini file
- Further code change to classes
- in the README file, adding a description of the function and method