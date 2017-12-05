#!/usr/bin/env python
# coding: utf-8

import csv
import pandas as pd
import numpy as np
from matplotlib import rcParams
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict
import networkx as nx
from datetime import datetime
from PIL import Image
from os import path
import matplotlib.patches as mpatches
import random

#get_ipython().magic('matplotlib inline')
sns.set(style="whitegrid", palette="colorblind", color_codes=True, font_scale=1.4,
        rc = {'font.size': 12, 'font.family':'NanumGothic'})


# * 사용될 색상 팔렛트
col_pal = "#FF5254 #5CACC4 #CEE879 #8CD19D #FCB653 #11644D #1D1313 #5F0D3B #FF7D10".split()
sns.palplot(col_pal)


# ---
# ## 데이터 준비


load_cols = ['product_id', 'item_id', 'vendor_item_id', 'product_info'
            , 'date', 'rating', 'member_id', 'review_content']

review_ds = pd.read_csv("./resource/Electric_Heater.csv" 
      , sep='|'
      , usecols = load_cols
      , error_bad_lines=False
      , quoting=csv.QUOTE_NONE
      , encoding='utf-8')
#print(" - " + str(review_ds.shape) + "\n")
#print (review_ds.head())

# 혼합된 데이터 타입 변환 
review_ds = review_ds.astype(str)

# timestamp type을 datetime으로 변환하자 
def str2datetime(s):
    return datetime.strptime( s.replace('오후','pm').replace('오전','am'),  '%Y.%m.%d' )

#print (review_ds[pd.to_datetime(review_ds['date'], errors='coerce').isnull()])

review_ds['timestamp'] = review_ds['date'].apply( str2datetime ) 

# timestamp date, time으로 분리해서 처리하자 
review_ds['date'] = review_ds['timestamp'].apply(datetime.date)
#print (review_ds.head())

# 분석을 쉽게하는 필드 추가 
review_ds['year_days'] = review_ds['timestamp'].apply(lambda x : (x-datetime(x.year,1,1)).days)
review_ds['days'] = review_ds['timestamp'].apply(lambda x : (x-datetime(2012,1,1)).days)
review_ds['total'] = 'total'
review_ds['year'] = review_ds['timestamp'].apply(lambda x : (x.year))
review_ds['month'] = review_ds['timestamp'].apply(lambda x : (x.month))
#print (review_ds.head())

# initialize index 
review_ds = review_ds.sort_values('timestamp').reset_index(drop=True)
#print (review_ds.head())

# ---
# ## 1. Stat 탐색
daily_stats = review_ds.groupby('date').agg({'review_content':len}).describe()
print(u'하루에 평균 %.1f 건' % (daily_stats.loc['mean']))
print(u'하루에 최대 %d 건' % (daily_stats.loc['max']))
print(u'평균 %.1f단어 %d글자로 씀' % ( review_ds['review_content'].apply(lambda x: len(x.split(' '))).mean(),
       review_ds['review_content'].apply(lambda x: len(x)).mean()) )

print(review_ds.groupby('year')['review_content'].count())


## word cloud by word-frequency 
from os import path
from wordcloud import WordCloud

## draw word cloud by word-corpus 

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(230, 60%%, %d%%)" % random.randint(0, 20)


def drawWordCloud(corpus, figsize=(10,10), max_font_size=None):
    mask = np.array(Image.open('./resource/shape-round-square-long.png'))
    
    wordcloud = WordCloud(width=1000, height=400, margin=2, background_color='white',max_font_size=max_font_size
                          , color_func=grey_color_func , font_path='/Library/Fonts/NanumGothic.ttc'
                          , mask=mask)
    if type(corpus)==str:
        wordcloud = wordcloud.generate(corpus)
    else :
        wordcloud = wordcloud.generate_from_frequencies(corpus)

    plt.figure(figsize=figsize)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

import math

replace_chars = ":_![]/()'\","
exclude_words = set(u"re fw accepted canceled 관현".split())

def tokenize(string):
    string = string.lower()
    for ch in replace_chars:
        string = string.replace(ch, ' ')
    words = [ word for word in string.split() 
                 if (word not in exclude_words) and (len(word)>1) and (not word[0].isnumeric()) 
            ]
    return words

group_func = lambda x: '%d-%02d' % (x.year, math.floor((x.month-1)/3)*3)
def makeCorpus(ds, target):
    corpus = []
    idx2name = []
    
    #for (name, group) in ds.groupby(ds['date'].apply(group_func)):
    for (name, group) in ds.groupby(ds['product_info']):
        group_corpus= []
        for string in group[target].values:
            group_corpus.extend(tokenize(string))
        corpus.append(group_corpus)
        idx2name.append(name)
    return (corpus, idx2name)


(subject_corpus, idx2group) = makeCorpus(review_ds, 'review_content')

# * 생성된 Corpus로 TF-IDF 모델생성
from gensim import corpora, models, similarities
from time import time
import operator

dictionary = corpora.Dictionary(subject_corpus)

# compile corpus (vectors number of times each elements appears)
raw_corpus = [dictionary.doc2bow(t) for t in subject_corpus]

# Transform Text with TF-IDF
tfidf = models.TfidfModel(raw_corpus) # step 1 -- initialize a model


# * 생성된 모델로 Topic 100개씩 추출 
topic_word_list = []
topic_score_list = []
topic_word_count = 200

for (idx, src_name) in enumerate(idx2group):
    topic = tfidf[raw_corpus[idx]]
    src_name = src_name.lower()
    topic = [ (dictionary[word], score) for (word,score) in topic ]
    topic = sorted(topic, key=operator.itemgetter(1), reverse=True)
    
    topic_word_list.append( [ word for word, score in topic[:topic_word_count]] )
    topic_score_list.append( [ score for word, score in topic[:topic_word_count]] )


topic_score_ds = pd.DataFrame( topic_score_list, index=idx2group )
topic_score_ds.fillna(0, inplace=True)
topic_word_ds = pd.DataFrame( topic_word_list, index=idx2group )
topic_word_ds.fillna('', inplace=True)

## cut letters to 10
topic_word_ds = topic_word_ds.applymap(lambda x: x[:10])

# * Hitmap 형태로 그리기 
sns.set(style="whitegrid", palette="colorblind", color_codes=True, font_scale=1.1, font='NanumGothic' )
plt.figure(figsize=(18,14))
ax = sns.heatmap(topic_score_ds.ix[:,:10], annot=topic_word_ds.ix[:,:10].values, fmt="", linewidths=.2)

print("=====================")
print("=====================")
print("=====================")
plt.savefig('myfig')
plt.show()
sns.plt.show()
print("-"*30)
print("-"*30)
print("-"*30)

