# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:13:07 2020

@author: carlo
"""

# Problema 1
#  =============================================================================
#  Assume s is a string of lower case characters.
#  
#  Write a program that counts up the number of vowels contained in the strings.
#  Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
#  your program should print:
#  
#  Number of vowels: 5
#  =============================================================================


numVowels=0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numVowels += 1
print(numVowels)


# Problema 2
# =============================================================================
# Assume s is a string of lower case characters.
# 
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
# =============================================================================

bobs=0
for i in range(len(s)-2):
    if s[i] =="b" and s[i+1] =="o" and s[i+2] =="b":
        bobs+=1
print(bobs)


# Problem 3
# =============================================================================
# Assume s is a string of lower case characters.
# 
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
# 
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# 
# Longest substring in alphabetical order is: abc
# =============================================================================

longeststringhere=""
longest=""
for _ in range(len(s)):
    sum=0
    if _==len(s):
        break
    try:
        longeststringhere=s[_]
        while s[_]<=s[_+1]:
            longeststringhere=longeststringhere+s[_+1]
            if _+1>len(s):
                break
            _+=1
            sum+=1
            #print(longeststringhere,"\tLen", len(longeststringhere))
        if sum+1>len(longest):
                longest=longeststringhere
                #print(longest)
    except:
        break
if sum+1>len(longest):
    longest=longeststringhere
print(longest) 
