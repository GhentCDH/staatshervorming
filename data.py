import csv
from csvReaders.readerTitels import ReaderTitels
from csvReaders.readerStudies import ReaderStudies
from csvReaders.readerPersonen import ReaderPersonen
from csvReaders.readerReferenties import ReaderReferenties
from csvReaders.readerAfkortingen import ReaderAfkortingen
from csvReaders.readerKwantificeerbaar import ReaderKwantificeerbaar


#studies = read_studies()
titels = ReaderTitels().read()
studies = ReaderStudies().read()
afkortingen = ReaderAfkortingen().read()
referenties = ReaderReferenties().read()
kwantificeerbaar = ReaderKwantificeerbaar.read()

personen = ReaderPersonen().read()
