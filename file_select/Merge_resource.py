import pandas as pd
import cchardet
import os


class merge_resorce():
    def __init__(self, merge, ostype):
        self.__merge = merge
        self.__ostype = ostype
        if ostype == 0:
            self.__localization = "file_select\\csv_file"
        elif ostype == 1:
            self.__localization = "file_select\\csv_file".replace('\\', '/')
        self.merge(self.__localization, self.__merge)

    def get_localization(self):
        return self.__localization

    def set_localization(self, localization):
        self.__localization = localization

    def get_ostype(self):
        return self.__ostype

    #newFileCreate
    def merge(self, newcsv, oldcsv):
        self.__loca = pd.read_csv(newcsv)
        self.__mwegefile = pd.read_csv(oldcsv)
        merge_file = pd.merge(self.__loca, self.__mergefile)
        with open(self.get_localization() + os.path.basename(oldcsv), "w")as f:
            f.write(merge_file)

    #mergeOverride
    def merge_override(self):
        pass