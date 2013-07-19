#!C:\Python33\python.exe
#https://projecteuler.net/problem=14
from tkinter import Tk

steps = {0:0, 1:1}
largest_collatz = 0
startnum = 1
while startnum < 1000000:
    num = startnum
    chain = []
    while True:
        if num in steps:
            cached_answer = steps[num]
            for i in range(len(chain)):
                steps[chain[i]] = cached_answer + len(chain) - i
                
            break
        else:
            chain.append(num)
            if num % 2 == 0:
                num /= 2
            else:
                num = num*3 + 1
    
    if steps[startnum] > steps[largest_collatz]:
        largest_collatz = startnum
        
    startnum += 1


answer = largest_collatz

#boiler-plate code for printing the answer and
#copying it to the clipboard
print(answer)
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)