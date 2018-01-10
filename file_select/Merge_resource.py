import pandas as pd
import cchardet
import os
import system_type
import glob


class merge_resorce(system_type.os_type):
    def __init__(self, merge):
        self.__merge = merge
        self.__merge_file = None
        self.__chardet = None
        self.__localization = "csv_file/dummy (1).csv"
        file = glob.glob('csv_file/*.csv')
        self.encoding(file)
        #self.__checked_csv = super().__init__(self.read_csv(self.__merge, self.__localization))#OSによってファイルパス変換
        #self.merge(self.__localization, self.__checked_csv)



    def get_localization(self):
        return self.__localization

    def set_localization(self, localization):
        self.__localization = localization

    def get_ostype(self):
        return self.__ostype

    def get_chardet(self):
        return self.__chardet

    def set_chardet(self, char):
        self.__chardet = char

    encode = property(get_chardet, set_chardet)

    def encoding(self, csv_file):
        print(csv_file)
        for i in csv_file:
            with open(i, 'rb')as f:
                readfile = f.read()
                char = cchardet.detect(readfile)
                print('{0}:{1}'.format(i, char))
                #print(char['encoding'])
        return char['encoding']

    def print_csv(self, csv_file):
        with open(csv_file, 'r', encoding=self.encode)as f:
            readfile = f.read()
            print(readfile)
        return

    #readcsv, forchar
    def read_csv(self, *merge):
        with open(os.fspath(merge), 'rb')as f:
            file = f.read()
            char = cchardet.detect(file)
            self.encode = char
            print(self.__chardet)
            pd.set_option('display.width', 1000)
            df = pd.read_csv(merge, encoding=self.__chardet['encoding'])
            print(df)
            return df

    #newFileCreate_merge
    def merge(self, new_csv, old_csv):
        self.__loca = pd.read_csv(new_csv)
        self.__merge_file = pd.read_csv(old_csv)
        merge_file = pd.merge(self.__loca, self.__merge_file, on=['名前', 'ふりがな', 'アドレス', '性別', '年齢', '誕生日',
                                                                  '婚姻', '都道府県', '携帯', 'キャリア', 'カレーの食べ方'])
        with open("merge_file/test.csv", "w", encoding=self.encode)as f:
            new_data = f.write(merge_file)
            print(new_data)

    #mergeOverride
    def merge_override(self):
        pass