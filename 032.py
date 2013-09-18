#!C:\Python33\python.exe
#https://projecteuler.net/problem=32

digits = list(range(1, 9 + 1))
unusual_products = set()

from Combinatorics.combinatorics import m_way_ordered_combinations as combos

def num(tuple_comb):
    number = 0
    for index in range(1, len(tuple_comb) + 1):
        number += tuple_comb[-index][0] * 10**(index - 1)
    return number

def find_products(factor_length1, factor_length2):
    product_length = len(digits) - factor_length1 - factor_length2
    global unusual_products
    for small_factor in combos(digits, [1]*factor_length1):  
        remaining_digits1 = list(digits)
        for digit in small_factor:
            remaining_digits1.remove(digit[0])
        for large_factor in combos(remaining_digits1, [1]*factor_length2):
            remaining_digits2 = list(remaining_digits1)
            for digit in large_factor:
                remaining_digits2.remove(digit[0])
            
            previous_product = 0
            product = num(small_factor) * num(large_factor)
            product_tuples = list(combos(remaining_digits2, [1]*product_length))
            product_tuples.sort()
            for product_tuple in product_tuples:
                possible_product =num(product_tuple)
                if possible_product > product:
                    break
                if possible_product == product:
                    unusual_products.add(product)

find_products(1, 4)
find_products(2, 3)  

answer = sum(unusual_products)

import clip
clip._and_print(answer)