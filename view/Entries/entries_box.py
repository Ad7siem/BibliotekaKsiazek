from tkinter import *
from tkcalendar import *
from view.Treeview import category
from view.Treeview import persons

#################################################################
###########  ############
#################################################################
def entries_box(root):
	global title_entry, author_entry, position_entry, id_label, category_entry, date_rental_entry, person_rental_entry, other_text, entries_frame
	###
	entries_frame = LabelFrame(root, text='Wpis w bazie danych')
	entries_frame.pack(padx=20, pady=5)

	###
	title_label = Label(entries_frame, text='Nazwa Książki')
	title_label.grid(row=0, column=0, padx=10, pady=10)
	title_entry = Entry(entries_frame, width=25)
	title_entry.grid(row=0, column=1, padx=10, pady=10)

	author_label = Label(entries_frame, text='Autor')
	author_label.grid(row=0, column=2, padx=10, pady=10)
	author_entry = Entry(entries_frame, width=25)
	author_entry.grid(row=0, column=3, padx=10, pady=10)

	position_label = Label(entries_frame, text='Miejsce Książki')
	position_label.grid(row=0, column=4, padx=10, pady=10)
	position_entry = Entry(entries_frame, width=25)
	position_entry.grid(row=0, column=5, padx=10, pady=10)

	category_label = Button(entries_frame, text='Kategorie', width=15, command=category.select_category)
	category_label.grid(row=1, column=0, padx=10, pady=10)
	category_entry = Entry(entries_frame, width=25)
	category_entry.grid(row=1, column=1, padx=10, pady=10)

	date_rental_label = Label(entries_frame, text='Data Wyp.')
	date_rental_label.grid(row=1, column=2, padx=10, pady=10)
	# date_rental_dateEntry = DateEntry(entries_frame, width=20, selectmode="month")
	# date_rental_dateEntry.grid(row=1, column=3, padx=10, pady=10)
	date_rental_entry = Entry(entries_frame, width=25)
	date_rental_entry.grid(row=1, column=3, padx=10, pady=10)

	person_rental_label = Button(entries_frame, text='Osoba Wyp.', width=15, command=persons.select_person)
	person_rental_label.grid(row=1, column=4, padx=10, pady=10)
	person_rental_entry = Entry(entries_frame, width=25)
	person_rental_entry.grid(row=1, column=5, padx=10, pady=10)

	other_label = Label(entries_frame, text='Uwagi')
	other_label.grid(row=3, column=0, padx=10, pady=10)
	other_text = Text(entries_frame, width=65, height=2)
	other_text.grid(row=3, column=1, rowspan=2, columnspan=4, padx=10, pady=10)

	id_label = Label(entries_frame, text='ID:   ')
	# id_label.grid(row=3, column=4, padx=10, pady=10)

	clear_boxes_button = Button(entries_frame, text='Wyczyść pola', width=15, command=clear_entries_box) 
	clear_boxes_button.grid(row=3, column=5, padx=10, pady=10)

#################################################################
###
#################################################################
def clear_entries_box():
	### Clear entry boxes
	title_entry.delete(0, END)
	author_entry.delete(0, END)
	position_entry.delete(0, END)
	category_entry.delete(0, END)
	date_rental_entry.delete(0, END)
	person_rental_entry.delete(0, END)
	other_text.delete("1.0", END)
	id_label.config(text='ID:   ')
	entries_frame.config(text=f'Wpis w bazie danych')


#################################################################
###
#################################################################
def insert_records(values):
	try:
		title_entry.insert(0, values[1])
		author_entry.insert(0, values[2])
		position_entry.insert(0, values[3])
		category_entry.insert(0, values[4])
		date_rental_entry.insert(0, values[5])
		person_rental_entry.insert(0, values[6])
		other_text.insert("1.0", values[7])
		id_label.config(text=f'ID: {values[0]}')
		entries_frame.config(text=f'ID: {values[0]}')
	except:
		pass

		
#################################################################
###
#################################################################
def records():
	records = [(
		title_entry.get(),
		author_entry.get(),
		position_entry.get(),
		category_entry.get(),
		date_rental_entry.get(),
		person_rental_entry.get(),
		other_text.get("1.0",END),
		)]
	return records

#################################################################
###
#################################################################
def ID_record():
	return id_label['text'][4:]

#################################################################
###
#################################################################
def category_record(values):
	category_entry.delete(0, END)
	category_entry.insert(0, values)

#################################################################
###
#################################################################
def person_record(values):
	person_rental_entry.delete(0, END)
	person_rental_entry.insert(0, values)



