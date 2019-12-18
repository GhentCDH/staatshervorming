from .reader import Reader
from .exceptions import InvalidRowException

class ReaderPersonen(Reader):

    def __init__(self):
        super().__init__(fileName='./data/naamdatatabel_utf8.csv',delimiter=';')

    def validateRow(self, row):
        pass

    def createItemFromRow(self, row):
        item = {
            'id': row[0],
            'familienaam': row[1],
            'voornaam': row[2],
            'code': row[3],
            'sociaal': row[4],
            'carrière': row[5],
            'bezit': row[6],
            'cultureel': row[7],
            'datum_geboorte': row[8],
            'datum_overlijden': row[9],
            'des': row[10]
        }

        return item

    def enrichItem(self, item, data):

        item['label'] = item['voornaam'] + ' ' + item['familienaam'];
        item['titels'] = [ v for (k,v) in data.titels.items() if v['persoon_id'] == item['id'] ];
        item['referenties'] = [ v for (k,v) in data.referenties.items() if v['persoon_id'] == item['id'] ];
