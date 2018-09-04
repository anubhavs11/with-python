#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 10:57:41 2018

@author: root
"""

import random
import nltk

text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

words = nltk.word_tokenize(text)

n=3
ngram = {}

for i in range(len(words)-n):
    gram = ' '.join(words[i:i+n])
    if gram not in ngram.keys():
        ngram[gram] = []
    ngram[gram].append(words[i+n])
    
currentGram = ' '.join(words[0:n])
result = words[0:n]

for i in range(len(words)):
    if currentGram not in ngram.keys():
        break
    possibilities = ngram[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result.append(nextItem)
    currentGram = ' '.join(result[len(result)-n:len(result)])
    
print(' '.join(result))