from webbrowser import open_new
from tkinter import *

class Info:
    def __init__(self, root):
        ###
        info_labelframe = LabelFrame(root, text='Informacje o aplikacji')
        info_labelframe.pack(padx=10, pady=10)

        ###
        info_label = Label(info_labelframe, text='Informacje', font=("Arial", 32))
        info_label.pack(padx=10, pady=10)

        info_box = Frame(info_labelframe)
        info_box.pack(padx=10, pady=10)

        ###
        name_label_key = Label(info_box, text='Nazwa aplikacji:')
        name_label_value = Label(info_box, text='Biblioteka Książek')
        version_label_key = Label(info_box, text='Wersja:')
        version_label_value = Label(info_box, text='0.1.2 (BETA)')
        creator_app_key = Label(info_box, text='Twórca programu:')
        creator_app_value = Label(info_box, text='Adam Golewski', fg="blue")
        program_created_from_key = Label(info_box, text='Program stworzony dla:')
        program_created_from_value = Label(info_box, text='Biblioteka Hufca ZHP Pabianice')
        langauage_creates_program_key = Label(info_box, text='Język programu:')
        langauage_creates_program_value = Label(info_box, text='Python 3.x')
        library_gui_key = Label(info_box, text='Silnik GUI')
        library_gui_value = Label(info_box, text='Tkinter', fg='blue')
        library_database_key = Label(info_box, text='Baza danych:')
        library_database_value = Label(info_box, text='SQLite')

        ###
        name_label_key.grid(row=0, column=0, padx=10, pady=0)
        name_label_value.grid(row=0, column=1, padx=10, pady=0)
        version_label_key.grid(row=1, column=0, padx=10, pady=0)
        version_label_value.grid(row=1, column=1, padx=10, pady=0)
        creator_app_key.grid(row=2, column=0, padx=10, pady=0)
        creator_app_value.grid(row=2, column=1, padx=10, pady=0)
        program_created_from_key.grid(row=3, column=0, padx=10, pady=0)
        program_created_from_value.grid(row=3, column=1, padx=10, pady=0)
        langauage_creates_program_key.grid(row=4, column=0, padx=10, pady=(30,0))
        langauage_creates_program_value.grid(row=4, column=1, padx=10, pady=(30,0))
        library_gui_key.grid(row=5, column=0, padx=10, pady=0)
        library_gui_value.grid(row=5, column=1, padx=10, pady=0)
        library_database_key.grid(row=6, column=0, padx=10, pady=0)
        library_database_value.grid(row=6, column=1, padx=10, pady=0)

        ###
        creator_app_value.bind("<Button-1>", lambda e: self.callback("https://www.facebook.com/Ad7siem"))
        library_gui_value.bind("<Button-1>", lambda e: self.callback("https://docs.python.org/3/library/tkinter.html"))


    def callback(self, url):
        open_new(url)


if __name__ == "__main__":
    Info()