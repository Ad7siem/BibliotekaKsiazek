from tkinter import *
from tkinter import ttk
from .Tab.size_tab import Size_tab
from .Color.color import Color
from .Database.setting import Setting_database
from .Info.info import Info


#################################################################
####### Create a setting function in the top options bar ########
#################################################################
class Settings:
    def __init__(self):
        ### Create Top Level - Mini Window
        self.settings = Toplevel()
        self.settings.title('Ustawienia')
        self.settings.resizable(0,0)
        self.settings.iconbitmap('bookshelf.ico')
        self.settings.grab_set()

        ### Create Notebook - the space of the Top Tabs 
        my_notebook = ttk.Notebook(self.settings)
        my_notebook.pack(pady=5, padx=5)

        ### Create space single tab
        my_treeview = Frame(my_notebook)
        my_color = Frame(my_notebook)
        my_datebase = Frame(my_notebook)
        my_info = Frame(my_notebook)

        ### Placement of the tab space
        my_treeview.pack(fill=BOTH, expand=1)
        my_color.pack(fill=BOTH, expand=1)
        my_datebase.pack(fill=BOTH, expand=1)
        my_info.pack(fill=BOTH, expand=1)

        ### Adding links with the name to the top tabs
        my_notebook.add(my_treeview, text='Tablica')
        my_notebook.add(my_color, text='Kolory')
        my_notebook.add(my_datebase, text='Dane')
        my_notebook.add(my_info, text='Informacje')

        ### Table size
        Size_tab(my_treeview)
        Color(my_color)
        Setting_database(my_datebase)
        Info(my_info)

        ### Completing the execution of commands
        self.settings.mainloop()