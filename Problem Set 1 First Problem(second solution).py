# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 10:34:33 2021

@author: DA_VINCI
"""

s = "azcbobobegghakl"
count = 0
x = 0
while True:
    if s[x] == 'a' or s[x] == 'o' or s[x] == 'e' or s[x] == 'i' or s[x] == 'u':
        count += 1
    x += 1
    if x == len(s):
        break    
print("Number of Vowels is: ", count)