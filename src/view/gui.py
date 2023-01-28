#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/16 23:05:21.520132
#+ Editado:	2023/01/28 01:04:25.598772
# ------------------------------------------------------------------------------
from src.view.iview import iView
# ------------------------------------------------------------------------------
import customtkinter

from src.model.entity import Media
# ------------------------------------------------------------------------------
class GUI(iView):
    def __init__(self) -> None:
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk()
        self.root.geometry('800x500')
        self.root.mainloop()

    def menu(self, options: dict) -> int:
        pass

    def exit(self) -> None:
        pass

    def get_media(self) -> Media:
        pass
# ------------------------------------------------------------------------------
