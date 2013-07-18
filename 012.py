#!C:\Python33\python.exe
#https://projecteuler.net/problem=12
from tkinter import Tk
from Prime import prime3

triangle  = 0
number = 0
while True:
  number += 1
  triangle += number
  factors  = prime3.factorize(triangle)
  unique_divisors = 1
  for exponent in factors.values():
    unique_divisors *= (1+exponent)

  if unique_divisors > 500:
    answer = triangle
    break
  

#boiler plate code for printing the answer 
#and copying it to the clipboard
print(answer)
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)
