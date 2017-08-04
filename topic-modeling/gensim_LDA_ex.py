#!/usr/bin/env python

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

# =======================================
# -- Data Set
# =======================================
doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health."

# =======================================
# -- Create word tokenizer
# =======================================
# Ref : dbrang.tistory.com/1183
word_tokenizer = RegexpTokenizer(r'\w+')

# =======================================
# -- Create English stop words list
# =======================================
# Ref : dbrang.tistory.com/1184
en_stop = get_stop_words('en')

# =======================================
# -- Create p_stemmer of class PorterStemmer
# =======================================
p_stemmer = PorterStemmer()

# =======================================
# -- Compile sample documents into a list
# =======================================
doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

print(doc_set)
print("... doc_set", "." * 100, "\n")

# =======================================
# -- List for tokenized documents in loop
# =======================================
texts = []

# --
# -- Loop through document list
# --
for i in doc_set:
    # -- clean and tokenize document string
    raw = i.lower()
    word_token = word_tokenizer.tokenize(raw)

    # -- remove stop words from tokens
    stopped_tokens = [i for i in word_token if not i in en_stop]

    # -- stem tokens
    stemmed_wtoken = [p_stemmer.stem(i) for i in stopped_tokens]

    # -- add tokens to list
    texts.append(stemmed_wtoken)

print(texts)
print(",,, word tokenization", "," * 100, "\n")


# =======================================
# -- Turn our tokenized documents into a id <-> term dictionary
# =======================================
word_dictionary = corpora.Dictionary(texts)

print(word_dictionary)
print(word_dictionary[1])
print(",,, word dictionary", "," * 100, "\n")

# for word_dic in word_dictionary.items():
#     print(word_dic)
# print(",,, word_dictionary.items()", "," * 100, "\n")

for idx, val in enumerate(word_dictionary):
    print(idx, word_dictionary[idx])
print(",,, enumerate(word_dictionary)", "," * 100, "\n")

print(word_dictionary.token2id)
print(",,, word_dictionary.token2id", "," * 100, "\n")

print(word_dictionary.id2token)
print(",,, word_dictionary.id2token", "," * 100, "\n")


# =======================================
# -- convert tokenized documents into a document-term matrix
# =======================================
corpus = [word_dictionary.doc2bow(text) for text in texts]  # Tuple (Term ID, Term Frequency)

print("doc_set[0]:", doc_set[0])
print(corpus[0])
print(corpus)
print("::: corpus", ":" * 100, "\n")


# =======================================
# -- generate LDA model
# =======================================
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word=word_dictionary, passes=20)
'''
* num_topics: required. An LDA model requires the user to determine how many topics should be generated.
* id2word: required. The LdaModel class requires our previous dictionary to map ids to strings.
* passes: optional. The number of laps the model will take through corpus. The greater the number of passes, 
the more accurate the model will be. A lot of passes can be slow on a very large corpus.
'''

print(ldamodel)
print(";;; ldamodel", ";" * 100, "\n")

print(ldamodel.print_topics(num_topics=3, num_words=3))
print(";;; ldamodel.print_topics", ";" * 100, "\n")

