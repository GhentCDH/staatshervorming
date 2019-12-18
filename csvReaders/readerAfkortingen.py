from .reader import Reader
from .exceptions import InvalidRowException


class ReaderAfkortingen(Reader):

    def __init__(self):
        super().__init__(fileName='./data/afkortingen_utf8.csv',delimiter=";")

    def validateRow(self, row):
        return

    def createItemFromRow(self, row):
        item = {
            'id': row[1],
            'label': row[2].rstrip('.')
        }

        return item

    def enrichItem(self, item, data):
        return

    def postProcess(self, d):

        # fix missing shortcodes
        d['AS[nummer]'] = d['AS']
        d['RK[nummer]'] = d['RK']

        # order dictionary
        l = list(d.items())
        l = sorted(l,key=self.keyLength, reverse=True)
        d = dict(l)
        return d

    def keyLength(self, x):
        return len(x[0])
