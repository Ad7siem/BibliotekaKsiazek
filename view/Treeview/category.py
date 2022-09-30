from tkinter import colorchooser
from tkinter import *
from tkinter import ttk
from database import database
from view.Treeview import auxiliary


#################################################################
########### Add category to database ############
################################################################# 
def add_category():
	### Create Top Level - Mini Window
	add_category = Toplevel()
	add_category.title("Dodawanie Kategorii")
	add_category.iconbitmap('bookshelf.ico')
	add_category.resizable(0,0)

	### Create Label of the window
	window = Label(add_category)
	window.pack(padx=10, pady=10)

	###
	treeview_category(window)

	###
	add_record_frame = LabelFrame(window, text="Opcje")
	add_record_frame.grid(row=0, column=1, padx=10, pady=10)

	###
	global new_category_entry

	new_category_label = Label(add_record_frame, text="Nowa Kategoria")
	new_category_label.pack(padx=10, pady=10)
	new_category_entry = Entry(add_record_frame)
	new_category_entry.pack(padx=10, pady=10)
	new_category_button = Button(add_record_frame, text="Dodaj Kategorie", width=20, command=new_category)
	new_category_button.pack(padx=10, pady=10)

	###
	separator = ttk.Separator(add_record_frame, orient='horizontal')
	separator.pack(fill='x')

	###
	global delate_category_entry

	delate_category_label = Label(add_record_frame, text="Usuń Kategorię")
	delate_category_label.pack(padx=10, pady=10)
	delate_category_entry = Entry(add_record_frame)
	delate_category_entry.pack(padx=10, pady=10)
	delate_category_button = Button(add_record_frame, text="Usuń Kategorię", width=20, command=remove_category)
	delate_category_button.pack(padx=10, pady=10)


	### Bind the treeview
	my_tree.bind("<ButtonRelease-1>", select_record)

	###
	query_category_database()


#################################################################
###########  ############
################################################################# 
def select_category():
	### Create Top Level - Mini Window
	global select_category
	select_category = Toplevel()
	select_category.title('Wybór Kategorii')
	select_category.resizable(0,0)
	select_category.iconbitmap('bookshelf.ico')


	### Create Label of the window
	window = Label(select_category)
	window.pack(padx=10, pady=10)

	### Create The Treeview
	treeview_category(window)

	###
	select_category_button = Button(window, text='Wybierz Kategorie', command=select_categories)
	select_category_button.grid(row=1, column=0, padx=10, pady=10)

	###
	query_category_database()


#################################################################
###########  ############
################################################################# 
def treeview_category(root):
	### Create a Treeview Frame
	tree_frame = Frame(root)
	tree_frame.grid(row=0, column=0, padx=10, pady=10)

	# tree_scroll = Scrollbar(tree_frame)
	# tree_frame.pack(side=RIGHT, fill='y')

	### Create The Treeview
	global my_tree
	my_tree = ttk.Treeview(tree_frame)
	my_tree.pack()

	# tree_scroll.config(command=my_tree.yview)

	### Define Our Columns
	my_tree['columns'] = ("ID", "Nazwa Kategorii")

	### Frame Our Columns
	my_tree.column("#0", width=0, stretch=NO)
	my_tree.column("ID", anchor=CENTER, width=20)
	my_tree.column("Nazwa Kategorii", anchor=W, width=180)

	### Create Headings
	my_tree.heading("#0", text="", anchor=W)
	my_tree.heading("ID", text="ID", anchor=CENTER)
	my_tree.heading("Nazwa Kategorii", text="Nowa Kategoria", anchor=CENTER)

	### Create Striped Row Tags
	my_tree.tag_configure('oddrow', background="white")
	my_tree.tag_configure('evenrow', background="lightblue")
	

#################################################################
###########  ############
################################################################# 
def query_category_database():
	for record in my_tree.get_children():
		my_tree.delete(record)

	global count
	count = 0

	for record in database.show_database('categories'):
		if count % 2 == 0:
			my_tree.insert(parent='',
							index='end',
							iid=count,
							text='',
							values=(record[0], record[1]),
							tags=('evenrow'))
		else:
			my_tree.insert(parent='',
							index='end',
							iid=count,
							text='',
							values=(record[0], record[1]),
							tags=('oddrow'))
		count += 1

#################################################################
###########  ############
################################################################# 
def new_category():
	###
	record = [new_category_entry.get()]

	###
	database.add_records_categories(record)

	###
	my_tree.delete(*my_tree.get_children())

	###
	query_category_database()

	###
	new_category_entry.delete(0, END)


#################################################################
###########  ############
################################################################# 
def select_categories():
	###
	cs = ''
	for record in my_tree.selection():
		cs += (my_tree.item(record, 'values')[1])
		if record != my_tree.selection()[-1]:
			cs += ' - '

	auxiliary.category_entry(cs)

	select_category.destroy()


#################################################################
###########  ############
################################################################# 
def select_record(e):
	# Clear entry boxes
	new_category_entry.delete(0, END)

	# Grab record Number
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')

	# Outpus to entry boxes
	try:
		delate_category_entry.insert(0, values[1])
	except:
		pass


#################################################################
###########  ############
################################################################# 
def remove_category():
	###
	database.delete_record('categories', my_tree.item(my_tree.focus(), 'values')[0])

	###
	my_tree.delete(*my_tree.get_children())

	###
	query_category_database()

	###
	delate_category_entry.delete(0, END)










