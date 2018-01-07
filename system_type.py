# -*- coding: utf-8 -*-
#!/usr/bin/python3
import platform
import os
import mainprogress


class os_type:
    def __init__(self, path):
        self.os_type()
        self.__path = path
        self.system_pathchange(self.__path, self.os_type())

    def os_type(self):
        system_os = platform.system()
        os_ver = 'OS:'
        if system_os == 'Windows':
            print(os_ver + system_os)
            return 0
        elif system_os == 'Darwin':
            print(os_ver + system_os)
            return 1
        elif system_os == 'Linux':
            print(os_ver + system_os)
            return 2
        else:
            print(system_os)

    def system_pathchange(self, path, os_type):
        print(path)
        originalpath = os.getcwd()
        print(originalpath)
        if os_type == 0:
            slashed_path = path.replace(os.path.sep, '\\')
            return slashed_path

        elif os_type == 1:
            slashed_path = path.replace('/', os.sep)
            return slashed_path

