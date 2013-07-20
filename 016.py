#!C:\Python33\python.exe
#https://projecteuler.net/problem=16
num = 2**1000
str = str(num)

sum = 0

for char in str:
	sum += int(char)

answer = sum

print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)
