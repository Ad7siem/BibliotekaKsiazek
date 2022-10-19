from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from configparser import ConfigParser
from view.Treeview import treeview
from treebase import Parser


#################################################################
############### Create Option Coloru - Settings #################
#################################################################
class Color:
	def __init__(self, root):
		### Add Some Style
		self.style = ttk.Style()

		### Read our config files and get colors 
		self.parser = Parser()
		saved_primary_color = self.parser.get_parser('colors', 'primary_color')
		saved_secondary_color = self.parser.get_parser('colors', 'secondary_color')
		saved_highlight_color = self.parser.get_parser('colors', 'highlight_color')
		saved_text_color = self.parser.get_parser('colors', 'text_color')
		saved_text_highlight_color = self.parser.get_parser('colors', 'text_highlight_color')

		### Create LabelFrame Tab
		table_color = LabelFrame(root, text='Kolor tablicy')
		table_color.pack(padx=10, pady=10)

		### Create Label and Button color settings
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

		text_color_1_label = Label(table_color, text='Kolor tekstu:')
		text_color_1_label.grid(row=3, column=0, padx=10, pady=5)
		self.text_color_1_button = Button(table_color, width=5, bg=saved_text_color, command=self.text_color)
		self.text_color_1_button.grid(row=3, column=1, padx=(100, 10), pady=5)

		text_color_2_label = Label(table_color, text='Kolor tekstu podświetlonego')
		text_color_2_label.grid(row=4, column=0, padx=10, pady=5)
		self.text_color_2_button = Button(table_color, width=5, bg=saved_text_highlight_color, command=self.text_highlight_color)
		self.text_color_2_button.grid(row=4, column=1, padx=(100, 10), pady=5)

		reset_color = Button(table_color, text='Restartuj kolory', command=self.reset_colors)
		reset_color.grid(row=5, column=0, padx=10, pady=5)

		### ???
		app_color = LabelFrame(root, text='Kolor aplikacji')
		app_color.pack(padx=10, pady=10)

		window_color_label = Label(app_color, text='Kolor okna')
		window_color_label.grid(row=0, column=0, padx=10, pady=5)
		window_color_button = Button(app_color, width=5)
		window_color_button.grid(row=0, column=1, padx=(100, 10), pady=5)


	#################################################################
	##### Create options to change the base color of an array #######
	#################################################################
	def primary_color(self):
		### Pick Color
		primary_color = colorchooser.askcolor()[1]

		### Update Treeview Color
		if primary_color:
			### Create Striped Row Tags
			treeview.config_color_treeview('evenrow', primary_color)

			### Set the color change
			self.parser.edit_parser("colors", "primary_color", primary_color)

			### Change color button
			self.color_1_button.config(bg=primary_color)


	#################################################################
	### Create an option to change the second color of the board ####
	#################################################################
	def secondary_color(self):
		### Pick Color
		secondary_color = colorchooser.askcolor()[1]

		### Update Treeview Color
		if secondary_color:
			### Create Striped Row Tags
			treeview.config_color_treeview('oddrow', secondary_color)

			### Set the color change
			self.parser.edit_parser("colors", "secondary_color", secondary_color)
			
			### Change color button
			self.color_2_button.config(bg=secondary_color)


	#################################################################
	### Create options to change the color of the row highlight #####
	#################################################################
	def highlight_color(self):
		### Pick Color
		highlight_color = colorchooser.askcolor()[1]

		### Update Treeview Color
		if highlight_color:
			### Create Striped Row Tags
			self.style.map("Treeview", background=[('selected', highlight_color)])

			### Set the color change
			self.parser.edit_parser("colors", "highlight_color", highlight_color)

			### Change color button
			self.color_3_button.config(bg=highlight_color)


	#################################################################
	### Create options for changing the color of the table text #####
	#################################################################
	def text_color(self):
		### Pick Color
		text_color = colorchooser.askcolor()[1]

		### Update Treeview Color
		if text_color:
			### Create Striped Row Tags
			self.style.configure('Treeview', foreground=text_color)

			### Set the color change
			self.parser.edit_parser("colors", "text_color", text_color)

			### Change color button
			self.text_color_1_button.config(bg=text_color)


	##################################################################
	# Create options to change the text color of the highlighted row #
	##################################################################
	def text_highlight_color(self):
		### Pick Color
		text_highlight_color = colorchooser.askcolor()[1]

		### Update Treeview Color
		if text_highlight_color:
			### Create Striped Row Tags
			self.style.map('Treeview', foreground=[('selected', text_highlight_color)])

			### Set the color change
			self.parser.edit_parser("colors", "text_highlight_color", text_highlight_color)

			### Change color button
			self.text_color_2_button.config(bg=text_highlight_color)


	#################################################################
	############# Reset the colors to the basic values ##############
	#################################################################
	def reset_colors(self):
		### Save original colors to config file
		self.parser.edit_parser("colors", "primary_color", self.parser.get_parser("colors_copy", "primary_color"))
		self.parser.edit_parser("colors", "secondary_color", self.parser.get_parser("colors_copy", "secondary_color"))
		self.parser.edit_parser("colors", "highlight_color", self.parser.get_parser("colors_copy", "highlight_color"))
		self.parser.edit_parser("colors", "text_color", self.parser.get_parser("colors_copy", "text_color"))
		self.parser.edit_parser("colors", "text_highlight_color", self.parser.get_parser("colors_copy", "text_highlight_color"))

		### Reset the colors
		saved_primary_color = self.parser.get_parser("colors", "primary_color")
		saved_secondary_color = self.parser.get_parser("colors", "secondary_color")
		saved_highlight_color = self.parser.get_parser("colors", "highlight_color")
		saved_text_color = self.parser.get_parser("colors", "text_color")
		saved_text_highlight_color = self.parser.get_parser("colors", "text_highlight_color")
		
		### Defult setting color
		treeview.config_color_treeview('oddrow', saved_secondary_color)
		treeview.config_color_treeview('evenrow', saved_primary_color)
		self.style.map("Treeview", background=[("selected", saved_highlight_color)])
		self.style.configure("Treeview", foreground=f"{saved_text_color}")
		self.style.map("Treeview", foreground=[("selected", saved_text_highlight_color)])

		### Change color button
		self.color_1_button.config(bg=saved_primary_color)
		self.color_2_button.config(bg=saved_secondary_color)
		self.color_3_button.config(bg=saved_highlight_color)
		self.text_color_1_button.config(bg=saved_text_color)
		self.text_color_2_button.config(bg=saved_text_highlight_color)



if __name__ == '__main__':
	Color()