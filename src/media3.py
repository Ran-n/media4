#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:17:25.456829
#+ Editado:	2023/01/09 23:36:03.233794
# ------------------------------------------------------------------------------
from uteis.ficheiro import cargarJson

from src.model.db import DB
from src.model.sqlite import Sqlite
from src.controller.sair import sair
from src.controller.insertar import insertar

from src.uteis import print_fin

from src.dtos.Media import Media
from src.dtos.MediaAgrupacion import MediaAgrupacion
# ------------------------------------------------------------------------------
def print_inicio():
    print('----------------------------------------')
    print('Media3 Manager')
    print('----------------------------------------')
# ------------------------------------------------------------------------------
def opcions_menu(opcions: dict) -> int:
    print('\n*** MENÚ ***')

    for chave, valor in zip(opcions.keys(), opcions.values()):
        print(f'{chave}. {valor[0]}')

    while True:
        opcion = input('Escolla: ')
        if opcion in opcions:
            break
    print('*** MENÚ ***\n')
    return opcion

def menu(db: DB):
    opcions = {
            '0': ['Sair', sair],
            '1': ['Insertar', insertar],
    }

    opcions[opcions_menu(opcions)][1](db)

# ------------------------------------------------------------------------------
def main():
    cnf = cargarJson('.cnf')
    db = DB(Sqlite(cnf['db']))

    print_inicio()

    while True:
        menu(db)

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
# ------------------------------------------------------------------------------
