# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 10:34:33 2021

@author: DA_VINCI
"""

s = "azcbobobegghakl"
count = 0
x = 0
for x in range(len(s)):
    if s[x] == 'b' and s[x + 1] == 'o' and s[x + 2] == 'b':
        count += 1
print("Number of bob is: ", count)