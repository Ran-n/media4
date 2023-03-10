#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:40:21.798484
#+ Editado:	2023/02/26 19:37:03.748630
# ------------------------------------------------------------------------------
#* Context Class (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.view import iView
# ------------------------------------------------------------------------------
from src.model import iModel
# ------------------------------------------------------------------------------
from src.exception import InheritException

from src.model.entity import Media, MediaGroup, MediaIssue
from src.model.entity import MediaType, MediaStatus
from src.model.entity import Platform, ShareSiteType, ShareSite
from src.model.entity import WarehouseType, Warehouse
# ------------------------------------------------------------------------------
class View:
    def __init__(self, strategy: iView, model: iModel) -> None:
        # demand the use of an intance of view
        if isinstance(strategy, iView):
            self.strategy = strategy

            self.model = model
            self.strategy.model = model

            self.controller = None
        else:
            raise InheritException(_(f'Must inherit from {iView.__name__}'))

    def start(self) -> None:
        return self.strategy.start()

    def save(self) -> None:
        return self.strategy.save()

    def exit(self) -> None:
        self.strategy.exit()

    def update_member_count(self) -> None:
        """
        """
        self.strategy.update_member_count()


    def add_media_type(self) -> MediaType:
        return self.strategy.add_media_type()

    def add_media_status(self) -> MediaStatus:
        return self.strategy.add_media_status()

    def add_media(self) -> Media:
        return self.strategy.add_media()

    def add_media_group(self, id_media: int = None) -> MediaGroup:
        return self.strategy.add_media_group(id_media= id_media)

    def add_media_issue(self) -> MediaIssue:
        return self.strategy.add_media_issue()

    def add_platform(self) -> Platform:
        return self.strategy.add_platform()

    def add_sharesite_type(self) -> ShareSiteType:
        return self.strategy.add_sharesite_type()

    def add_sharesite(self) -> ShareSite:
        return self.strategy.add_sharesite()

    def add_warehouse_type(self) -> WarehouseType:
        return self.strategy.add_warehouse_type()

    def add_warehouse(self) -> Warehouse:
        return self.strategy.add_warehouse()

    def add_file(self) -> str:
        return self.strategy.add_file()
# ------------------------------------------------------------------------------
