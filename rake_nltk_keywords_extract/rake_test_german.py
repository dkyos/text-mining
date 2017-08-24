#!/usr/bin/env python

import unittest
from collections import defaultdict

import nltk
from rake_nltk import Rake

###########################################################


def test_extract_keywords_from_text():
    #r = Rake()
    rg = Rake(language='german')
    #rp = Rake(language='polish') # not support

    text = '''Compatibility of systems of linear constraints over the set of
        natural numbers. Criteria of compatibility of a system of linear
        Diophantine equations, strict inequations, and nonstrict inequations are
        considered. Upper bounds for components of a minimal set of solutions
        and algorithms of construction of minimal generating sets of solutions
        for all types of systems are given. These criteria and the corresponding
        algorithms for constructing a minimal supporting set of solutions can be
        used in solving all the considered types of systems and systems of mixed
        types.'''

    german_text = '''Kompatibilität von Systemen linearer Einschränkungen über den Satz von
        Natürliche Zahlen. Kriterien der Kompatibilität eines linearen Systems
        Diophantische Gleichungen, strenge Ungleichungen und nonstrict Ungleichungen sind
        Betrachtete Obere Schranken für Komponenten
        Und Algorithmen der Konstruktion von minimalen Generierung von Lösungen
        Für alle Arten von Systemen sind gegeben. Diese Kriterien und die entsprechenden
        Algorithmen für den Aufbau eines minimalen unterstützenden Satzes von Lösungen können sein
        Wird verwendet, um alle betrachteten Systeme und Systeme von gemischten zu lösen
        Typen.'''


    polish_text = '''Zgodność systemów liniowych ograniczeń w zbiorze
        Naturalne liczby. Kryteria zgodności systemu liniowego
        Równania diofantyne, ścisłe nierówności i nierównomierne nierówności są
        Uważano. Górne granice elementów
        I algorytmy budowy minimalnych zespołów prądotwórczych rozwiązań
        Dla wszystkich typów systemów podano. Te kryteria i odpowiadające im kryteria
        Algorytmy konstruowania minimalnego zestawu wspomagającego mogą być
        Używane do rozwiązywania wszystkich rozważanych typów systemów i systemów mieszanych
        Rodzaje.'''

    #r.extract_keywords_from_text(text)
    rg.extract_keywords_from_text(german_text)

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

    print("==== German =======")
    print(rg.get_ranked_phrases())

test_extract_keywords_from_text()


