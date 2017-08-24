#!/usr/bin/env python

from nltk.corpus import sentiwordnet as swn

'''
breakdown = swn.senti_synset('breakdown')
print(breakdown)
breakdown.pos_score()
breakdown.neg_score()
breakdown.obj_score()
'''

good_list = list(swn.senti_synsets('good', 'a'))
for item in good_list:
    print (item)


