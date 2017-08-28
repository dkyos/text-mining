#!/usr/bin/env python

from konlpy.tag import Twitter
from konlpy.utils import pprint
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

twitter = Twitter()
stop_words = set(stopwords.words('korean'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) # remove it if you need punctuation

#TEXT = u'S8에서 Bixby가 왜 광고에 나오는 것처럼 추천기능이 작동하지 않는거니'
TEXT = u'갤럭시에서 Bixby 기능이 왜 광고에 나오는 것처럼 추천기능이 작동하지 않는거니'

print ("=== Parse phrase(tokenize) to morphemes. ===")
print(twitter.morphs(TEXT))
#print ("=== Nouns extract ===")
#print(twitter.nouns(TEXT))
#print ("=== Phrase extract ===")
#print(twitter.phrases(TEXT))

print ("=== Post tagger ===")
print(twitter.pos(TEXT))

print ("="*10 + ' Remove stopwords(& lower) Test: ' + "="*10)
print ([(i.lower(), j) for i, j in twitter.pos(TEXT) if i.lower() not in stop_words])

print ("=== Post tagger with normalization & stemming(lemmatization) ===")
print ([(i.lower(), j) for i, j in twitter.pos(TEXT, norm=True, stem=True) if i.lower() not in stop_words])
