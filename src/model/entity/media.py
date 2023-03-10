#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:09:59.330936
#+ Editado:	2023/02/27 20:39:01.776021
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, MediaType, MediaStatus
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class Media(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('Media'))
    name: str
    type_: MediaType
    status: MediaStatus
    year_start: int
    year_end: Optional[int] = field(default=None)
    active: Optional[int] = field(default=1)

    def __str__(self) -> str:
        string = f'{self.name}'
        if self.year_start:
            string += ' ({self.year_start})'
        return string
# ------------------------------------------------------------------------------
