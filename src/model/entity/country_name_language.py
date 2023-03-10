#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/01 21:21:01.942449
#+ Editado:	2023/02/17 20:36:24.251290
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field

from src.utils import Config
from src.model.entity import BaseEntity, CountryName, Language
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class CountryNameLanguage(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('CountryNameLanguage'))
    country_name: CountryName
    language: Language
# ------------------------------------------------------------------------------
