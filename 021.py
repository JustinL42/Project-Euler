#!C:\Python33\python.exe
#https://projecteuler.net/problem=21

from Prime import prime3

d_hash = dict()

def d(n):
    global d_hash
    
    if n not in d_hash:
        result = sum((prime3.factor_list(n))[:-1])
        d_hash[n] = result
        return result
    else:
        return d_hash[n]
        
upto = 10000
amicable_sum = 0
a = 2

while a < upto:
    b = d(a)
    d2 = d(b)
    
    if a == d2 and a != b:
        amicable_sum += a
        
    a += 1
    
answer = amicable_sum


#print the answer and copy to clipboard
print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)