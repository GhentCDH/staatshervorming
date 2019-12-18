from .reader import Reader
from .exceptions import InvalidRowException


class ReaderTitels(Reader):

    def __init__(self):
        super().__init__(fileName='./data/titeltabel_utf8.csv',delimiter=';')

    def validateRow(self, row):
        if row is None:
            raise InvalidRowException('row')

        if not row[1]:
            raise InvalidRowException('empty title')


    def createItemFromRow(self, row):
        item = {
            'id': row[0],
            'label': row[1],
            'persoon_id': row[2]
        }

        return item

    def enrichItem(self, item, data):
        return
