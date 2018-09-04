
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 18:51:32 2018

@author: root
"""

from nltk.corpus import wordnet

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for s in syn.lemmas():
        synonyms.append(s.name())
        for a in s.antonyms():
            antonyms.append(a.name())

print(set(synonyms))
print(set(antonyms))