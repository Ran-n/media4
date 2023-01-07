#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/05 21:26:41.185113
#+ Editado:	2023/01/07 01:33:36.252156
# ------------------------------------------------------------------------------
#* Concrete Strategy (Strategy Pattern)
# ------------------------------------------------------------------------------
import src.db.idb as idb

import sqlite3
from sqlite3 import Connection, Cursor

from typing import List, Tuple, Union

from src.dtos.MediaTipo import MediaTipo
from src.dtos.MediaSituacion import MediaSituacion
from src.dtos.Almacen import Almacen
from src.dtos.NomeCarpeta import NomeCarpeta
from src.dtos.Secuencia import Secuencia
# ------------------------------------------------------------------------------
class Sqlite(idb.DB):
    def __init__(self, ficheiro: str) -> None:
        self.ficheiro = ficheiro
        self.conn = None
        self.cur = None

    def get_conn(self) -> Connection:
        if self.conn == None:
            return self.conectar()[0]
        return self.con

    def get_cur(self) -> Cursor:
        if self.cur == None:
            return self.conectar()[1]
        return self.cur

    def conectar(self) -> tuple([Connection, Cursor]):
        self.conn = sqlite3.connect(self.ficheiro)
        self.cur = self.conn.cursor()
        return (self.conn, self.cur)

    def desconectar(self, commit: bool = True) -> None:
        if self.conn:
            if commit:
                self.conn.commit()
            self.conn.close()
            self.conn = None
            self.cur = None

    def select_tipos(self) -> List[MediaTipo]:
        results = self.get_cur().execute(f'select ID, Nome from "_Media Tipo"').fetchall()
        valores = []
        for result in results:
            valores.append(MediaTipo(id_=result[0], nome=result[1]))
        return valores

    def select_situacions(self) -> List[MediaSituacion]:
        results = self.get_cur().execute(f'select ID, Nome from "_Media Situación"').fetchall()
        valores = []
        for result in results:
            valores.append(MediaTipo(id_=result[0], nome=result[1]))
        return valores

    def select_almacens(self) -> List[Almacen]:
        results = self.get_cur().execute(f'select ID, Nome from "_Almacén"').fetchall()
        valores = []
        for result in results:
            valores.append(Almacen(id_=result[0], nome=result[1]))
        return valores

    def select_carpetas(self) -> List[NomeCarpeta]:
        results = self.get_cur().execute(f'select ID, Nome from "Nome Carpeta"').fetchall()
        valores = []
        for result in results:
            valores.append(NomeCarpeta(id_=result[0], nome=result[1]))
        return valores

    def select_secuencias(self) -> List[Secuencia]:
        results = self.get_cur().execute(f'select name, seq from "sqlite_sequence"').fetchall()
        valores = []
        for result in results:
            valores.append(Secuencia(nome=result[0], seq=result[1]))
        return valores

    def select(self, elemento: object) -> List[object]:
        return ['a', 'b']
# ------------------------------------------------------------------------------
