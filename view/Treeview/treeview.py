from tkinter import ttk
from tkinter import *
from configparser import ConfigParser
from database import database
from view.Entries import entries_box

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
###################### Create The Treeview ######################
#################################################################
def treeview(root):
	global my_tree

	### Create a Treeview Frame
	tree_frame = Frame(root)   	
	tree_frame.pack(fill=BOTH, expand=True, pady=20, padx=20)

	### Create a Treeview Scrollbar
	tree_scroll_y = Scrollbar(tree_frame, orient=VERTICAL)
	tree_scroll_y.pack(side=RIGHT, fill=Y)
	tree_scroll_x = Scrollbar(tree_frame, orient=HORIZONTAL)
	tree_scroll_x.pack(side=BOTTOM, fill=X)

	### Create The Treeview
	my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set, selectmode="extended", height=row_treeview)
	my_tree.pack(fill=BOTH, expand=True)

	### Configure the Scrollbar
	tree_scroll_y.config(command=my_tree.yview)
	tree_scroll_x.config(command=my_tree.xview)

	### Define Our Columns
	my_tree['columns'] = ("ID", "title", "author", "position",
							"category", "date_rental", "person_rental", "other")

	### Frame Our Columns
	my_tree.column("#0", width=0, stretch=NO)
	my_tree.column("ID", anchor=CENTER, width=width_id)
	my_tree.column("title", anchor=W, width=width_title)
	my_tree.column("author", anchor=W, width=width_author)
	my_tree.column("position", anchor=CENTER, width=width_position)
	my_tree.column("category", anchor=CENTER, width=width_category)
	my_tree.column("date_rental", anchor=CENTER, width=width_date_rental)
	my_tree.column("person_rental", anchor=CENTER, width=width_person_rental)
	my_tree.column("other", anchor=W, width=width_other)

	### Create Headings
	my_tree.heading("#0", text='', anchor=W)
	my_tree.heading("ID", text='ID', anchor=CENTER)
	my_tree.heading("title", text='Nazwa Książki', anchor=CENTER)
	my_tree.heading("author", text='Autor', anchor=CENTER)
	my_tree.heading("position", text='Miejsce Książki', anchor=CENTER)
	my_tree.heading("category", text='Kategorie', anchor=CENTER)
	my_tree.heading("date_rental", text='Data Wyp.', anchor=CENTER)
	my_tree.heading("person_rental", text='Osoba Wypożyczająca', anchor=CENTER)
	my_tree.heading("other", text='Uwagi', anchor=CENTER)

	### Create Striped Row Tags
	my_tree.tag_configure("oddrow", background=saved_secondary_color)
	my_tree.tag_configure("evenrow", background=saved_primary_color)

	### Bind the treeview
	my_tree.bind("<ButtonRelease-1>", cursor_my_tree)

#################################################################
##### Create a function that shows the contents of a table ######
#################################################################
def query_database():
	### Clear the Treeview
	clear_treeview()

	### Add out data to the screen
	count = 0
	for record in database.show_database('listofbook'):
		if count % 2 == 0:
			insert_treeview(count, record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], 'evenrow')

		else:
			insert_treeview(count, record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], 'oddrow')

		count += 1


#################################################################
###########  ############
#################################################################
def cursor_my_tree(e):
	###
	entries_box.clear_entries_box()
	###
	values = my_tree.item(my_tree.focus(), 'values')
	###
	entries_box.insert_records(values)


#################################################################
###########  ############
#################################################################
def list_id():
	### Create list of ID's
	ids_to_delete = []
	### Append to list
	for record in my_tree.selection():
		ids_to_delete.append(my_tree.item(record, 'values')[0])

	return ids_to_delete


#################################################################
###########  ############
#################################################################
def config_color_treeview(row, color):
	return my_tree.tag_configure(f'{row}', background=color)

# #################################################################
# ###########  ############
# #################################################################
# def config_color_text_treeview(row, color):
# 	return my_tree.tag_configure(f'{row}', background=color)


#################################################################
###########  ############
#################################################################
def insert_treeview(iid, value_1,value_2,value_3,value_4,value_5,value_6,value_7, value_8, tags):
	return my_tree.insert(parent="", index=END, iid=iid, text='', 
							values=(value_1, value_2, value_3, value_4, value_5, value_6, value_7, value_8),
							tags=(tags, ))


#################################################################
###########  ############
#################################################################
def config_row_treeview(size):
	return my_tree.config(height=size)

#################################################################
#############  ##############
#################################################################
def config_column_size(column, size):
	return my_tree.column(f"{column}", width=size)

#################################################################
###########  ############
#################################################################
def clear_treeview():
	my_tree.delete(*my_tree.get_children())












