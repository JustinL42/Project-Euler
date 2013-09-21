#!C:\Python33\python.exe
#https://projecteuler.net/problem=34
from math import factorial, log
from functools import lru_cache

sum_curious_numbers = 0
upto = 1000000 
num = 10
skip_factor = 10

@lru_cache(maxsize=None)
def factorial_sum(n_str):
    try:
        return factorial(int(n_str[1])) + factorial_sum(n_str[2:]) + factorial(int(n_str[0]))
    except IndexError:
        try:
            return factorial(int(n_str))
        except ValueError:
            return 0

while num < upto:
    sum_num = factorial_sum(str(num))
    if sum_num < num:
        skip_factor = 10
        num += 1
        continue
    if sum_num > num:
        num = max(num//skip_factor + 1, 1) * skip_factor
        skip_factor *= 10
        continue      
    sum_curious_numbers += num
    skip_factor = 10
    num += 1
    
answer = sum_curious_numbers

import clip
clip._and_print(answer)