#!C:\Python33\python.exe
#https://projecteuler.net/problem=24
from math import factorial

n = 1000000
n -= 1
nth_perm = 0
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digits.sort()
permutations = factorial(len(digits))

while len(digits) > 0:
	division_size = permutations//len(digits)
	index = n//division_size
	nth_perm += (digits[index] * 10**(len(digits)-1))
	used_up = index * division_size
	permutations = division_size
	n -= used_up
	digits.pop(index)
	

answer = nth_perm

#print the answer and copy to clipboard
print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)
