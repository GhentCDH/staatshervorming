import csv
from csvReaders.readerTitels import ReaderTitels
from csvReaders.readerStudies import ReaderStudies
from csvReaders.readerPersonen import ReaderPersonen
from csvReaders.readerReferenties import ReaderReferenties
from csvReaders.readerAfkortingen import ReaderAfkortingen
from csvReaders.readerFuncties import ReaderFuncties
from csvReaders.readerFunctiesAndere import ReaderFunctiesAndere
from csvReaders.readerGeografisch import ReaderGeografisch
from csvReaders.readerLeekClericus import ReaderLeekClericus

from csvReaders.readerKwantificeerbaar import ReaderKwantificeerbaar

titels = ReaderTitels().read()
studies = ReaderStudies().read()
functies = ReaderFuncties().read()
functies_andere = ReaderFunctiesAndere().read()
leekclericus = ReaderLeekClericus().read()
geografisch = ReaderGeografisch().read()

kwantificeerbaar = ReaderKwantificeerbaar().read()

afkortingen = ReaderAfkortingen().read()
referenties = ReaderReferenties().read()

personen = ReaderPersonen().read()
