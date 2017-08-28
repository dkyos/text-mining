#!/usr/bin/env python



from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()

TEXT = u'S8에서 Bixby가 왜 광고에 나오는 것처럼 추천기능이 작동하지 않는거니'

pprint(kkma.sentences(TEXT))
pprint(kkma.nouns(TEXT))
print(kkma.pos(TEXT))

