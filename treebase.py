from configparser import ConfigParser


#################################################################
    #############  ##############
    #################################################################
class Parser:
    def __init__(self):
        self.parser = ConfigParser()
        self.parser.read("treebase.ini")

    #################################################################
    #############  ##############
    #################################################################
    def edit_parser(self, name, name_row, value):
        self.parser.set(name, name_row, str(value))
        with open("treebase.ini", "w") as configfile:
            self.parser.write(configfile)

    #################################################################
    #############  ##############
    #################################################################
    def get_parser(self, name, name_row):
        return self.parser.get(name, name_row)

    