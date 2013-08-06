#!C:\Python33\python.exe
#https://projecteuler.net/problem=23
from Prime import prime3

ceiling = 28123
floor = 12

candidates = set(range(1, ceiling + 1))
abundent_numbers = []

for num in range(floor, (ceiling + 1 - floor)):
    if num < sum(prime3.factor_list(num)[:-1]):
        abundent_numbers.append(num)

while len(abundent_numbers) > 0:
    addend1 = abundent_numbers.pop()

    for addend2 in abundent_numbers:
        abundent_sum = addend1 + addend2
        if abundent_sum > ceiling:
            break
        if abundent_sum in candidates:
            candidates.remove(abundent_sum)
            
    double_addend = 2*addend1
    if double_addend <= ceiling:
        if double_addend in candidates:
            candidates.remove(double_addend)
            

answer = sum(candidates)

print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)
