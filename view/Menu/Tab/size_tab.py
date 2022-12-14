from tkinter import *
from view.Treeview import treeview
from treebase import Parser


#################################################################
################## Create array size options ####################
#################################################################
class Size_tab:
    def __init__(self, root):
        ### Read our config files and get colors
        self.parser = Parser()
        row_treeview = self.parser.get_parser('treeview', 'row')
        width_id = self.parser.get_parser('treeview', 'id')
        width_title = self.parser.get_parser('treeview', 'title')
        width_author = self.parser.get_parser('treeview', 'author')
        width_position = self.parser.get_parser('treeview', 'position')
        width_category = self.parser.get_parser('treeview', 'category')
        width_date_rental = self.parser.get_parser('treeview', 'date_rental')
        width_person_rental = self.parser.get_parser('treeview', 'person_rental')
        width_other = self.parser.get_parser('treeview', 'other')

        ### Create LabelFrame Tab
        table_size = LabelFrame(root, text='Rozmiar Tablicy')
        table_size.pack(padx=10, pady=10)

        ### Create Label, Scale, Button displayed minimum number of table rows
        row_label = Label(table_size, text='Ilość wierszy')
        row_label.grid(row=0, column=0, padx=10, pady=5)
        self.row_scale = Scale(table_size, from_=0, to=20, orient=HORIZONTAL)
        self.row_scale.set(row_treeview)
        self.row_scale.grid(row=0, column=1, padx=10, pady=5)
        row_button = Button(table_size, text='Ustaw', command=self.row_size)
        row_button.grid(row=0, column=2, padx=10, pady=5)

        ### Create Label width column
        size_column = Label(table_size, text='Szerokość kolumn:')
        size_column.grid(row=1, column=0, padx=10, pady=(5,0))

        ### Create Label, Scale, Button width "ID" column
        size_id_label = Label(table_size, text='ID:')
        size_id_label.grid(row=2, column=0, padx=10, pady=0)
        self.size_id_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_id_scale.set(width_id)
        self.size_id_scale.grid(row=2, column=1, padx=10, pady=0)
        size_id_button = Button(table_size, text='Ustaw', command=self.id_size)
        size_id_button.grid(row=2, column=2, padx=10, pady=0)

        ### Create Label, Scale, Button width "Name Book" column
        size_title_label = Label(table_size, text='Nazwa Książki:')
        size_title_label.grid(row=3, column=0, padx=10, pady=0)
        self.size_title_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_title_scale.set(width_title)
        self.size_title_scale.grid(row=3, column=1, padx=10, pady=0)
        size_title_button = Button(table_size, text='Ustaw', command=self.title_size)
        size_title_button.grid(row=3, column=2, padx=10, pady=0)

        ### Create Label, Scale, Button width "Author" column
        size_author_label = Label(table_size, text='Autor:')
        size_author_label.grid(row=4, column=0, padx=10, pady=0)
        self.size_author_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_author_scale.set(width_author)
        self.size_author_scale.grid(row=4, column=1, padx=10, pady=0)
        size_author_button = Button(table_size, text='Ustaw', command=self.author_size)
        size_author_button.grid(row=4, column=2, padx=10, pady=0)

        ### Create Label, Scale, Button width "Position" column
        size_position_label = Label(table_size, text='Pozycja książki:')
        size_position_label.grid(row=5, column=0, padx=10, pady=0)
        self.size_position_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_position_scale.set(width_position)
        self.size_position_scale.grid(row=5, column=1, padx=10, pady=0)
        size_position_button = Button(table_size, text='Ustaw', command=self.position_size)
        size_position_button.grid(row=5, column=2, padx=10, pady=0)

        ### Create Label, Scale, Button width "Category" column
        size_category_label = Label(table_size, text='Kategorie:')
        size_category_label.grid(row=6, column=0, padx=10, pady=0)
        self.size_category_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_category_scale.set(width_category)
        self.size_category_scale.grid(row=6, column=1, padx=10, pady=0)
        size_category_button = Button(table_size, text='Ustaw', command=self.category_size)
        size_category_button.grid(row=6, column=2, padx=10, pady=0)

        ### Create Label, Scale, Button width "Date rental" column
        size_date_rental_label = Label(table_size, text='Data wypożyczenia:')
        size_date_rental_label.grid(row=7, column=0, padx=10, pady=0)
        self.size_date_rental_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_date_rental_scale.set(width_date_rental)
        self.size_date_rental_scale.grid(row=7, column=1, padx=10, pady=0)
        size_date_rental_button = Button(table_size, text='Ustaw', command=self.date_rental_size)
        size_date_rental_button.grid(row=7, column=2, padx=10, pady=0)

        ### Create Label, Scale, Button width "Person rental" column
        size_person_rental_label = Label(table_size, text='Osoba wypożyczająca:')
        size_person_rental_label.grid(row=8, column=0, padx=10, pady=0)
        self.size_person_rental_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_person_rental_scale.set(width_person_rental)
        self.size_person_rental_scale.grid(row=8, column=1, padx=10, pady=0)
        size_person_rental_button = Button(table_size, text='Ustaw', command=self.person_rental_size)
        size_person_rental_button.grid(row=8, column=2, padx=10, pady=0)

        ### Create Label, Scale, Button width "Other" column
        size_other_label = Label(table_size, text='Uwagi:')
        size_other_label.grid(row=9, column=0, padx=10, pady=0)
        self.size_other_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_other_scale.set(width_other)
        self.size_other_scale.grid(row=9, column=1, padx=10, pady=0)
        size_other_button = Button(table_size, text='Ustaw', command=self.other_size)
        size_other_button.grid(row=9, column=2, padx=10, pady=(0, 5))

        ### Create Button to reset size tab
        reset_size = Button(root, text='Reset rozmiaru tablicy', command=self.reset_sice_tab)
        reset_size.pack(padx=10, pady=5)


    #################################################################
    ########## Create option to reset table size settings ###########
    #################################################################
    def reset_sice_tab(self):
        ### Save to .ini file
        self.parser.edit_parser('treeview', 'row', self.parser.get_parser('treeview_copy', 'row'))
        self.parser.edit_parser('treeview', 'id', self.parser.get_parser('treeview_copy', 'id'))
        self.parser.edit_parser('treeview', 'title', self.parser.get_parser('treeview_copy', 'title'))
        self.parser.edit_parser('treeview', 'author', self.parser.get_parser('treeview_copy', 'author'))
        self.parser.edit_parser('treeview', 'position', self.parser.get_parser('treeview_copy', 'position'))
        self.parser.edit_parser('treeview', 'date_rental', self.parser.get_parser('treeview_copy', 'date_rental'))
        self.parser.edit_parser('treeview', 'person_rental', self.parser.get_parser('treeview_copy', 'person_rental'))
        self.parser.edit_parser('treeview', 'other', self.parser.get_parser('treeview_copy', 'other'))

        ### Set the scale to their default value
        self.row_scale.set(self.parser.get_parser('treeview', 'row'))
        self.size_id_scale.set(self.parser.get_parser('treeview', 'id'))
        self.size_title_scale.set(self.parser.get_parser('treeview', 'title'))
        self.size_author_scale.set(self.parser.get_parser('treeview', 'author'))
        self.size_position_scale.set(self.parser.get_parser('treeview', 'position'))
        self.size_category_scale.set(self.parser.get_parser('treeview', 'category'))
        self.size_date_rental_scale.set(self.parser.get_parser('treeview', 'date_rental'))
        self.size_person_rental_scale.set(self.parser.get_parser('treeview', 'person_rental'))
        self.size_other_scale.set(self.parser.get_parser('treeview', 'other'))

        ### Set the size of the array to the scale value
        self.row_size()
        self.id_size()
        self.title_size()
        self.author_size()
        self.position_size()
        self.category_size()
        self.date_rental_size()
        self.person_rental_size()
        self.other_size()


    #################################################################
    ########### Create a minimum number of lines option #############
    #################################################################
    def row_size(self):
        ### Save to .ini file
        self.parser.edit_parser("treeview", "row", self.row_scale.get())

        ### Change whiteboard settings
        treeview.config_row_treeview(self.row_scale.get())


    #################################################################
    ############### Create "ID" column width options ################
    #################################################################
    def id_size(self):
        ### Save to .ini file
        self.parser.edit_parser("treeview", "id", self.size_id_scale.get())

        ### Change whiteboard settings
        treeview.config_column_size("ID", self.size_id_scale.get())


    #################################################################
    ########### Create "Name Book" column width options #############
    #################################################################
    def title_size(self):
        ### Save to .ini file
        self.parser.edit_parser("treeview", "titile", self.size_title_scale.get())

        ### Change whiteboard settings
        treeview.config_column_size('title', self.size_title_scale.get())


    #################################################################
    ############# Create "Author" column width options ##############
    #################################################################
    def author_size(self):
        ### Save to .ini file
        self.parser.edit_parser("treeview", "author", self.size_author_scale.get())

        ### Change whiteboard settings
        treeview.config_column_size('author', self.size_author_scale.get())


    #################################################################
    ############ Create "Position" column width options #############
    #################################################################
    def position_size(self):
        ### Save to .ini file
        self.parser.edit_parser("treeview", "position", self.size_position_scale.get())

        ### Change whiteboard settings
        treeview.config_column_size('position', self.size_position_scale.get())


    #################################################################
    ############ Create "Category" column width options #############
    #################################################################
    def category_size(self):
        ### Save to .ini file
        self.parser.edit_parser("treeview", "category", self.size_category_scale.get())

        ### Change whiteboard settings
        treeview.config_column_size('category', self.size_category_scale.get())


    #################################################################
    ########## Create "Date rental" column width options ############
    #################################################################
    def date_rental_size(self):
        ### Save to .ini file
        self.parser.edit_parser("treeview", "date_rental", self.size_date_rental_scale.get())

        ### Change whiteboard settings
        treeview.config_column_size('date_rental', self.size_date_rental_scale.get())


    #################################################################
    ########## Create "Person rental" column width options ##########
    #################################################################
    def person_rental_size(self):
        ### Save to .ini file
        self.parser.edit_parser("treeview", "person_rental", self.size_person_rental_scale.get())

        ### Change whiteboard settings
        treeview.config_column_size('person_rental', self.size_person_rental_scale.get())


    #################################################################
    ############# Create "Other" column width options ###############
    #################################################################
    def other_size(self):
        ### Save to .ini file
        self.parser.edit_parser("treeview", "other", self.size_other_scale.get())

        ### Change whiteboard settings
        treeview.config_column_size('other', self.size_other_scale.get())


#################################################################
#############  ##############
#################################################################
if __name__ == '__main__':
    Size_tab()