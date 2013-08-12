#!C:\Python33\python.exe
#https://projecteuler.net/problem=26

def repeating_digits(d):
    divisor = d
    dividend = 1
    repeat_tracking = {}
    digit = 0
    while True:
        while dividend < divisor:
            dividend *= 10
            digit += 1
        quotient = dividend//divisor
        segment = (dividend, quotient)
        dividend = dividend%divisor
        
        if dividend == 0:
            return 0
        
        if segment in  repeat_tracking:
            repeat_length = digit - repeat_tracking[segment]
            return repeat_length

        repeat_tracking[segment] = digit

record = 0
record_holder = 0

for number in range(100,1000+1):
    length = repeating_digits(number)
    if length > record:
        record = length
        record_holder = number
            
answer = record_holder

#print the answer and copy to clipboard
print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)