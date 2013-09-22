#!C:\Python33\python.exe
#https://projecteuler.net/problem=35
from Prime.prime3 import prime_gen, prime_list
from bisect import bisect_left

upto = 1000000
prime_gen(upto)
count = 0

while prime_list:
    prime = prime_list[0]
    prime_str = str(prime)
    prime_len = len(prime_str)
    rotation_iter = range(1, prime_len)
    is_circular = True
    related_primes = set()
    for rotation in rotation_iter:
        prime_str = prime_str[-1] + prime_str[:-1]
        prime_int = int(prime_str)
        prime_index = bisect_left(prime_list, prime_int)
        try:
            assert prime_list[prime_index] == prime_int
        except:
            is_circular = False
            break
        related_primes.add(prime_int)    
    related_primes.add(prime)
    if not is_circular:
        del prime_list[0]
        continue
    related_primes.add(prime)
    count += len(related_primes)
    for related_prime in related_primes:
        prime_list.remove(related_prime)
    
answer = count

import clip
clip._and_print(answer)