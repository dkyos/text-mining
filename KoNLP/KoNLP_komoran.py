#!/usr/bin/env python



from konlpy.tag import Komoran
from konlpy.utils import pprint

komoran = Komoran()

TEXT = u'S8에서 Bixby가 왜 광고에 나오는 것처럼 추천기능이 작동하지 않는거니'

print(komoran.morphs(TEXT))
#print(komoran.nouns(TEXT))
print(komoran.pos(TEXT))

