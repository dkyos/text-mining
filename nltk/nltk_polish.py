#!/usr/bin/env python

# http://www.nltk.org/api/nltk.stem.html#nltk.stem.snowball.GermanStemmer

import nltk

print ("="*10 + ' Word Tokenize Test: ' + "="*10)

text = '''Compatibility of systems of linear constraints over the set of
          natural numbers. Criteria of compatibility of a system of linear
          Diophantine equations, strict inequations, and nonstrict inequations are
          considered. Upper bounds for components of a minimal set of solutions
          and algorithms of construction of minimal generating sets of solutions
          for all types of systems are given. These criteria and the corresponding
          algorithms for constructing a minimal supporting set of solutions can be
          used in solving all the considered types of systems and systems of mixed
          types.'''

polish_text = '''Zgodność systemów liniowych ograniczeń w zbiorze
                 Naturalne liczby. Kryteria zgodności systemu liniowego
                 Równania diofantyne, ścisłe nierówności i nierównomierne nierówności są
                 Uważano. Górne granice elementów
                 I algorytmy budowy minimalnych zespołów prądotwórczych rozwiązań
                 Dla wszystkich typów systemów podano. Te kryteria i odpowiadające im kryteria
                 Algorytmy konstruowania minimalnego zestawu wspomagającego mogą być
                 Używane do rozwiązywania wszystkich rozważanych typów systemów i systemów mieszanych
                 Rodzaje.'''

tokens = nltk.word_tokenize(polish_text)
print (tokens)

print ("="*10 + ' Pos Tagging Test: ' + "="*10)
tagged = nltk.pos_tag(tokens)
#print (tagged[0:6])
print (tagged)

print ("="*10 + ' Noun phrase chunking Test: ' + "="*10)
# function to test if something is a noun
is_noun = lambda pos: pos[:2] == 'NN'
# do the nlp stuff
tokenized = nltk.word_tokenize(polish_text.lower())
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
print (nouns)

print ("="*10 + ' Named Entity Recognizer (NER) Test: ' + "="*10)
entities = nltk.chunk.ne_chunk(tagged)
#print (entities)


'''
import spacy 

nlp = spacy.load('xx_ent_wiki_sm')

print ("="*10 + ' Word Tokenize Test: ' + "="*10)
#doc1 = nlp(u'To jest zdanie.')
doc1 = nlp(u'To jest zdanie.')
for token in doc1:
    print (token)

print ("="*10 + ' Sentence Tokenize Test or Sentence Segmentation Test: ' + "="*10)
#doc2 = nlp(u"this is spacy sentence tokenize test. this is second sent! is this the third sent? final test.")
doc2 = nlp(u"To spajające zdanie tokenize testu. To jest drugie wysłane! Jest to trzecia wysłana? test końcowy.")
# ValueError: sentence boundary detection requires the dependency parse, which requires data to be installed. For more info, see the documentation: 
#https://spacy.io/docs/usage/models
#for sent in doc2.sents:
#    print (sent)

print ("="*10 + ' Lemmatize Test: ' + "="*10)
#doc3 = nlp(u"this is spacy lemmatize testing. programming books are more better than others")
doc3 = nlp(u"To jest spiczasty lemmatize testów. Książki programowania są lepsze od innych")
# not working => all 0 values
for token in doc3:
    print (token, token.lemma, token.lemma_)

print ("="*10 + ' Pos Tagging Test: ' + "="*10)
#doc4 = nlp(u"This is pos tagger test for spacy pos tagger")
doc4 = nlp(u"To jest test tagger tag dla tagu spacy pos")
# not working => all 0 values
for token in doc4:
    print (token, token.pos, token.pos_)

print ("="*10 + ' Named Entity Recognizer (NER) Test: ' + "="*10)
# A named entity is any real world object such as a person, location, organisation or product with a proper name.
#doc5 = nlp(u"Rami Eid is studying at Stony Brook University in New York")
# not working => wrong
doc5 = nlp(u"Rami Eid studiuje w Stony Brook University w Nowym Jorku")
for ent in doc5.ents:
    print (ent, ent.label, ent.label_)

'''



'''
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
'''
