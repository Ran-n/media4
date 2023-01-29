#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:58:36.138946
#+ Editado:	2023/01/28 00:30:56.474895
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional, Union

from src.utils import Config
from src.model.entity import MediaName, Language
# ------------------------------------------------------------------------------
@dataclass
class MediaNameLanguage:
    table_name: str = field(init=False, repr=False, default=Config().get_table_name('MediaNameLanguage'))
    media_name: MediaName
    language: Language
    id_: Optional[int] = field(default=None)

    # table_name and id_ attributes are frozen
    def __setattr__(self, attr: str, value: Union[int, str]) -> None:
        if (attr != 'table_name'):
            object.__setattr__(self, attr, value)
# ------------------------------------------------------------------------------
