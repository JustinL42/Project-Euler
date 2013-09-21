#!C:\Python33\python.exe
#https://projecteuler.net/problem=34
from math import factorial
from itertools import permutations, combinations_with_replacement

calculated_digits = list(range(10))
calculated_factorials = [factorial(x) for x in calculated_digits]
curious_numbers = set()

for num_digits in range(2, 8):
    digits = calculated_digits
    factorials = calculated_factorials
    possibilities = []
    sum_nums = []
    floor = 10**(num_digits - 1) - 1
    ceiling = 10**(num_digits)
    for combo in combinations_with_replacement(digits, num_digits):
        sum_num = sum(factorials[digit] for digit in combo)

        if ceiling > sum_num > floor:
            possibilities.append(combo)  
            sum_nums.append(sum_num)
            
    calculated_digit_range = list(range(num_digits))
    for possible_combo, sum_num in zip(possibilities, sum_nums):
        digit_range = calculated_digit_range
        for permutation in sorted(permutations(possible_combo, num_digits)):
            number = sum(permutation[-i - 1] * 10**(i) for i in digit_range)
            if number > sum_num:
                break
            if number == sum_num:
                print(number)
                curious_numbers.add(number)
    
answer = sum(curious_numbers)

import clip
clip._and_print(answer)