#!/usr/bin/env python

# https://www.lucypark.kr/courses/2015-dm/text-mining.html


#샘플 corpus 및 사전
#토큰 생성(tokenizing)
#형태소 분석(stemming/lemmatizing)
#품사 태깅(part-of-speech tagging)
#구문 분석(syntax parsing)

import nltk

text = '''Compatibility of systems of linear constraints over the set of
          natural numbers. Criteria of compatibility of a system of linear
          Diophantine equations, strict inequations, and nonstrict inequations are
          considered. Upper bounds for components of a minimal set of solutions
          and algorithms of construction of minimal generating sets of solutions
          for all types of systems are given. These criteria and the corresponding
          algorithms for constructing a minimal supporting set of solutions can be
          used in solving all the considered types of systems and systems of mixed
          types.'''


##################################################################
print ("="*10 + ' Word_tokenize Test: ' + "="*10)
tokens = nltk.word_tokenize(text)
print (tokens)

##################################################################
print ("="*10 + ' stop words Test: ' + "="*10)
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) # remove it if you need punctuation 
list_of_words = [i.lower() for i in wordpunct_tokenize(text) if i.lower() not in stop_words]
print (list_of_words)

##################################################################
print ("="*10 + ' Pos Tagging Test: ' + "="*10)
#tagged = nltk.pos_tag(tokens)
#print (tagged[0:5])
tagged2 = nltk.pos_tag(list_of_words)
print (tagged2[0:5])

##################################################################
print ("="*10 + ' Nouns Test: ' + "="*10)
# function to test if something is a noun
is_noun = lambda pos: pos[:2] == 'NN'
from nltk.stem import PorterStemmer
st = PorterStemmer()
nouns = [st.stem(word) for (word, pos) in nltk.pos_tag(list_of_words) if is_noun(pos)] 
print (nouns)

print ("="*10 + ' Named Entity Recognizer (NER) Test: ' + "="*10)
entities = nltk.chunk.ne_chunk(tagged2)
print (entities)
#print (entities[0:5])


'''
##################################################################
#print ("="*10 + ' Stemming and lemmatizing Test:' + "="*10)
from nltk.stem import PorterStemmer
st = PorterStemmer()
#print (st.stem("eating"))

from nltk.stem import LancasterStemmer
st = LancasterStemmer()
#print (st.stem("shopping"))

from nltk.stem import RegexpStemmer
st = RegexpStemmer("ing")
#print (st.stem("cooking"))

from nltk.stem import WordNetLemmatizer
lm = WordNetLemmatizer()
print(lm.lemmatize("cooking"))
print(lm.lemmatize("cooking", pos="v"))
print(lm.lemmatize("cookbooks"))

print(WordNetLemmatizer().lemmatize("believes"))
print(LancasterStemmer().stem("believes"))

##################################################################
#print ("="*10 + ' nltk.Text Test: ' + "="*10)
import nltk
en = nltk.Text(tokens)
#print(len(en.tokens))       # returns number of tokens (document length)
#print(len(set(en.tokens)))  # returns number of unique tokens
#print(en.vocab())                  # returns frequency distribution
#en.plot()

from matplotlib import pylab
pylab.show = lambda: pylab.savefig('some_filename.png')

from matplotlib import font_manager, rc
font_fname = 'c:/windows/fonts/gulim.ttc'     # A font of your choice
font_name = font_manager.FontProperties(fname=font_fname).get_name()
rc('font', family=font_name)

print(en.count('of'))        # Counts occurrences

#en.dispersion_plot(['Emma', 'Frank', 'Jane'])
print (en.similar('of'))
print(en.collocations())

print(en.vocab())
data = en.vocab().items()
print(data)
print(type(data))
'''
