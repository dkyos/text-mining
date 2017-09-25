#!/usr/bin/env python

# from http://shichaoji.com/2017/02/25/topicmodeling/

import pandas as pd
from helper import *
# ! pip install pandas nltk gensim pyldavis
# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

import nltk
#nltk.download('stopwords')
#nltk.download('wordnet')

from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string


#DOC_FILE = 'plot.tok.gt9.5000'
DOC_FILE = "docs_txt"
DICT_FILE = DOC_FILE+".dict"
CORPUS_FILE = DOC_FILE+".mm"
MODEL_FILE = DOC_FILE+".model"
HTML_FILE = DOC_FILE+".html"

stopwords = set(stopwords.words('english'))
punctuation = set(string.punctuation) 
lemmatize = WordNetLemmatizer()

def cleaning(article):
    one = " ".join([i for i in article.lower().split() if i not in stopwords])
    two = "".join(i for i in one if i not in punctuation)
    three = " ".join(lemmatize.lemmatize(i) for i in two.split())
    return three

# from http://www.cs.cornell.edu/People/pabo/movie-review-data/
# download http://www.cs.cornell.edu/people/pabo/movie-review-data/rotten_imdb.tar.gz
df = pd.read_table(DOC_FILE, names=['text'], encoding = 'utf8')
df.info()
df.head(3)

text = df.applymap(cleaning)['text']
text_list = [i.split() for i in text]
print (len(text_list))
print (text_list[0])

'''
for i in range(len(text_list)):
    for j in range(len(text_list[i])):
        #print ("[%d] %d: %s" % (i, j, text_list[i][j]))
        text_list[i][j] = text_list[i][j] + ' (translated)'
        print ("[%d] %d: %s" % (i, j, text_list[i][j]))
'''

from time import time
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO,
                   filename='running.log',filemode='w')

# Importing Gensim
import gensim
from gensim import corpora

# Creating the term dictionary of our courpus, where every unique term is assigned an index. dictionary = corpora.Dictionary(doc_clean)
dictionary = corpora.Dictionary(text_list)
dictionary.save(DICT_FILE)
print (dictionary)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in text_list]
corpora.MmCorpus.serialize(CORPUS_FILE, doc_term_matrix)
print (len(doc_term_matrix))
print (doc_term_matrix[3])


start = time()
Hdp = gensim.models.hdpmodel.HdpModel
hdpmodel = Hdp(doc_term_matrix, id2word = dictionary)

print ('used: {:.2f}s'.format(time()-start))
print(hdpmodel.print_topics(num_topics=2, num_words=4))

for i in hdpmodel.print_topics(): 
    for j in i: 
        print (j)

hdpmodel.save(MODEL_FILE)

from gensim.models import HdpModel
loading = HdpModel.load(MODEL_FILE)
print(loading.print_topics(num_topics=2, num_words=4))

import pyLDAvis.gensim
import gensim

d = gensim.corpora.Dictionary.load(DICT_FILE)
c = gensim.corpora.MmCorpus(CORPUS_FILE)
hdp  = gensim.models.HdpModel.load(MODEL_FILE)

# the followin is error
#lda = hdp.hdp_to_lda()
#data = pyLDAvis.gensim.prepare(lda, c, d)

data = pyLDAvis.gensim.prepare(hdp, c, d)
#print (data)

pyLDAvis.save_html(data, HTML_FILE)

#for i in range(len(c)):
#    print ('doc id:'+str(i))
#    print (lda[c[i]])
#    i=i+1
