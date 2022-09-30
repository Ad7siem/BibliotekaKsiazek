from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from configparser import ConfigParser
from view.Treeview import treeview

#################################################################
############# Read our config files and get colors ##############
#################################################################
parser = ConfigParser()
parser.read('treebase.ini')
saved_primary_color = parser.get('colors', 'primary_color')
saved_secondary_color = parser.get('colors', 'secondary_color')
saved_highlight_color = parser.get('colors', 'highlight_color')
row_treeview = parser.get('treeview', 'row')
width_id = parser.get('treeview', 'ID')
width_title = parser.get('treeview', 'title')
width_author = parser.get('treeview', 'author')
width_position = parser.get('treeview', 'position')
width_category = parser.get('treeview', 'category')
width_date_rental = parser.get('treeview', 'date_rental')
width_person_rental = parser.get('treeview', 'person_rental')
width_other = parser.get('treeview', 'other')

#################################################################
###########  ############
#################################################################
def menu_app(root):
	### Add Menu
	my_menu = Menu(root)
	root.config(menu=my_menu)

	### Configure our menu
	option_menu = Menu(my_menu, tearoff=0)
	my_menu.add_cascade(label='Plik', menu=option_menu)

	### Drop down menu
	option_menu.add_command(label='Ustawienia', command=settings)
	# option_menu.add_command(label='Kolor podstawowy', command=primary_color)
	# option_menu.add_command(label='Kolor pomocniczy', command=secondary_color)
	# option_menu.add_command(label='Kolor podświetlania', command=highlight_color)
	# option_menu.add_separator()
	# option_menu.add_command(label='Reset kolorów', command=reset_colors)
	option_menu.add_separator()
	option_menu.add_command(label='Zamknij', command=root.quit)

	# ### Search Menu
	# search_menu = Menu(my_menu, tearoff=0)
	# my_menu.add_cascade(label='Search', menu=search_menu)
	# ### Drop down menu
	# search_menu.add_command(label='Search', command="")


#################################################################
###########  ############
#################################################################
def settings():
	global settings
	### Create Top Level - Mini Window
	settings = Toplevel()
	settings.title('Ustawienia')
	settings.resizable(0,0)
	settings.iconbitmap('bookshelf.ico')

	# settings.attributes('-topmost', 'true')

	###
	my_notebook = ttk.Notebook(settings)
	my_notebook.pack(pady=5, padx=5)

	###
	my_treeview = Frame(my_notebook, width=500, height=500)
	my_color = Frame(my_notebook, width=500, height=500)
	my_datebase = Frame(my_notebook, width=500, height=500)

	###
	my_treeview.pack(fill=BOTH, expand=1)
	my_color.pack(fill=BOTH, expand=1)
	my_datebase.pack(fill=BOTH, expand=1)

	###
	my_notebook.add(my_treeview, text='Tablica')
	my_notebook.add(my_color, text='Kolory')
	my_notebook.add(my_datebase, text='Dane')

	###
	table_size = LabelFrame(my_treeview, text='Rozmiar tablicy')
	table_size.pack(padx=10, pady=10)

	global row_entry
	row_label = Label(table_size, text='Ilość wierszy:')
	row_label.grid(row=0, column=0, padx=10, pady=5)
	row_entry = Entry(table_size, textvariable=row_treeview)
	row_entry.grid(row=0, column=1, padx=10, pady=10)
	row_button = Button(table_size, text='Ustaw', command=row_size)
	row_button.grid(row=0, column=2, padx=10, pady=5)

	size_column = Label(table_size, text='Szerokość kolumn:')
	size_column.grid(row=1, column=0, padx=10, pady=5)
	size_id_label = Label(table_size, text='ID:')
	size_id_label.grid(row=2, column=0, padx=10, pady=5)
	size_id_entry = Entry(table_size)
	size_id_entry.grid(row=2, column=1, padx=10, pady=5)
	size_id_button = Button(table_size, text='Ustaw', command="") 
	size_id_button.grid(row=2, column=2, padx=10, pady=5)
	size_title_label = Label(table_size, text='Nazwa Książki:')
	size_title_label.grid(row=3, column=0, padx=10, pady=5)
	size_title_entry = Entry(table_size)
	size_title_entry.grid(row=3, column=1, padx=10, pady=5)
	size_title_button = Button(table_size, text='Ustaw', command="") 
	size_title_button.grid(row=3, column=2, padx=10, pady=5)

	###
	table_color = LabelFrame(my_color, text='Kolor tablicy')
	table_color.pack(padx=10, pady=10)

	###
	global color_1_button, color_2_button, color_3_button
	color_1_label = Label(table_color, text='Kolor podstawowy:')
	color_1_label.grid(row=0, column=0, padx=10, pady=5)
	color_1_button = Button(table_color, width=5, bg=saved_primary_color, command=primary_color)
	color_1_button.grid(row=0, column=1, padx=(100, 10), pady=5)

	color_2_label = Label(table_color, text='Kolor pomocniczy:')
	color_2_label.grid(row=1, column=0, padx=10, pady=5)
	color_2_button = Button(table_color, width=5, bg=saved_secondary_color, command=secondary_color)
	color_2_button.grid(row=1, column=1, padx=(100, 10), pady=5)

	color_3_label = Label(table_color, text='Kolor podświetlania:')
	color_3_label.grid(row=2, column=0, padx=10, pady=5)
	color_3_button = Button(table_color, width=5, bg=saved_highlight_color, command=highlight_color)
	color_3_button.grid(row=2, column=1, padx=(100, 10), pady=5)

	color_text_1_label = Label(table_color, text='Kolor tekstu:')
	color_text_1_label.grid(row=3, column=0, padx=10, pady=5)
	color_text_1_button = Button(table_color, text='Kolor')
	color_text_1_button.grid(row=3, column=1, padx=(100, 10), pady=5)

	color_text_2_label = Label(table_color, text='Kolor tekstu podświetlonego')
	color_text_2_label.grid(row=4, column=0, padx=10, pady=5)
	color_text_2_button = Button(table_color, text='Kolor')
	color_text_2_button.grid(row=4, column=1, padx=(100, 10), pady=5)

	reset_color = Button(table_color, text='Restartuj kolory', command=reset_colors)
	reset_color.grid(row=5, column=0, padx=10, pady=5)

	###
	app_color = LabelFrame(my_color, text='Kolor aplikacji')
	app_color.pack(padx=10, pady=10)

	window_color_label = Label(app_color, text='Kolor okna')
	window_color_label.grid(row=0, column=0, padx=10, pady=5)
	window_color_button = Button(app_color, width=5)
	window_color_button.grid(row=0, column=1, padx=(100, 10), pady=5)

	settings.mainloop()



