from .reader import Reader
from .exceptions import InvalidRowException


class ReaderStudies(Reader):

    def __init__(self):
        super().__init__(fileName='./data/studies_utf8.csv',delimiter=";")

    def validateRow(self, row):
        return

    def createItemFromRow(self, row):
        item = {
            'id': row[1],
            'label': row[2] or row[1],
        }

        return item

    def enrichItem(self, item, data):
        return
