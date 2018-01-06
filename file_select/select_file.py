import os
import filecmp
import shutil
from pathlib import Path
from Merge_resource import merge_resorce


class file_selector(merge_resorce):
    def __init__(self, file, ostype):
        self.__file = file
        if ostype == 0:
            self.__selectfile = "file_select/backup_file/".replace('/', '¥¥')
        elif ostype == 1:
            self.__selectfile = "file_select/backup_file"
        self.backup(self.__file)

    def is_file(self, firstfile, secondfile):
        if filecmp.cmp(firstfile, secondfile):
            return True
        else:
            return False

    def backup(self, oldfile):
        #マージ前バックアップデータ
        backup = shutil.copy(oldfile,'file_select/backup_file/' + os.path.basename(oldfile))
        #shutil.move(file)
        print("BackUpForm_directory" + oldfile)
        print("CurrentDirectory:" + os.getcwd())

