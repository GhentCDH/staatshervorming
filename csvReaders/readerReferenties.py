from .reader import Reader
from .exceptions import InvalidRowException
import re


class ReaderReferenties(Reader):

    def __init__(self):
        super().__init__(fileName='./data/reftabel_utf8.csv',delimiter=";")

    def validateRow(self, row):
        if len([v for v in row if v]) != 3:
            raise InvalidRowException('row count invalid')

        return

    def createItemFromRow(self, row):
        item = {
            'id': row[0],
            'label': row[1],
            'persoon_id': row[2],
        }

        return item

    def enrichItem(self, item, data):
        item['fullref'] = item['label']
        for afk_key, afk_item in data.afkortingen.items():
            if '[nummer]' not in afk_key:
                pattern = '^(' + re.escape(afk_key) + '([, ]|$))'
                # print(pattern)
            else:
                pattern = '^(' + re.escape(afk_key) + ')'
                pattern = pattern.replace(re.escape(', [folio]'),'')
                pattern = pattern.replace(re.escape(' [nummer]'),'([ ]?[0-9]{1,5}(\-[0-9]{1,5})?([, ]|$))')
                pattern = pattern.replace(re.escape('[nummer]'),'([0-9]{1,5}(\-[0-9]{1,5})?([, ]|$))')

            if re.search(pattern,item['label']):
                item['fullref'] = re.sub(pattern,r''+ afk_item['label'] + r': \2',item['label'])
                break


        # parts = item['label'].split(', ')
        # if parts[0] in data.afkortingen:
        #     item['fullref'] = data.afkortingen[parts[0]]['label'] + ': ' + ', '.join(str(v) for v in parts[1:])
