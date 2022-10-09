from tkinter import *
from view.Treeview import treeview
from treebase import Parser


#################################################################
#############  ##############
#################################################################
class Size_tab:
    def __init__(self, root):
        row_treeview = Parser().get_parser('treeview', 'row')
        width_id = Parser().get_parser('treeview', 'id')
        width_title = Parser().get_parser('treeview', 'title')
        width_author = Parser().get_parser('treeview', 'author')
        width_position = Parser().get_parser('treeview', 'position')
        width_category = Parser().get_parser('treeview', 'category')
        width_date_rental = Parser().get_parser('treeview', 'date_rental')
        width_person_rental = Parser().get_parser('treeview', 'person_rental')
        width_other = Parser().get_parser('treeview', 'other')

        ###
        table_size = LabelFrame(root, text='Rozmiar Tablicy')
        table_size.pack(padx=10, pady=10)

        ###
        row_label = Label(table_size, text='Ilość wierszy')
        row_label.grid(row=0, column=0, padx=10, pady=5)
        self.row_scale = Scale(table_size, from_=0, to=20, orient=HORIZONTAL)
        self.row_scale.set(row_treeview)
        self.row_scale.grid(row=0, column=1, padx=10, pady=5)
        row_button = Button(table_size, text='Ustaw', command=self.row_size)
        row_button.grid(row=0, column=2, padx=10, pady=5)

        ###
        size_column = Label(table_size, text='Szerokość kolumn:')
        size_column.grid(row=1, column=0, padx=10, pady=(5,0))

        ###
        size_id_label = Label(table_size, text='ID:')
        size_id_label.grid(row=2, column=0, padx=10, pady=0)
        self.size_id_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_id_scale.set(width_id)
        self.size_id_scale.grid(row=2, column=1, padx=10, pady=0)
        size_id_button = Button(table_size, text='Ustaw', command=self.id_size)
        size_id_button.grid(row=2, column=2, padx=10, pady=0)

        ##
        size_title_label = Label(table_size, text='Nazwa Książki:')
        size_title_label.grid(row=3, column=0, padx=10, pady=0)
        self.size_title_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_title_scale.set(width_title)
        self.size_title_scale.grid(row=3, column=1, padx=10, pady=0)
        size_title_button = Button(table_size, text='Ustaw', command=self.title_size)
        size_title_button.grid(row=3, column=2, padx=10, pady=0)

        ###
        size_author_label = Label(table_size, text='Autor:')
        size_author_label.grid(row=4, column=0, padx=10, pady=0)
        self.size_author_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_author_scale.set(width_author)
        self.size_author_scale.grid(row=4, column=1, padx=10, pady=0)
        size_author_button = Button(table_size, text='Ustaw', command=self.author_size)
        size_author_button.grid(row=4, column=2, padx=10, pady=0)

        ###
        size_position_label = Label(table_size, text='Pozycja książki:')
        size_position_label.grid(row=5, column=0, padx=10, pady=0)
        self.size_position_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_position_scale.set(width_position)
        self.size_position_scale.grid(row=5, column=1, padx=10, pady=0)
        size_position_button = Button(table_size, text='Ustaw', command=self.position_size)
        size_position_button.grid(row=5, column=2, padx=10, pady=0)

        ###
        size_category_label = Label(table_size, text='Kategorie:')
        size_category_label.grid(row=6, column=0, padx=10, pady=0)
        self.size_category_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_category_scale.set(width_category)
        self.size_category_scale.grid(row=6, column=1, padx=10, pady=0)
        size_category_button = Button(table_size, text='Ustaw', command=self.category_size)
        size_category_button.grid(row=6, column=2, padx=10, pady=0)

        ###
        size_date_rental_label = Label(table_size, text='Data wypożyczenia:')
        size_date_rental_label.grid(row=7, column=0, padx=10, pady=0)
        self.size_date_rental_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_date_rental_scale.set(width_date_rental)
        self.size_date_rental_scale.grid(row=7, column=1, padx=10, pady=0)
        size_date_rental_button = Button(table_size, text='Ustaw', command=self.date_rental_size)
        size_date_rental_button.grid(row=7, column=2, padx=10, pady=0)

        ###
        size_person_rental_label = Label(table_size, text='Osoba wypożyczająca:')
        size_person_rental_label.grid(row=8, column=0, padx=10, pady=0)
        self.size_person_rental_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_person_rental_scale.set(width_person_rental)
        self.size_person_rental_scale.grid(row=8, column=1, padx=10, pady=0)
        size_person_rental_button = Button(table_size, text='Ustaw', command=self.person_rental_size)
        size_person_rental_button.grid(row=8, column=2, padx=10, pady=0)

        ###
        size_other_label = Label(table_size, text='Uwagi:')
        size_other_label.grid(row=9, column=0, padx=10, pady=0)
        self.size_other_scale = Scale(table_size, from_=0, to=400, orient=HORIZONTAL)
        self.size_other_scale.set(width_other)
        self.size_other_scale.grid(row=9, column=1, padx=10, pady=0)
        size_other_button = Button(table_size, text='Ustaw', command=self.other_size)
        size_other_button.grid(row=9, column=2, padx=10, pady=(0, 5))

        ###
        reset_size = Button(root, text='Reset rozmiaru tablicy', command=self.reset_sice_tab)
        reset_size.pack(padx=10, pady=5)


    #################################################################
    #############  ##############
    #################################################################
    def reset_sice_tab(self):
        ###
        parser = Parser()
        parser.edit_parser('treeview', 'row', parser.get_parser('treeview_copy', 'row'))
        parser.edit_parser('treeview', 'id', parser.get_parser('treeview_copy', 'id'))
        parser.edit_parser('treeview', 'title', parser.get_parser('treeview_copy', 'title'))
        parser.edit_parser('treeview', 'author', parser.get_parser('treeview_copy', 'author'))
        parser.edit_parser('treeview', 'position', parser.get_parser('treeview_copy', 'position'))
        parser.edit_parser('treeview', 'date_rental', parser.get_parser('treeview_copy', 'date_rental'))
        parser.edit_parser('treeview', 'person_rental', parser.get_parser('treeview_copy', 'person_rental'))
        parser.edit_parser('treeview', 'other', parser.get_parser('treeview_copy', 'other'))

        ###
        self.row_scale.set(parser.get_parser('treeview', 'row'))
        self.size_id_scale.set(parser.get_parser('treeview', 'id'))
        self.size_title_scale.set(parser.get_parser('treeview', 'title'))
        self.size_author_scale.set(parser.get_parser('treeview', 'author'))
        self.size_position_scale.set(parser.get_parser('treeview', 'position'))
        self.size_category_scale.set(parser.get_parser('treeview', 'category'))
        self.size_date_rental_scale.set(parser.get_parser('treeview', 'date_rental'))
        self.size_person_rental_scale.set(parser.get_parser('treeview', 'person_rental'))
        self.size_other_scale.set(parser.get_parser('treeview', 'other'))

        ###
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
    #############  ##############
    #################################################################
    def row_size(self):
        ###
        Parser().edit_parser("treeview", "row", self.row_scale.get())
        ###

        treeview.config_row_treeview(self.row_scale.get())

    #################################################################
    #############  ##############
    #################################################################
    def id_size(self):
        ###
        Parser().edit_parser("treeview", "id", self.size_id_scale.get())

        ###
        treeview.config_column_size("ID", self.size_id_scale.get())


    #################################################################
    #############  ##############
    #################################################################
    def title_size(self):
        ###
        Parser().edit_parser("treeview", "titile", self.size_title_scale.get())

        ###
        treeview.config_column_size('title', self.size_title_scale.get())

    #################################################################
    #############  ##############
    #################################################################
    def author_size(self):
        ###
        Parser().edit_parser("treeview", "author", self.size_author_scale.get())

        ###
        treeview.config_column_size('author', self.size_author_scale.get())

    #################################################################
    #############  ##############
    #################################################################
    def position_size(self):
        ###
        Parser().edit_parser("treeview", "position", self.size_position_scale.get())

        ###
        treeview.config_column_size('position', self.size_position_scale.get())

    #################################################################
    #############  ##############
    #################################################################
    def category_size(self):
        ###
        Parser().edit_parser("treeview", "category", self.size_category_scale.get())

        ###
        treeview.config_column_size('category', self.size_category_scale.get())

    #################################################################
    #############  ##############
    #################################################################
    def date_rental_size(self):
        ###
        Parser().edit_parser("treeview", "date_rental", self.size_date_rental_scale.get())

        ###
        treeview.config_column_size('date_rental', self.size_date_rental_scale.get())

    #################################################################
    #############  ##############
    #################################################################
    def person_rental_size(self):
        ###
        Parser().edit_parser("treeview", "person_rental", self.size_person_rental_scale.get())

        ###
        treeview.config_column_size('person_rental', self.size_person_rental_scale.get())

    #################################################################
    #############  ##############
    #################################################################
    def other_size(self):
        ###
        Parser().edit_parser("treeview", "other", self.size_other_scale.get())

        ###
        treeview.config_column_size('other', self.size_other_scale.get())


#################################################################
#############  ##############
#################################################################
if __name__ == '__main__':
    Size_tab()