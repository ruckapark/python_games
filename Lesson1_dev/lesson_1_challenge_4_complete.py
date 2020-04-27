# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 13:28:20 2020

@author: George
"""


"""
SOLUTION
"""

import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('articles')

text_files = [file for file in os.listdir() if 'txt' in file]

article_dict = {}
article_paramters = {'newspaper':[],'word_length':[],'sentences':[],'ands':[]}
for file in text_files:
    temp = open(file,'r')
    article_dict.update({file:temp.read()})
    
min_length = min([len(article_dict[file]) for file in text_files])
    
for file in text_files:
    article_dict[file] = article_dict[file][:min_length]
    article_paramters['newspaper'].append(file.split('.')[0])
    article_paramters['word_length'].append(np.mean([len(word) for word in article_dict[file].split()]))
    article_paramters['sentences'].append(len(article_dict[file].split('.')))
    article_paramters['ands'].append(len([word for word in article_dict[file].split() if 'and' in word.lower()]))
 
#plotting
x_locs = np.array([0,1,2])
barwidth = 0.25
fig, ax = plt.subplots(1,3,sharey = True)

ax[0].bar(x_locs,article_paramters['word_length'],color = ['r','b','y'])
ax[0].set_title('Mean word length')
ax[1].bar(x_locs,article_paramters['sentences'],color = ['r','b','y'])
ax[1].set_title('Sentences')
ax[2].bar(x_locs,article_paramters['ands'],color = ['r','b','y'])
ax[2].set_title('Ands')

plt.show()
os.chdir('..')