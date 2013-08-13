#!C:\Python33\python.exe
#https://projecteuler.net/problem=27
from Prime import prime3
from datetime import datetime

class Quad:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def prod_of_coefficients(self):
        return self.a * self.b
        
    def consecutive_primes(self):
        count = 0
        fun = lambda x: x**2 + self.a * x + self.b
        result = fun(count)
        while result > 1 and prime3.is_prime(result):
            count += 1
            result = fun(count)
        return count  

print(datetime.now().time())

prime3.prime_gen(1000)
fixed_prime_list = list(prime3.prime_list)
record = 0
record_holder = 0

def inner_loop(a, b):
    q = Quad(a, b)
    c = q.consecutive_primes()
    global record, record_holder
    if c > record:
        record = c
        record_holder = q.prod_of_coefficients()
    

for a in range(-1000, 1000+1):
    for prime in fixed_prime_list:
        inner_loop(a, prime)
        inner_loop(a, -prime)


answer = record_holder

#print the answer and copy to clipboard
print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)

print(datetime.now().time())