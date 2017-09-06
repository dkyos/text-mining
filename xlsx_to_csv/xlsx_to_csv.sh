#!/bin/bash

SRC=$1
DST=$2

if [ -z "$SRC" ] || [ -z "$DST" ]
then
    echo "No src or dst argument supplied"
    exit 0
fi

# Not using variable predefined $PWD
SPWD=`pwd`
echo "Current dir is [$SPWD]"

for dir in $(cat ./input.dir); 
    do
        echo "-------"
        cd $SPWD

        echo `pwd`
        cd $SRC/$dir

        for f in *.XLSX; 
            do 
                file_name=`basename $f .XLSX`
                mv $file_name.XLSX $file_name.xlsx
            done

        for f in *.xlsx; 
            do 
                file_name=`basename $f .xlsx`
                echo "Processing [$f] file.."; 
                echo "mkdir -p $SPWD/$DST/$dir"
                mkdir -p $SPWD/$DST/$dir

                #echo "ssconvert -O 'separator=| format=raw' ./$file_name.xlsx $SPWD/$DST/$dir/$file_name.txt"
                #ssconvert -O 'separator=| format=raw' ./$file_name.xlsx $SPWD/$DST/$dir/$file_name.txt
                #mv $SPWD/$DST/$dir/$file_name.txt $SPWD/$DST/$dir/$file_name.csv

                # ;(59), |(124) 
                libreoffice --headless --convert-to "csv:Text - txt - csv (StarCalc):124,,76,1" \
                    --outdir $SPWD/$DST/$dir/ \
                    ./$file_name.xlsx

            done
        echo `pwd`
    done

#options for libreoffice 124,,76,1 – these are four arguments:
# https://wiki.openoffice.org/wiki/Documentation/DevGuide/Spreadsheets/Filter_Options#Tokens_1_to_5
    #the first parameter is the delimiter in the output file – 124 is the ASCII code for '|'
    #the second parameter is the text delimiter – it's missing because I don't want to wrap text in quotes
    #the third parameter is the file encoding – 76 is the internal OpenOffice code for UTF-8 (from the table on the documentation page)
    #the fourth parameter defines the line number with which to start the export – here, we start with line 1




