#!/bin/bash

# git clone https://github.com/facebookresearch/fastText.git
# cd fastText
# make
# cd ..
# awk -F\| '{print $13}' ./pl_filtered_data.csv > comment.csv
# awk -F\| 'FNR > 1 {print $10}' ./*.csv > pl_comment.txt

./fastText/fasttext skipgram -input ./comment.csv -output pl_model -dim 100 -ws 3 -minCount 10 -verbose 2

./fastText/fasttext skipgram -input ./pl_comment.txt -output pl -dim 100 -ws 3 -minCount 5 -verbose 2

./fastText/fasttext skipgram -input ./de_comment.txt -output de -dim 100 -ws 3 -minCount 5 -verbose 2

