#!C:\Python33\python.exe
#https://projecteuler.net/problem=25

sequence = [1, 1]

def latest_fibonacci():
	return sequence[-1]

def generate_next():
    global sequence
    next = sequence[-2] + sequence[-1]
    sequence.append(next)

def generate_fibonacci_over(num):
        while latest_fibonacci() <= num:
            generate_next()


generate_fibonacci_over(10**(1000 - 1) - 1)

answer = len(sequence)


#print the answer and copy to clipboard
print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)