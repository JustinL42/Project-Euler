#!C:\Python33\python.exe
#https://projecteuler.net/problem=19

day = 3
count = 0

def count_if_sunday():
	global count
	if day % 7 == 1:
		count += 1

for year in range(1901, 2000+1):
	count_if_sunday()
	day += 31
	count_if_sunday()
	if year % 4 == 0:
		day += 29
	else:
		day += 28
	count_if_sunday()
	day += 31
	count_if_sunday()
	day += 30
	count_if_sunday()
	day += 31
	count_if_sunday()
	day += 30
	count_if_sunday()
	day += 31
	count_if_sunday()
	day += 31
	count_if_sunday()
	day += 30
	count_if_sunday()
	day += 31
	count_if_sunday()
	day += 30
	count_if_sunday()
	day += 31

answer = count

#print the answer and copy to clipboard
print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)
