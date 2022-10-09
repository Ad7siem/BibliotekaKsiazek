from tkinter import *
from tkinter import messagebox
from view.Treeview import treeview
from view.Entries import entries_box
from database import database
from view.Treeview import category
from view.Treeview import persons

#################################################################
###########  ############
#################################################################
class Button_box:
	def __init__(self, root):
		self.root = root
		###
		button_frame = LabelFrame(root, text='Opcje')
		button_frame.pack(padx=20, pady=(5,20))

		add_button = Button(button_frame, text='Dodaj Książkę', width=20, command=self.add_record)
		add_button.grid(row=0, column=0, padx=(13, 10), pady=10)

		update_button = Button(button_frame, text='Edytuj wpis', width=20, command=self.update_record)
		update_button.grid(row=0, column=1, padx=10, pady=10)

		remove_entries_button = Button(button_frame, text='Usuń wpis', width=20, command=self.remove_many)
		remove_entries_button.grid(row=0, column=2, padx=10, pady=10)

		add_category_button = Button(button_frame, text='Dodaj Kategorię', width=20, command=category.add_category)
		add_category_button.grid(row=0, column=3, padx=10, pady=10)

		add_person_button = Button(button_frame, text='Dodaj Osobę', width=20, command=persons.add_person)
		add_person_button.grid(row=0, column=4, padx=10, pady=10)


	#################################################################
	###########  ############
	#################################################################
	def add_record(self):
		### Add list to database
		database.add_records_listofbook(entries_box.records())

		### Clear entry boxes
		entries_box.clear_entries_box

		### Show update the treeview table
		treeview.query_database()

	#################################################################
	###########  ############
	#################################################################
	def update_record(self):
		### Update list in database
		database.update_record(entries_box.records()[0], entries_box.ID_record())

		### Show table database in Treeview
		treeview.query_database()

		### Clear entry boxes
		entries_box.clear_entries_box

	#################################################################
	###########  ############
	#################################################################
	def remove_many(self):
		### Add a message box Yes or No
		response = messagebox.askyesno('Usuwanie wpisu', 'Czy na pewno chcesz usunąć książkę/i ze spisu?')

		###
		if response == 1:
			### Designate selections
			database.delete_records(treeview.list_id())

			### Show table database in Treeview
			treeview.query_database()

			### Clear entry boxes
			entries_box.clear_entries_box

	#################################################################
	###########  ############
	#################################################################
	def remove_one(self):
		### Add a message box Yes or No
		response = messagebox.askyesno('Usuwanie wpisu', 'Czy na pewno chcesz usunąć książkę ze spisu?')

		###
		if response == 1:
			### Delete Record in database
			database.delete_record('listofbook', entries_box.ID_record())

			### Show table database in Treeview
			treeview.query_database()

			### Clear entry boxes
			entries_box.clear_entries_box


if __name__ == '__main__':
	Button_box()