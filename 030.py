#!C:\Python33\python.exe
#https://projecteuler.net/problem=30
 
exponent = 5
upto = 10**(exponent+1)
special_sum = 0
num = 2

while num < upto:
    result = sum([int(digit)**exponent for digit in str(num)])
    if result < num:
        num += 1
    elif result > num:
        exp = 1
        while True:
            incr = 10**exp
            num = ((num + incr)//incr)*incr
            if num >= sum([int(digit)**exponent for digit in str(num)]) or num > upto:
                break
            exp +=1  
    else:
        special_sum += num
        print(num)
        num += 1

answer = special_sum

#print the answer and copy to clipboard
print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)