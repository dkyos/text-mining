#!/usr/bin/env python

# from http://shichaoji.com/2017/02/25/topicmodeling/

import pandas as pd
from helper import *
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import pprint
import numpy as np

DOC_FILE = "data.txt"

stopwords = set(stopwords.words('english'))
stopwords.update(['.', ',', '"', "'", '?', '!', ':', ';', '('    , ')', '[', ']', '{', '}']) # remove it if you need punctuation
punctuation = set(string.punctuation)
lemmatize = WordNetLemmatizer()

def cleaning(article):
    one = " ".join([i for i in article.lower().split() if i not in stopwords])
    two = "".join(i for i in one if i not in punctuation)
    three = " ".join(lemmatize.lemmatize(i) for i in two.split())
    four = "".join(i for i in three if not i[0].isdigit() )
    return four 

df = pd.read_table(DOC_FILE, names=['text'], encoding = 'utf8')
#df.info()
#df.head(3)

text = df.applymap(cleaning)['text']
text_train= [i for i in text]
print (len(text_train))

from sklearn.feature_extraction.text import CountVectorizer

#vect = CountVectorizer(min_df=3).fit(text_train)
vect = CountVectorizer(min_df=3, ngram_range=(1,3)).fit(text_train)
X = vect.transform(text_train)

word_freq_df = pd.DataFrame({'term': vect.get_feature_names(), 'occurrences':np.asarray(X.sum(axis=0)).ravel().tolist()})
word_freq_df['frequency'] = word_freq_df['occurrences']/np.sum(word_freq_df['occurrences'])
#print (word_freq_df.sort('occurrences',ascending = False).head())
print (word_freq_df.sort('occurrences',ascending = False))

#print("X:\n{}".format(repr(X)))
#feature_names = vect.get_feature_names()
#print("특성 개수: {}".format(len(feature_names)))
#print("처음 20개 특성:\n{}".format(feature_names[:20]))


