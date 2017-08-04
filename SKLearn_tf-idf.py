#!/usr/bin/env python

from sklearn.feature_extraction import stop_words
from sklearn.feature_extraction.text import TfidfVectorizer

# =======================================
# -- Frozon Stopwords
# =======================================
print(len(stop_words.ENGLISH_STOP_WORDS), stop_words.ENGLISH_STOP_WORDS)
print("... SKlearn stop words ", "." * 100, "\n")

from nltk.corpus import stopwords
print(len(stopwords.words('english')), stopwords.words('english'))
print("... NLTK stop words", "." * 100, "\n")

# =======================================
# -- Add stopword in Tfidf vectorizer
# =======================================
corpus = ['Saya benci awak aaa',
    'Saya cinta awak aaa',
    'Saya x happy awak bbb',
    'Saya geram awak bbb',
    'Saya taubat awak ccc']

# --
# -- Add custom stopwords
# --
stop_words = ["aaa","bbb","ccc"]

# --
# -- Get TFIDF without Stopwords
# --
vectorizer = TfidfVectorizer(analyzer='word')
X = vectorizer.fit_transform(corpus)
idf = vectorizer.idf_

print (dict(zip(vectorizer.get_feature_names(), idf)))
print(",,, tfidf without Stopwords", "," * 100, "\n")

# --
# -- Get TFIDF with Stopwords
# --
vectorizer2 = TfidfVectorizer(analyzer='word', stop_words = stop_words)
X2 = vectorizer2.fit_transform(corpus)
idf2 = vectorizer2.idf_

print (dict(zip(vectorizer2.get_feature_names(), idf2)))
print("::: tfidf with Stopwords", ":" * 100, "\n")
