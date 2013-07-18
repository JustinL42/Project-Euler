#!C:\Python33\python.exe
#https://projecteuler.net/problem=10
from Prime import prime3

prime3.prime_gen(2000000)
print(sum(prime3.prime_list))