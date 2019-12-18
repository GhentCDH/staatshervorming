from .reader import Reader
from .exceptions import InvalidRowException


class ReaderStudies(Reader):

    def __init__(self):
        super().__init__(fileName='./data/kwantificeerbaar_utf8.csv',delimiter=";")

    def validateRow(self, row):
        return

    def createItemFromRow(self, row):
        "Id";"naamid";"Carrierebegin";"Carriereeind";"FunctieRVVRK";"Functieandere1";"Functieandere2";"Origine";"Sociaal";"LeekClericus";"Studies";"Netwerk";"Verwant";"Nepotisme"
        item = {
            'id': row[0],
            'persoon_id': row[1],
            'carriere_begin': row[2],
            'carriere_begin': row[3],
            'functie_rvvrk': row[4],
            'functie_andere1': row[5],
            'functie_andere2': row[6],
            'functie_andere2': row[7],
            'origine': row[8],
            'sociaal': row[9],
            'studies': row[10],
            'netwerk': row[11],
            'verwant': row[12],
            'nepotisme': row[13]
        }

        return item

    def enrichItem(self, item, data):
        return
