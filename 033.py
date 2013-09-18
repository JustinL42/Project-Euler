#!C:\Python33\python.exe
#https://projecteuler.net/problem=33
from fractions import Fraction

product = Fraction(1,1)

def check(n_tens, n_ones, d_tens, d_ones):
    raw_fraction = Fraction(n_tens*10 + n_ones, d_tens*10 + d_ones)
    
    def cancel_out(num, den):
        if den != 0:
            if Fraction(num, den) == raw_fraction:
                global product
                print(n_tens*10 + n_ones, "over", d_tens*10 + d_ones)
                product *= raw_fraction
            
    if n_ones == d_ones:
        cancel_out(n_tens, d_tens)
    if n_tens == d_tens:
        cancel_out(n_ones, d_ones)
    if n_ones == d_tens:
        cancel_out(n_tens, d_ones)
    if n_tens == d_ones:
        cancel_out(n_ones, d_tens)


for den_tens in range(1, 9 + 1):
    for den_ones in range (0, 9 + 1):
        for num_tens in range(1, den_tens):
            for num_ones in range(1, 9 + 1):
                check(num_tens, num_ones, den_tens, den_ones)
        num_tens = den_tens
        for num_ones in range(1, den_ones):
            check(num_tens, num_ones, den_tens, den_ones)


answer = product.denominator

import clip
clip._and_print(answer)