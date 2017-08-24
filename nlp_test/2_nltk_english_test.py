#!/usr/bin/env python

import nltk

print ("="*10 + ' Word Tokenize Test: ' + "="*10)
doc1 = "This is a sentence."
tokens = nltk.word_tokenize(doc1)
print (tokens)


print ("="*10 + ' Pos Tagging Test: ' + "="*10)
doc4 = "This is pos tagger test for spacy pos tagger"
tokens = nltk.word_tokenize(doc4)
tagged = nltk.pos_tag(tokens)
print (tagged[0:6])

print ("="*10 + ' Named Entity Recognizer (NER) Test: ' + "="*10)
doc5 = "Rami Eid is studying at Stony Brook University in New York"
tokens = nltk.word_tokenize(doc5)
tagged = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tagged)
print (entities)