#################################################################
###########  ############
#################################################################
def primary_color():
	### Pick Color
	primary_color = colorchooser.askcolor()[1]

	### Update Treeview Color
	if primary_color:
		### Create Striped Row Tags
		treeview.config_color_treeview('evenrow', primary_color)

		### Config file
		parser = ConfigParser()
		parser.read("treebase.ini")

		### Set the color change
		parser.set("colors", "primary_color", primary_color)

		### Save the config file
		with open("treebase.ini", "w") as configfile:
			parser.write(configfile)

		color_1_button.config(bg=primary_color)

	settings.deiconify()



#################################################################
###########  ############
#################################################################
def secondary_color():
	### Pick Color
	secondary_color = colorchooser.askcolor()[1]

	### Update Treeview Color
	if secondary_color:
		### Create Striped Row Tags
		treeview.config_color_treeview('oddrow', secondary_color)

		### Config file
		parser = ConfigParser()
		parser.read("treebase.ini")

		### Set the color change
		parser.set("colors", "secondary_color", secondary_color)

		### Save the config file
		with open("treebase.ini", "w") as configfile:
			parser.write(configfile)

		color_2_button.config(bg=secondary_color)

	settings.deiconify()



#################################################################
###########  ############
#################################################################
def highlight_color():
	### Pick Color
	highlight_color = colorchooser.askcolor()[1]

	### Update Treeview Color
	if highlight_color:
		### Add Some Style
		style = ttk.Style()
		### Create Striped Row Tags
		style.map("Treeview", background=[('selected', highlight_color)])

		### Config file
		parser = ConfigParser()
		parser.read("treebase.ini")

		### Set the color change
		parser.set("colors", "highlight_color", highlight_color)

		### Save the config file
		with open("treebase.ini", "w") as configfile:
			parser.write(configfile)

		color_3_button.config(bg=highlight_color)

	settings.deiconify()


#################################################################
###########  ############
#################################################################
def reset_colors():
	### Save original colors to config file
	parser = ConfigParser()
	parser.read("treebase.ini")
	parser.set("colors", "primary_color", parser["colors_copy"]["primary_color"])
	parser.set("colors", "secondary_color", parser["colors_copy"]["secondary_color"])
	parser.set("colors", "highlight_color", parser["colors_copy"]["highlight_color"])

	with open("treebase.ini", "w") as configfile:
		parser.write(configfile)

	### Add Some Style
	style = ttk.Style()
	### Reset the colors
	saved_primary_color = parser.get('colors', 'primary_color')
	saved_secondary_color = parser.get('colors', 'secondary_color')
	saved_highlight_color = parser.get('colors', 'highlight_color')
	
	treeview.config_color_treeview('oddrow', saved_secondary_color)
	treeview.config_color_treeview('evenrow', saved_primary_color)
	style.map("Treeview", background=[("selected", saved_highlight_color)])

	color_1_button.config(bg=saved_primary_color)
	color_2_button.config(bg=saved_secondary_color)
	color_3_button.config(bg=saved_highlight_color)

def row_size():
	parser = ConfigParser()
	parser.read("treebase.ini")
	parser.set("treeview", "row", row_entry.get())
	with open("treebase.ini", "w") as configfile:
		parser.write(configfile)

	treeview.config_row_treeview(row_entry.get())