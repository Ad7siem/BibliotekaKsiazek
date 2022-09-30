from view.Treeview import treeview
from view.Entries import entries_box
from view.Button import button_box
from view.Search import search_box
from view.Menu import menu
from database import database
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from configparser import ConfigParser

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

### Configure the Treeview Colors
style.configure("Treeview",
				background="#D3D3D3",
				foreground="black",
				rowheight=25,
				fieldbackground="#D3D3D3"
				)

### Change Selected Color
style.map('Treeview',background=[('selected', "#347083")])

#################################################################
##################### Create space window #######################
#################################################################

###
menu.menu_app(root)
### Create Search Box
search_box.search_space(root)
### Create Table Box
treeview.treeview(root)
### Create Record Box
entries_box.entries_box(root)
### Create Button Box
button_box.button_box(root)
### Show database in Table
treeview.query_database()

###
root.mainloop()
