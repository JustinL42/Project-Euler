#!C:\Python33\python.exe
#https://projecteuler.net/problem=22

f = open('022_names.txt', 'r')
names_string = f.read()
names_list = names_string[1:-1].split('","')
names_list.sort()
total_name_score = 0

for index in range(len(names_list)):
	name_score = 0
	for char in names_list[index]:
		name_score += (ord(char) - 64)
	name_score *= (index + 1)
	total_name_score += name_score

answer = total_name_score

#print the answer and copy to clipboard
print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)
