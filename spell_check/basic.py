#!/usr/bin/env python

# http://pythonhosted.org/pyenchant/tutorial.html#id1
# pip install pyenchant

import enchant

print ("pyenchant examples")

print ("- Supported Languages")
print (enchant.list_languages())
# Default:
#   ['ko', 'ko_KR', 'en_GB', 'en_CA', 'en_US', 'en_AU', 'en_ZA', 'en']
# for german
#   sudo apt-get install myspell-de-de
#   ['ko', 'ko_KR', 'en_GB', 'en_CA', 'en_US', 'de_BE', 'de_LU', 'en_AU', 'en_ZA', 'de_DE', 'en']
# for german
#   sudo apt-get install myspell-pl
#   ['ko', 'ko_KR', 'en_GB', 'en_CA', 'en_US', 'de_BE', 'de_LU', 'en_AU', 'pl', 'en_ZA', 'de_DE', 'pl_PL', 'en']

print ("- German Test")
de = enchant.Dict('de_DE')
print(de.tag)
print("[Hello] check =>")
print(de.check("Hello")) # False
print("[Guten] check =>")
print(de.check("Guten")) # True
print("[Gute] Suggest =>")
print(de.suggest("Gute")) # True

print ("- Polish Test")
pl = enchant.Dict('pl_PL')
print(pl.tag)
print("[koszt] check =>")
print(pl.check("koszt")) 
print("[wyswietlacza] check =>")
print(pl.check("wyswietlacza")) # False (fail)

pl2= enchant.DictWithPWL("pl_PL","polish.txt")
print("[wyswietlacza] check =>")
print(pl2.check("wyswietlacza"))


print ("- Full Text Test")
from enchant.checker import SpellChecker
chkr = SpellChecker("en_US")
chkr.set_text("This is sme sample txt with erors.")
for err in chkr:
    print ("ERROR:", err.word)




