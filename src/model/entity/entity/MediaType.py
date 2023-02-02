#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:36:45.461301
#+ Editado:	2023/01/28 00:13:45.739578
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
import math
from typing import Optional, Union

from src.utils import Config
# ------------------------------------------------------------------------------
@dataclass
class MediaType:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('MediaType'))
    name: str
    groupable: Optional[int] = field(default=0)
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)

    """
    def __repr__(self) -> str:
        repeat = 1
        if len(self.name) < 6:
            repeat = 2
        return f'{self.name}' + repeat*'\t' + f'[{self.id_}]'
    """
# ------------------------------------------------------------------------------