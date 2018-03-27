#!/usr/bin/env python

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


# English: "I love this library"
# German: "Ich liebe diese Bibliothek"
# Polish: "Uwielbiam tę bibliotekę"

# English: This product does not function properly
# German: Dieses Produkt funktioniert nicht richtig
# Polish: Ten produkt nie działa poprawnie


test_string = ["Ich liebe diese Bibliothek"
    ,"Uwielbiam tę bibliotekę"
    ,"Dieses Produkt funktioniert nicht richtig"
    ,"Ten produkt nie działa poprawnie"]

i=0 
while i<len(test_string): 
    print("================================")
    print("Sentence: {}".format(test_string[i]))
    blob = TextBlob(test_string[i], analyzer=NaiveBayesAnalyzer())
    lang = blob.detect_language()
    print("language: {}".format(lang))
    print(blob.translate(from_lang=lang, to="en"))
    print(blob.sentiment)
    blob = TextBlob(str(blob.translate(to="en")), analyzer=NaiveBayesAnalyzer())
    print("Sentimenal after translated to english: {}".format(blob.sentiment))
    i=i+1 

