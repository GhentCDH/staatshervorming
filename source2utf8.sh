#!/bin/bash
pushd csv
for filename in $(find . -type f -name '*.txt'); do iconv -f ISO-8859-1 -t UTF8 $filename -o ${filename/.txt/_utf8.csv}; done
popd
