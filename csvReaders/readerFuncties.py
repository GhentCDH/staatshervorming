from .reader import Reader
from .exceptions import InvalidRowException


class ReaderFuncties(Reader):

    def __init__(self):
        super().__init__(fileName='./data/functies_utf8.csv',delimiter=";")

    def validateRow(self, row):
        return

    def createItemFromRow(self, row):
        item = {
            'id': row[1],
            'label': row[2],
        }

        return item

    def enrichItem(self, item, data):
        return
