#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 12:45:23 2018

@author: root
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import nltk

dataset =  ["The amount of polution is increasing day by day",
           "The concert was just great",
           "I love to see Gordon Ramsay cook",
           "Google is introducing a new technology",
           "AI Robots are examples of great technology present today",
           "All of us were singing in the concert",
"We have launch campaigns to stop pollution and global warming"]

dataset = [line.lower() for line in dataset]

# Created TF-IDF Model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset)

print(X[0])

# Created SVD(Singular Value Decomposition)
lsa = TruncatedSVD(n_components = 4,n_iter = 100)
lsa.fit(X)

row1 = lsa.components_[0]

terms = vectorizer.get_feature_names()
concept_words={}

for i,comp in enumerate(lsa.components_):
    componentTerms = zip(terms,comp)
    sortedTerms = sorted(componentTerms,key=lambda x:x[1],reverse=True)
    sortedTerms = sortedTerms[:10]
    concept_words["Concept "+str(i)] = sortedTerms
    
for key in concept_words.keys():
    sentence_scores = []
    for sentence in dataset:
        words = nltk.word_tokenize(sentence)
        scores = 0
        for word in words:
            for word_with_scores in concept_words[key]:
                if word == word_with_scores[0]:
                    scores += word_with_scores[1]
        sentence_scores.append(scores)
    print("\n"+key+":")
    for sentence_score in sentence_scores:
        print(sentence_score)
