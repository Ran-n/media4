#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/19 00:53:10.705486
#+ Editado:	2023/02/19 00:53:43.671020
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, Country
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CountryDescription(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CountryDescription'))
    desc: str
    country: Country
# ------------------------------------------------------------------------------
