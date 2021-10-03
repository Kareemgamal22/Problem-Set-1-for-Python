# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 10:34:33 2021

@author: DA_VINCI
"""

s = "azcbobobegghakl"
count = 0
for x in s:
    if x == 'a' or x == 'o' or x == 'e' or x == 'i' or x == 'u':
        count += 1
print("Number of Vowels is: ", count)