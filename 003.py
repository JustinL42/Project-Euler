#!C:\Python33\python.exe
#https://projecteuler.net/problem=3
import sys
import primegen2
import functools
import operator

def product(seq):
    """Product of a sequence."""
    return functools.reduce(operator.mul, seq, 1)

try:
    number = int(sys.argv[1])
except IndexError:
    number = 600851475143

prime_factors = []
top = 10000

#first time 
primes = primegen2.primegen(top, 1000000)
nmbr = number

for prime in primes:
  if nmbr%prime == 0:
    prime_factors.append(prime)
    while nmbr%prime == 0:
      nmbr /= prime
      
while top < nmbr:
  top *= 10
  primes = primegen2.primegen(top, 1000000, prime_list=primes)
  for prime in primes:
    if nmbr%prime == 0:
      prime_factors.append(prime)
      while nmbr%prime == 0:
        nmbr /= prime
        
if nmbr != 1:
  prime_factors.add(nmbr)
  prime_factors.sort()

if len(prime_factors) == 0:
    prime_factors.append(number)

print("nmbr", nmbr)
print("prime_factors:", prime_factors)
print("max pfactor", max(prime_factors))
print("check: product of the list equals:", product(prime_factors))