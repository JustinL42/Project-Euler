#!C:\Python33\python.exe
#https://projecteuler.net/problem=28

def square_subtotal(side_length):
    return 4 * side_length**2 - 6 * side_length + 6

def spiral_diagnal_sum(side_length):
    squares = range(3, side_length + 1, 2)
    subtotals = map(square_subtotal, squares)
    return sum(subtotals) + 1
    
answer = spiral_diagnal_sum(1001)

#print the answer and copy to clipboard
print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)