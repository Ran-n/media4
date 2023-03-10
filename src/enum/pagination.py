#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/02/05 21:04:38.608054
#+ Editado:	2023/02/05 21:08:17.134558
# ------------------------------------------------------------------------------
from enum import Enum
# ------------------------------------------------------------------------------
class PaginationEnum(Enum):
    NEXT = '>'
    PREVIOUS = '<'
    OPTIONS = [NEXT, PREVIOUS]
# ------------------------------------------------------------------------------
