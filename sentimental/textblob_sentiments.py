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
    blob = TextBlob(test_string[i], analyzer=NaiveBayesAnalyzer())
    print(blob.detect_language())
    print(blob.translate(to="en"))
    print(blob.sentiment)
    i=i+1 

