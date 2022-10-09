from tkinter import *
from tkinter import ttk
from .Tab.size_tab import Size_tab
from .Color.color import Color
from .Database.setting import Setting_database
from .Info.info import Info


#################################################################
###########  ############
#################################################################
class Menu_app:
	def __init__(self, root):
		### Add Menu
		my_menu = Menu(root)
		root.config(menu=my_menu)

		### Configure our menu
		option_menu = Menu(my_menu, tearoff=0)
		my_menu.add_cascade(label='Plik', menu=option_menu)

		### Drop down menu
		option_menu.add_command(label='Ustawienia', command=Settings)
		option_menu.add_separator()
		option_menu.add_command(label='Zamknij', command=root.quit)


	#################################################################
	###########  ############
	#################################################################
class Settings:
	def __init__(self):
		### Create Top Level - Mini Window
		self.settings = Toplevel()
		self.settings.title('Ustawienia')
		self.settings.resizable(0,0)
		self.settings.iconbitmap('bookshelf.ico')

		# settings.attributes('-topmost', 'true')

		###
		my_notebook = ttk.Notebook(self.settings)
		my_notebook.pack(pady=5, padx=5)

		###
		my_treeview = Frame(my_notebook)
		my_color = Frame(my_notebook)
		my_datebase = Frame(my_notebook)
		my_info = Frame(my_notebook)

		###
		my_treeview.pack(fill=BOTH, expand=1)
		my_color.pack(fill=BOTH, expand=1)
		my_datebase.pack(fill=BOTH, expand=1)
		my_info.pack(fill=BOTH, expand=1)

		###
		my_notebook.add(my_treeview, text='Tablica')
		my_notebook.add(my_color, text='Kolory')
		my_notebook.add(my_datebase, text='Dane')
		my_notebook.add(my_info, text='Informacje')

		### Table size
		Size_tab(my_treeview)
		Color(my_color)
		Setting_database(my_datebase)
		Info(my_info)

		###
		self.settings.mainloop()	
