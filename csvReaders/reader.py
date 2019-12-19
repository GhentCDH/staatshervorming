import csv
import re
import data

from .exceptions import InvalidRowException
from .exceptions import InvalidItemException

NULLABLE = ['', ' ', '?', 'n/a', '/', '0']

class Reader:

    def __init__(self, fileName, delimiter=','):
        self.fileName = fileName
        self.delimiter = delimiter

    def validateRow(self, row):
        pass

    def sanitizeRow(self, row):
        for i, cell in enumerate(row):
            # Don't clean ID column (would remove 99)
            if i == 0:
                continue

            if cell in NULLABLE:
                row[i] = None
        return row

    def createItemFromRow(self, row):
        pass

    def enrichItem(self, item, data):
        pass

    def postProcess(self, d):
        return d

    def printRowError(self, e, row):
        print()
        print('Invalid item: ' + str(e))
        print('    file: ' + self.fileName.split('/')[-1])
        print(row)

    def read(self):
        d = {}

        with open(self.fileName) as inputFile:
            inputReader = csv.reader(inputFile, delimiter=self.delimiter)

            # skip header row
            header = next(inputReader)

            # loop rows
            for row in inputReader:

                # Validate row
                try:
                    self.validateRow(row=row)
                except InvalidRowException as e:
                    self.printRowError(e, row)
                    continue

                # Get data from row
                row = self.sanitizeRow(row=row)
                try:
                    item = self.createItemFromRow(row=row)
                except InvalidItemException as e:
                    continue

                # enricht item
                self.enrichItem(item=item,data=data)

                # duplicate id?
                if item['id'] in d:
                    self.printRowError("duplicate id", row)
                    continue

                # add item
                d[item['id']] = item

            # post process dictionary
            d = self.postProcess(d=d)

        return d
