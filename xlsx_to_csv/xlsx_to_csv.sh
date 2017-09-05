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

        for f in *.xlsx; 
            do 
                file_name=`basename $f .xlsx`
                echo "Processing [$f] file.."; 
                echo "mkdir -p $SPWD/$DST/$dir"
                mkdir -p $SPWD/$DST/$dir
                echo "ssconvert -O 'separator=| format=raw' ./$file_name.xlsx $SPWD/$DST/$dir/$file_name.txt"
                ssconvert -O 'separator=| format=raw' ./$file_name.xlsx $SPWD/$DST/$dir/$file_name.txt
                mv $SPWD/$DST/$dir/$file_name.txt $SPWD/$DST/$dir/$file_name.csv
            done
        echo `pwd`
    done



