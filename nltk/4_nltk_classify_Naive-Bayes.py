#!/usr/bin/env python

import nltk

# =======================================
# -- Sourcing
# =======================================
data = [('Hi John, I will see you at 9:00pm', 'ham'),
     ('Buy Viagra at low, low prices.  One time offer.', 'spam'),
     ('Your Amazon Order is for the book "Harry Potter"', 'ham'),
     ('Earn a million dollars by working at home.', 'spam')]

print(type(data))
print(data)
print("... source", "." * 100, "\n")


# =======================================
# -- Word_token & Word featuring
# =======================================
def features(s):
    dict_vec = {}
    for wtoken in nltk.tokenize.word_tokenize(s):
        dict_vec[wtoken] = 1 if wtoken not in dict_vec else dict_vec[wtoken] + 1
    return dict_vec

processed_data = [(features(tup[0]), tup[1]) for tup in data]

print(type(processed_data))
print(processed_data)
print(",,, word_featuring", "," * 100, "\n")


# =======================================
# -- Training and Testing
# =======================================

# -- Training
# -- nltk.NaiveBayesClassifier.train( [( {'John': 1, ... }, 'ham'), ...] )
classifier = nltk.NaiveBayesClassifier.train(processed_data)

# -- Testing
print(classifier.classify(features("This is good Viagra!")))
print(classifier.classify(features("We will meet you at 7pm. Take care")))



