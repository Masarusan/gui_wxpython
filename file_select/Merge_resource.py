import pandas as pd
import cchardet
import os


class merge_resorce():
    def __init__(self, merge):
        self.__merge = merge
        self.__localization = "C:\\Users\\tobar\\PycharmProjects\\untitled\\gui_wxpython\\file_select\\csv_file"
        self.merge(self.__localization, self.__merge)

    def get_localization(self):
        return self.__localization

    def set_localization(self, localization):
        self.__localization = localization

    #newFileCreate
    def merge(self, newcsv, oldcsv):
        self.__loca = pd.read_csv(newcsv)
        self.__mwegefile = pd.read_csv(oldcsv)
        merge_file = pd.merge(self.__loca, self.__mergefile)
        with open("file_select\\merge_file\\" + os.path.basename(oldcsv), "w")as f:
            f.write(merge_file)

    #mergeOverride
    def merge_override(self):
        pass