#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/16 23:05:21.520132
#+ Editado:	2023/02/26 19:37:08.125633
# ------------------------------------------------------------------------------
from src.view import iView
# ------------------------------------------------------------------------------
import logging
import customtkinter

from src.model.entity import Media, MediaGroup, MediaIssue
from src.model.entity import MediaType, MediaStatus
from src.model.entity import Platform, ShareSiteType, ShareSite
from src.model.entity import WarehouseType, Warehouse
# ------------------------------------------------------------------------------
class CustomTKinter(iView):
    def __init__(self) -> None:
        logging.info(_('Starting GUI view'))
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk()

    def start(self) -> None:
        self.root.geometry('800x500')
        self.root.mainloop()

    def save(self) -> None:
        pass

    def exit(self) -> None:
        # nothing need to be done here
        pass

    def update_member_count(self) -> None:
        """
        """
        pass

    def add_media_type(self) -> MediaType:
        pass

    def add_media_status(self) -> MediaStatus:
        pass


    def add_media(self) -> Media:
        pass

    def add_media_group(self) -> MediaGroup:
        pass

    def add_media_issue(self) -> MediaIssue:
        pass

    def add_platform(self) -> Platform:
        pass

    def add_sharesite_type(self) -> Platform:
        """
        """
        pass

    def add_sharesite_type(self) -> ShareSiteType:
        """
        """
        pass

    def add_sharesite(self) -> ShareSite:
        """
        """
        pass

    def add_warehouse_type(self) -> WarehouseType:
        """
        """
        pass

    def add_warehouse(self) -> Warehouse:
        """
        """
        pass

    def add_file(self) -> str:
        """
        """
        pass

# ------------------------------------------------------------------------------
