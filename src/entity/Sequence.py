#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 19:03:40.041474
#+ Editado:	2023/01/20 17:43:22.566397
# ------------------------------------------------------------------------------
from dataclasses import dataclass, field
# ------------------------------------------------------------------------------
@dataclass
class Sequence:
    table_name: str = field(init=False, default='sqlite_sequence')
    name: str
    seq: int
# ------------------------------------------------------------------------------