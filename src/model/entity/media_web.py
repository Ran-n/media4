#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 00:06:39.547649
#+ Editado:	2023/02/17 20:38:28.365465
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional

from src.utils import Config
from src.model.entity import BaseEntity, Media, Web
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
@dataclass
class MediaWeb(BaseEntity):
    """Entity Object"""
    table_name: str = field(init=False, repr=False,
                            default=Config().get_table_name('MediaWeb'))
    media: Media
    web: Web
    link: str
    active: Optional[str] = field(default=1)
# ------------------------------------------------------------------------------
