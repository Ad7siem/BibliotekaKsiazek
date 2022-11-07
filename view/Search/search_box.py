from tkinter import *
from view.Treeview import treeview
from database import database


#################################################################
##################### Create Search Space  ######################
#################################################################
def search_space(root):
	### Create a Search Frame
	search_frame = LabelFrame(root, text='Wyszukaj')
	search_frame.pack(padx=20, pady=5)

	### Add Label and Entry Box
	global search_entry
	search_label = Label(search_frame, text='Wyszukaj:')
	search_label.grid(row=0, column=0, padx=10, pady=10)
	search_entry = Entry(search_frame, width=60)
	search_entry.grid(row=0, column=1, padx=10, pady=10)
	search_button = Button(search_frame, text='Szukaj!', width=20, command=search_records)
	search_button.grid(row=0, column=2, padx=(10, 100), pady=10)
	refresh_my_tree_button = Button(search_frame, text='Odśwież Tablicę', width=20, command=treeview.query_database)
	refresh_my_tree_button.grid(row=0, column=3, padx=(50, 105), pady=10)


#################################################################
########### Create a function that searches for data ############
#################################################################
def search_records():
	### Clear The Treeview
	treeview.clear_treeview()

	### Search Record in Database
	lookup_record = search_entry.get()
	count = 0

	for record in database.lookup_records(lookup_record):
		if count % 2 == 0:
			treeview.insert_treeview(count, record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], 'evenrow')
		else:
			treeview.insert_treeview(count, record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], 'oddrow')

		count += 1
