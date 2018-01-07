# -*- coding: utf-8 -*-
#!/usr/bin/python3
import system_type


class typetest(system_type.os_type):
    def __init__(self, path):
        super().__init__(path=path)


if __name__ == "__main__":
    tp = typetest('/Users/masaru/PycharmProjects/Pygame_plactice/wxpython_gui/gui_wxpython/ハサミのフリーアイコン.png')
    #tp.system_pathchange('/Users/masaru/PycharmProjects/Pygame_plactice/wxpython_gui/gui_wxpython/ハサミのフリーアイコン.png')
