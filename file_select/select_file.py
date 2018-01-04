import os
import filecmp
import shutil
from pathlib import Path
from Merge_resource import merge_resorce


class file_selector(merge_resorce):
    def __init__(self, file):
        self.__file = file
        self.backup(self.__file)

    def is_file(self, firstfile, secondfile):
        if filecmp.cmp(firstfile, secondfile):
            return True
        else:
            return False

    def backup(self, oldfile):
        #マージ前バックアップデータ
        backup = shutil.copy(oldfile,"file_select\\backup_file\\" + os.path.basename(oldfile))
        #shutil.move(file)
        print("BackUp_directory" + oldfile)
        print("CurrentDirectory:" + os.getcwd())

