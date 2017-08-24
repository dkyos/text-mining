#!/usr/bin/env python

import spacy 

nlp = spacy.load('en_core_web_sm')
#import en_core_web_md
#nlp = en_core_web_md.load()

print ("="*10 + ' Word Tokenize Test: ' + "="*10)
doc1 = nlp(u'This is a sentence.')
for token in doc1:
    print (token)

print ("="*10 + ' Sentence Tokenize Test or Sentence Segmentation Test: ' + "="*10)
doc2 = nlp(u"this is spacy sentence tokenize test. this is second sent! is this the third sent? final test.")
for sent in doc2.sents:
    print (sent)

print ("="*10 + ' Lemmatize Test: ' + "="*10)
doc3 = nlp(u"this is spacy lemmatize testing. programming books are more better than others")
for token in doc3:
    print (token, token.lemma, token.lemma_)

print ("="*10 + ' Pos Tagging Test: ' + "="*10)
doc4 = nlp(u"This is pos tagger test for spacy pos tagger")
for token in doc4:
    print (token, token.pos, token.pos_)

print ("="*10 + ' Named Entity Recognizer (NER) Test: ' + "="*10)
# A named entity is any real world object such as a person, location, organisation or product with a proper name.
doc5 = nlp(u"Rami Eid is studying at Stony Brook University in New York")
for ent in doc5.ents:
    print (ent, ent.label, ent.label_)

print ("="*10 + ' Noun Chunk Test: ' + "="*10)
# Noun chunks are the phrases based upon nouns recovered from tokenized text using the speech tags.
doc6 = nlp(u"Natural language processing (NLP) deals with the application of computational models to text or speech data.")
for np in doc6.noun_chunks:
    print (np)


print ("="*10 + ' Word Vectors Test: ' + "="*10)
doc7 = nlp(u"Apples and oranges are similar. Boots and hippos aren't.")
apples = doc7[0]
oranges = doc7[2]
boots = doc7[6]
hippos = doc7[8]
print (apples.similarity(oranges))
print (boots.similarity(hippos))

