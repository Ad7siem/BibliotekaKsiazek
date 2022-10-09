from tkinter import *
from tkinter import filedialog
from view.Menu.auxialiary import settings_deiconify
from treebase import Parser


#################################################################
#############  ##############
#################################################################
class Setting_database:
    def __init__(self, root):
        ###
        self.database_directory = Parser().get_parser('database', 'directory')
        self.database_directory_copy = Parser().get_parser('database', 'directory_copy')

        ###
        settings = LabelFrame(root, text='Ustawienia bazy danych')
        settings.pack(padx=10, pady=10)

        ###
        link_database_label = Label(settings, text='Folder zapisu pliku')
        link_database_label.grid(row=0, column=0, padx=10, pady=5)
        link_database_button = Button(settings, text='Wybierz', command=self.open_dir_to_database)
        link_database_button.grid(row=0, column=1, padx=10, pady=5)
        self.link_database_entry = Entry(settings, width=40)
        self.link_database_entry.insert(0, self.database_directory)
        self.link_database_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        ###
        link_database_copy_label = Label(settings, text='Folder zapisu pliku zapasowego')
        link_database_copy_label.grid(row=2, column=0, padx=10, pady=(10, 5))
        link_database_copy_button = Button(settings, text="Wybierz", command=self.open_dir_to_database_copy)
        link_database_copy_button.grid(row=2, column=1, padx=10, pady=5)
        self.link_database_copy_entry = Entry(settings, width=40)
        self.link_database_copy_entry.insert(0, self.database_directory_copy)
        self.link_database_copy_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    #################################################################
    #############  ##############
    #################################################################
    def open_dir_to_database(self):
        self.link_database_entry.delete(0, END)
        self.link_database_entry.insert(0, self.open_dir('directory'))


    #################################################################
    #############  ##############
    #################################################################
    def open_dir_to_database_copy(self):
        self.link_database_copy_entry.delete(0, END)
        self.link_database_copy_entry.insert(0, self.open_dir('directory_copy'))


    #################################################################
    #############  ##############
    #################################################################
    def open_dir(self, name):
        database_directory = filedialog.askdirectory(initialdir='./')

        if database_directory:
            Parser().edit_parser("database", name, database_directory)

        settings_deiconify()
        return database_directory


if __name__ == '__main__':
    Setting_database()