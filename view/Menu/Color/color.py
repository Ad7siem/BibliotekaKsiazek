from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from configparser import ConfigParser
from view.Treeview import treeview
from ..auxialiary import settings_deiconify

class Color:
	def __init__(self, root):
		### Read our config files and get colors 
		parser = ConfigParser()
		parser.read('treebase.ini')
		saved_primary_color = parser.get('colors', 'primary_color')
		saved_secondary_color = parser.get('colors', 'secondary_color')
		saved_highlight_color = parser.get('colors', 'highlight_color')

		###
		table_color = LabelFrame(root, text='Kolor tablicy')
		table_color.pack(padx=10, pady=10)

		###
		global color_1_button, color_2_button, color_3_button
		color_1_label = Label(table_color, text='Kolor podstawowy:')
		color_1_label.grid(row=0, column=0, padx=10, pady=5)
		self.color_1_button = Button(table_color, width=5, bg=saved_primary_color, command=self.primary_color)
		self.color_1_button.grid(row=0, column=1, padx=(100, 10), pady=5)

		color_2_label = Label(table_color, text='Kolor pomocniczy:')
		color_2_label.grid(row=1, column=0, padx=10, pady=5)
		self.color_2_button = Button(table_color, width=5, bg=saved_secondary_color, command=self.secondary_color)
		self.color_2_button.grid(row=1, column=1, padx=(100, 10), pady=5)

		color_3_label = Label(table_color, text='Kolor podświetlania:')
		color_3_label.grid(row=2, column=0, padx=10, pady=5)
		self.color_3_button = Button(table_color, width=5, bg=saved_highlight_color, command=self.highlight_color)
		self.color_3_button.grid(row=2, column=1, padx=(100, 10), pady=5)

		color_text_1_label = Label(table_color, text='Kolor tekstu:')
		color_text_1_label.grid(row=3, column=0, padx=10, pady=5)
		color_text_1_button = Button(table_color, text='Kolor')
		color_text_1_button.grid(row=3, column=1, padx=(100, 10), pady=5)

		color_text_2_label = Label(table_color, text='Kolor tekstu podświetlonego')
		color_text_2_label.grid(row=4, column=0, padx=10, pady=5)
		color_text_2_button = Button(table_color, text='Kolor')
		color_text_2_button.grid(row=4, column=1, padx=(100, 10), pady=5)

		reset_color = Button(table_color, text='Restartuj kolory', command=self.reset_colors)
		reset_color.grid(row=5, column=0, padx=10, pady=5)

		###
		app_color = LabelFrame(root, text='Kolor aplikacji')
		app_color.pack(padx=10, pady=10)

		window_color_label = Label(app_color, text='Kolor okna')
		window_color_label.grid(row=0, column=0, padx=10, pady=5)
		window_color_button = Button(app_color, width=5)
		window_color_button.grid(row=0, column=1, padx=(100, 10), pady=5)



	#################################################################
	###########  ############
	#################################################################
	def primary_color(self):
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

			self.color_1_button.config(bg=primary_color)

		settings_deiconify()


	#################################################################
	###########  ############
	#################################################################
	def secondary_color(self):
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

			self.color_2_button.config(bg=secondary_color)

		settings_deiconify()



	#################################################################
	###########  ############
	#################################################################
	def highlight_color(self):
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

			self.color_3_button.config(bg=highlight_color)

		settings_deiconify()


	#################################################################
	###########  ############
	#################################################################
	def reset_colors(self):
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
		
		###
		treeview.config_color_treeview('oddrow', saved_secondary_color)
		treeview.config_color_treeview('evenrow', saved_primary_color)
		style.map("Treeview", background=[("selected", saved_highlight_color)])

		###
		self.color_1_button.config(bg=saved_primary_color)
		self.color_2_button.config(bg=saved_secondary_color)
		self.color_3_button.config(bg=saved_highlight_color)

if __name__ == '__main__':
	Color()