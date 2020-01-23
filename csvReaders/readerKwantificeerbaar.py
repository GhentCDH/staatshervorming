# -*- coding: utf-8 -*-
from .reader import Reader
from .exceptions import InvalidRowException


class ReaderKwantificeerbaar(Reader):

    def __init__(self):
        super().__init__(fileName='./data/kwantificeerbaar_utf8.csv',delimiter=";")

    def validateRow(self, row):

        return

    def createItemFromRow(self, row):
        item = {
            'id': row[1],
            'persoon_id': row[1],
            'carrière_begin': row[2],
            'carrière_einde': row[3],
            'functie': row[4],
            'functie_andere': [ row[5], row [6] ],
            'origine': row[7],
            'sociaal': row[8],
            'leek_clericus': row[9],
            'studies': row[10],
            'netwerk': row[11],
            'verwant': row[12],
            'nepotisme': row[13]
        }

        return item

    def enrichItem(self, item, data):

        if item['studies']:
            key = item['studies']
            item['studies'] = data.studies[key]['label'] if key in data.studies else key

        if item['functie']:
            key = item['functie']
            item['functie'] = data.functies[key]['label'] if key in data.functies else key

        if item['functie_andere']:
            item['functie_andere'] = [ data.functies[v] for v in item['functie_andere'] if v in data.functies ]

        if item['leek_clericus']:
            key = item['leek_clericus']
            item['leek_clericus'] = data.leekclericus[key]['label'] if key in data.leekclericus else key

        if item['origine']:
            key = item['origine']
            item['origine'] = data.geografisch[key]['label'] if key in data.geografisch else key

        return
