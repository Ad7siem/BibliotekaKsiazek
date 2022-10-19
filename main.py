from view.Treeview import treeview
from view.Entries.entries_box import entries_box
from view.Button.button_box import Button_box
from view.Search import search_box
from view.Menu.menu import Menu_app
from database import database
from tkinter import *
from tkinter import ttk


database.create_table()
#################################################################
######################## Create Window ##########################
#################################################################
root = Tk()
root.title('Spis Książek i wypożyczeń')
root.iconbitmap('bookshelf.ico')
# root.geometry("1080x850")
# root.config()

#################################################################
######################### Style Config ##########################
#################################################################
### Add Some Style
style = ttk.Style()

### Pick A Theme
style.theme_use('default')

#################################################################
##################### Create space window #######################
#################################################################

###
Menu_app(root)
### Create Search Box
search_box.search_space(root)
### Create Table Box
treeview.treeview(root)
### Create Record Box
entries_box(root)
### Create Button Box
Button_box(root)
### Show database in Table
treeview.query_database()

###
root.mainloop()
