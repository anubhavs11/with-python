#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 10:37:13 2018

@author: root
"""

import random

text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

n=3

ngram = {}

for i in range(len(text)-n):
    gram = text[i:i+n]
    if(gram not in ngram.keys()):
        ngram[gram] = []
    ngram[gram].append(text[i+n])
    
# Building Autocomplete Model
Currentgram = text[0:n]
result = Currentgram

for i in range(len(text)+1-n):
    if(Currentgram not in ngram.keys()):
        break
    posibilities = ngram[Currentgram]
    nextItem = posibilities[random.randrange(len(posibilities))]
    result += nextItem
    Currentgram = result[len(result)-n:len(result)]

print(result)      