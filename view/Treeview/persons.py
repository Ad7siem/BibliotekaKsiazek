from tkinter import *
from tkinter import ttk
from database import database
from view.Treeview import auxiliary


#################################################################
########### Add person to database ############
################################################################# 
def add_person():
	### Create Top Level - Mini Window
	add_person = Toplevel()
	add_person.title("Dodawanie osoby")
	add_person.iconbitmap('bookshelf.ico')
	add_person.resizable(0,0)
	add_person.grab_set()

	### Create Label of the window
	window = Label(add_person)
	window.pack(padx=10, pady=10)

	###
	treeveiw_frame = Frame(window)
	treeveiw_frame.grid(row=0, column=0, padx=10, pady=10)
	treeview_person(treeveiw_frame)

	###
	option_frame = LabelFrame(window, text='Opcje')
	option_frame.grid(row=0, column=1, padx=10, pady=10)

	###
	add_record_frame = Frame(option_frame)
	add_record_frame.pack(padx=10, pady=10)

	###
	global firstName_entry, lastName_entry, team_entry, contact_entry
	firstName_label = Label(add_record_frame, text='Imię:')
	firstName_label.grid(row=0, column=0, padx=10, pady=0)
	firstName_entry = Entry(add_record_frame)
	firstName_entry.grid(row=0, column=1, padx=10, pady=0)

	lastName_label = Label(add_record_frame, text='Nazwisko:')
	lastName_label.grid(row=1, column=0, padx=10, pady=0)
	lastName_entry = Entry(add_record_frame)
	lastName_entry.grid(row=1, column=1, padx=10, pady=0)

	team_label = Label(add_record_frame, text='Drużyna:')
	team_label.grid(row=2, column=0, padx=10, pady=0)
	team_entry = Entry(add_record_frame)
	team_entry.grid(row=2, column=1, padx=10, pady=0)

	contact_label = Label(add_record_frame, text='Kontakt:')
	contact_label.grid(row=3, column=0, padx=10, pady=0)
	contact_entry = Entry(add_record_frame)
	contact_entry.grid(row=3, column=1, padx=10, pady=0)

	###
	separator = ttk.Separator(option_frame, orient='horizontal')
	separator.pack(fill=X, pady=10)

	###
	add_button = Button(option_frame, text='Dodaj Osobę', width=20, command=add_record)
	add_button.pack(padx=10, pady=0)

	###
	delete_button = Button(option_frame, text='Usuń Osobę', width=20, command=remove_record)
	delete_button.pack(padx=10, pady=(0,10))

	### Bind the treeview
	my_tree.bind("<ButtonRelease-1>", select_record)

	###
	query_persons_database()


#################################################################
###########  ############
################################################################# 
def select_person():
	### Create Top Level - Mini Window
	global select_person
	select_person = Toplevel()
	select_person.title('Wybór osoby')
	select_person.resizable(0, 0)
	select_person.iconbitmap('bookshelf.ico')
	select_person.grab_set()


	### Create Label of the window
	window = Label(select_person)
	window.pack(padx=10, pady=10)

	###
	search_person = LabelFrame(window, text='Wyszukiwanie osoby')
	search_person.pack(pady=(0, 15))

	###
	global search_person_entry
	search_person_entry = Entry(search_person, width=50)
	search_person_entry.grid(row=0, column=0, padx=5, pady=(5, 10))
	search_person_button = Button(search_person, text='Wyszukaj', command=search_records_person)
	search_person_button.grid(row=0, column=1, padx=5, pady=(5, 10))

	### Create The Treeview
	treeview_person(window)

	###
	select_person_button = Button(window, text='Wybierz osobę', command=person)
	select_person_button.pack(padx=10, pady=10)

	###
	query_persons_database()


