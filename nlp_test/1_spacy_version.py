#!/usr/bin/env python

import spacy 

print('spacy: {}'.format(spacy.__version__))

nlp = spacy.load('en_core_web_sm')
print('en_core_web_sm version: {}'.format(nlp.meta['version']))

