#!C:\Python33\python.exe
#https://projecteuler.net/problem=5
from Prime import prime3

num = dict()


for i in range(1,20+1):
    factor = prime3.factorize(i)
    for prime, exponent in factor.items():
        if prime in num:
            new_exponent = max(exponent, num[prime])
            num[prime] = new_exponent
        else:
            num[prime] = exponent

answer = prime3.combine(num)

print(answer)
    