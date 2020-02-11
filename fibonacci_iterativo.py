# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:08:48 2020

@author: carlo
"""

# =============================================================================
# def ajam(okgood):
#     okgood=
#     cache=[1,0,0]
#     fiboN=1
#     for i in range(okgood):
#         cache[2]=cache[1]
#         cache[1]=cache[0]
#         cache[0]+=cache[2]
#         fiboN=cache[0]
#     return fiboN
# =============================================================================

# =============================================================================
# # porque me dijeron que edgar lo hizo mas corto y compacto
# def ajam(okgood):
#     cache,cache1=1,0
#     for i in range(okgood):
#         cache1,cache = cache,cache+cache1
#     return cache1
# print(list(map(ajam,range(1,10))))
# =============================================================================

# suma de todos los numeros de fibonacci
from functools import *
def ajam(okgood):
    cache,cache1=1,0
    for i in range(okgood):
        cache1,cache = cache,cache+cache1
    return cache1

print(reduce(lambda a, b : a + b,list(map(ajam,range(1,1000)))))
