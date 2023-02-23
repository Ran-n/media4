#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/23 17:17:21.124687
#+ Editado:	2023/02/23 17:17:49.152586
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, AppVersion
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class AppVersionDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('AppVersionDescription'))
    desc: str
    app_version: AppVersion
# ------------------------------------------------------------------------------
