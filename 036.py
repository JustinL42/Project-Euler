#!C:\Python33\python.exe
#https://projecteuler.net/problem=36
from pally import is_pallindrome

palindrome_sum = 0
for num in range(1, 1000000):
    if is_pallindrome(str(num)):
        if is_pallindrome(bin(num)[2:]):
            # print(num)
            palindrome_sum += num
        
answer = palindrome_sum

import clip
clip._and_print(answer)