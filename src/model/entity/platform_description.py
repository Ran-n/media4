#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/13 22:20:32.532650
#+ Editado:	2023/02/24 21:19:55.904403
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Platform
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class PlatformDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('PlatformDescription'))
    desc: str
    platform: Platform
    active: Optional[int] = field(default=1)
# ------------------------------------------------------------------------------
