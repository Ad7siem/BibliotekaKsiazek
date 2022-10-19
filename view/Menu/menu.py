from tkinter import *
from view.Menu.settings import Settings


#################################################################
################## Create the top options bar ###################
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

