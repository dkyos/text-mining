#!/bin/bash

# git clone https://github.com/facebookresearch/fastText.git
# cd fastText
# make
# cd ..
# awk -F\| '{print $13}' ./pl_filtered_data.csv > comment.csv

./fastText/fasttext skipgram -input ./comment.csv -output pl_model -dim 100 -ws 3 -minCount 10 -verbose 2

