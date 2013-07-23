#!C:\Python33\python.exe
#https://projecteuler.net/problem=20
from math import factorial

string_fact = str(factorial(100))
sum = 0

for char in string_fact:
	sum += int(char)

answer = sum

#print the answer and copy to clipboard
print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)
