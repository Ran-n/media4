#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 22:41:57.231414
#+ Editado:	2023/01/29 22:42:43.750060
# ------------------------------------------------------------------------------
#* Concrete Strategy (Strategy Pattern)
# ------------------------------------------------------------------------------
from src.view import iView
# ------------------------------------------------------------------------------
import logging
from typing import List, Union

from src.entity import Media, MediaType, MediaStatus
# ------------------------------------------------------------------------------
class Terminal(iView):

    model = None

    def __init__(self) -> None:
        logging.info(_('Starting Terminal view'))

        print('----------------------------------------')
        print(_('Media4 Manager'))
        print('----------------------------------------')

    def menu(self, options: dict) -> int:
        print()
        print('*** '+_('MENU')+' ***')

        for key, value in zip(options.keys(), options.values()):
            print(f'{key}. {value[0]}')

        while True:
            option = input(_('Pick: '))
            if option in options:
                break

        print('*** '+_('MENU')+' ***')
        print()

        return option

    def exit(self) -> None:
        print('----------------------------------------')

    @staticmethod
    def __pick_from_options(message_title: str, message: str, options: List[Union[MediaType, MediaStatus]]) -> Union[MediaType, MediaStatus]:
        while True:
            print(f'< {message_title}')
            for index, ele in enumerate(options):
                print(f'{index}. {ele.name}')
            choice = input(f'> {message}: ')

            if choice.isdigit():
                choice = int(choice)
            else:
                continue

            if (choice >= 0 and choice <= len(options)-1):
                value = options[choice]
                break
        return value

    def add_media(self) -> Media:
        print('** '+_('Add Media')+' **')
        # name
        name = input('> '+_('Name')+': ')
        print()

        # type_
        type_ = self.__pick_from_options(
                        message_title = _('Types'),
                        message = _('Type'),
                        options = self.model.get_all(MediaType.table_name)
        )
        print()

        # status
        status = self.__pick_from_options(
                        message_title = _('Statuses'),
                        message = _('Status'),
                        options = self.model.get_all(MediaStatus.table_name)
        )
        print()

        # year_start
        while True:
            year_start = input('> '+_('Start Year')+': ')
            if year_start.isdigit():
                break
        print()

        # year_end
        while True:
            year_end = input('> '+_('End Year')+': ')
            if year_end.isdigit():
                break
            elif year_end == '=':
                year_end = year_start
                break
        print('** '+_('Add Media')+' **')

        return Media(
                name = name,
                type_ = type_,
                status = status,
                year_start = year_start,
                year_end = year_end
        )

# ------------------------------------------------------------------------------

