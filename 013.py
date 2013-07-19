#!C:\Python33\python.exe
#https://projecteuler.net/problem=13

sum = 0

for line in open('013_numbers.txt'):
    sum += float(line)

first_ten = str(sum).replace('.', '')[:10]

answer = first_ten

#boiler-plate code for printing the answer and
#copying it to the clipboard
print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)