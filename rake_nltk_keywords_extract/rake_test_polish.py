#!/usr/bin/env python

# polish language not support (default)
# polish stopwords file is not found in nltk_data/corpora/stopwords/
# we need add polish stopwords file in this location
# we get many_stop_words/stopwords-pl.txt in https://github.com/trec-kba/many-stop-words
# so, copy stopwords-pl.txt to nltk_data/corpora/stopwords/polish => It's works

import unittest
from collections import defaultdict

import nltk
from rake_nltk import Rake

###########################################################


def test_extract_keywords_from_text():
    #r = Rake()
    rp = Rake(language='polish') # not support

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

    rp.extract_keywords_from_text(polish_text)

    ranked_phrases = [
            'minimal generating sets', 'linear diophantine equations',
            'minimal supporting set', 'minimal set', 'linear constraints',
            'upper bounds', 'strict inequations', 'nonstrict inequations',
            'natural numbers', 'mixed types', 'corresponding algorithms',
            'considered types', 'set', 'types', 'considered', 'algorithms',
            'used', 'systems', 'system', 'solving', 'solutions', 'given',
            'criteria', 'construction', 'constructing', 'components',
            'compatibility'
    ]
    #assertEqual(r.get_ranked_phrases(), ranked_phrases)
    #assertEqual([phrase for _, phrase in r.get_ranked_phrases_with_scores()], ranked_phrases)

    print("==== Polish =======")
    print(rp.get_ranked_phrases())

test_extract_keywords_from_text()


