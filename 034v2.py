#!C:\Python33\python.exe
#https://projecteuler.net/problem=34
from math import factorial
from array import array

upto = 10000000
lookup_table = array('I', (0 for n in range(upto)))
for num in range(10):
    lookup_table[num] = factorial(num)

sum_curious_numbers = 0
num = 10
skip_factor = 10
while num < upto:
    str_num = str(num)
    sum_num = lookup_table[int(str_num[0])]
    
    def get_and_cache(num_string):
        extra_zeros = 0
        if num_string[0] == '0':
            for char in num_string:
                if char != '0':
                    break
                extra_zeros += 1
            num_string = num_string[extra_zeros:]
            if num_string == '':
                return extra_zeros
        index = int(num_string)               
        if lookup_table[index] == 0:
            lookup_table[index] = lookup_table[int(num_string[0])] + get_and_cache(num_string[1:])
        return lookup_table[index] + extra_zeros
        
    sum_num += get_and_cache(str_num[1:])
    lookup_table[num] = sum_num
    if sum_num < num:
        skip_factor = 10
        num += 1
        continue
    if sum_num > num:
        num = max(num//skip_factor + 1, 1) * skip_factor
        skip_factor *= 10
        continue 
    skip_factor = 10
    num += 1
    
answer = sum_curious_numbers

import clip
clip._and_print(answer)