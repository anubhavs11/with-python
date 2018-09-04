#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 18:57:00 2018

@author: root
"""
import nltk
from nltk.corpus import wordnet

sentence = "I was not happy with the team's performance"

#I was not happy with the team's performance
#I was unhappy with the team's performance

words = nltk.word_tokenize(sentence)

new_words = []
antonyms = []

temp_words = ""

for word in words:
    if word == "not":
        temp_words = "not_"
    elif temp_words == "not_":
        for syn in wordnet.synsets(word):
            for s in syn.lemmas():
                for a in s.antonyms():
                    antonyms.append(a.name())
        if len(antonyms) >= 1:
            word = antonyms[0]
        else:
            word = temp_words + word 
        temp_words = ""
    if word != "not":
        new_words.append(word)

sentence = " ".join(new_words)
print(sentence)