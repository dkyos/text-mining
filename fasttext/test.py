#!/usr/bin/env python

from gensim.models import KeyedVectors
import pprint

model = KeyedVectors.load_word2vec_format('pl_model.vec')

# 가장 유사한 단어 30개 뽑기
# wyświetlacz: display
# akumulator: battery
pprint (model.most_similar('akumulator', topn=30))

# 단어 리스트 작성
vocab = model.index2word
#print (vocab)

# 전체 단어벡터 추출
wordvectors = []
for v in vocab:
    wordvectors.append(model.wv[v])
#print (wordvectors)

