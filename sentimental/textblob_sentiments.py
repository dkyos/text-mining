#!/usr/bin/env python

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


# English: "I love this library"
# German: "Ich liebe diese Bibliothek"
# Polish: "Uwielbiam tę bibliotekę"

blob = TextBlob("I love this library", analyzer=NaiveBayesAnalyzer())
print(blob.sentiment)

blob = TextBlob("Ich liebe diese Bibliothek", analyzer=NaiveBayesAnalyzer())
print(blob.detect_language())
print(blob.translate(to="en"))
print(blob.sentiment)

blob = TextBlob("Uwielbiam tę bibliotekę", analyzer=NaiveBayesAnalyzer())
print(blob.detect_language())
print(blob.translate(to="en"))
print(blob.sentiment)

