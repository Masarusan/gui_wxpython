import os
import filecmp
import shutil
from Merge_resource import merge_resorce
import system_type


class file_backup(merge_resorce, system_type.os_type):
    def __init__(self, file_path, ostype):
        self.__file = file_path
        self.__change_fileslashed = super().system_pathchange(self.__file, os_type=ostype)
        self.backup(self.__change_fileslashed)

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