#################################################################
###########  ############
################################################################# 
def treeview_person(root):
	### Create a Treeview Frame
	tree_frame = Frame(root)
	tree_frame.pack(padx=10, pady=10)

	### Create The Treeview
	global my_tree
	my_tree = ttk.Treeview(tree_frame)
	my_tree.pack()

	### Define Our Columns
	my_tree['columns'] = ("ID", "firstName", "lastName", "team", "contact")

	### Frame Our Columns
	my_tree.column("#0", width=0, stretch=NO)
	my_tree.column("ID", anchor=CENTER, width=20)
	my_tree.column("firstName", anchor=CENTER, width=100)
	my_tree.column("lastName", anchor=CENTER, width=100)
	my_tree.column("team", anchor=CENTER, width=80)
	my_tree.column("contact", anchor=CENTER, width=80)

	### Create Headings
	my_tree.heading("#0", text='', anchor=W)
	my_tree.heading("ID", text='ID', anchor=CENTER)
	my_tree.heading("firstName", text='Imię', anchor=CENTER)
	my_tree.heading("lastName", text='Nazwisko', anchor=CENTER)
	my_tree.heading("team", text='Drużyna', anchor=CENTER)
	my_tree.heading("contact", text='Kontakt', anchor=CENTER)

	### Create Striped Row Tags
	my_tree.tag_configure('oddrow', background="white")
	my_tree.tag_configure('evenrow', background="lightblue")


#################################################################
###########  ############
################################################################# 
def clear_treeview_person():
	my_tree.delete(*my_tree.get_children())


#################################################################
###########  ############
################################################################# 
def search_records_person():
	###
	clear_treeview_person()

	###
	lookup_record = search_person_entry.get()
	count = 0
	
	for record in database.lookup_records_person(lookup_record):
		if count % 2 == 0:
			my_tree.insert(parent='', index=END, iid=count, text='',
							values=(record[0], record[1], record[2], record[3], record[4]),
							tags=('evenrow'))
		else:
			my_tree.insert(parent='', index=END, iid=count, text='',
							values=(record[0], record[1], record[2], record[3], record[4]),
							tags=('oddrow'))
		count += 1


#################################################################
###########  ############
################################################################# 
def query_persons_database():
	for record in my_tree.get_children():
		my_tree.delete(record)

	count = 0

	for record in database.show_database('personrental'):
		if count % 2 == 0: 
			my_tree.insert(parent='', index=END, iid=count, text='',
							values=(record[0], record[1], record[2], record[3], record[4]),
							tags=('evenrow'))
		else:
			my_tree.insert(parent='', index=END, iid=count, text='',
							values=(record[0], record[1], record[2], record[3], record[4]),
							tags=('oddrow'))
		count += 1


#################################################################
###########  ############
################################################################# 
def select_record(e):
	### Clear Entry boxes
	clear_record()	

	### Grab record values
	values = my_tree.item(my_tree.focus(), 'values')

	### Outpus to entry boxes
	insert_record(values)


#################################################################
###########  ############
################################################################# 
def clear_record():
	### Clear Entry boxes
	firstName_entry.delete(0, END)
	lastName_entry.delete(0, END)
	team_entry.delete(0, END)
	contact_entry.delete(0, END)


#################################################################
###########  ############
################################################################# 
def insert_record(values):
	try:
		firstName_entry.insert(0, values[1])
		lastName_entry.insert(0, values[2])
		team_entry.insert(0, values[3])
		contact_entry.insert(0, values[4])
	except:
		pass


#################################################################
###########  ############
################################################################# 
def add_record():
	###
	record = [
		firstName_entry.get(),
		lastName_entry.get(),
		team_entry.get(),
		contact_entry.get()
	]

	###
	database.add_records_personrental(record)

	###
	my_tree.delete(*my_tree.get_children())

	###
	query_persons_database()

	### Clear Entry Boxes
	clear_record()


#################################################################
###########  ############
################################################################# 
def remove_record():
	### Remove record in database
	database.delete_record('personrental', my_tree.item(my_tree.focus(), 'values')[0])

	###
	my_tree.delete(*my_tree.get_children())

	###
	query_persons_database()

	### Clear Entry Boxes
	clear_record()


#################################################################
###########  ############
################################################################# 
def person():
	###
	cs = f"{my_tree.item(my_tree.selection(), 'values')[1]} {my_tree.item(my_tree.selection(), 'values')[2]}"
	auxiliary.person_entry(cs)

	select_person.destroy()