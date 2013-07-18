#!C:\Python33\python.exe
#https://projecteuler.net/problem=11
from tkinter import Tk

grid = []

for line in open('011_grid.txt'):
    grid.append(list())
    for i in range(0, len(line), 3):
        grid[-1].append(line[i:i+2])
        
largest_product = 0

def check_product(lst):
    global largest_product
    product = 1
    for num in lst:
        product *= int(num)
        
    largest_product = max(product, largest_product)

line_len = 4
    
#check columns
for x in range(len(grid[0])):
    for y in range(len(grid) + 1 - line_len):
        column = []
        for i in range(line_len):
            column.append(grid[x][y+i])
            
        check_product(column)
        
#check rows
for x in range(len(grid[0]) + 1 - line_len):
    for y in range(len(grid)):
        row = []
        for i in range(line_len):
            row.append(grid[x+i][y])
            
        check_product(row)
        
#check bajas (shorthand for diagnal top-left to 
#bottom-right element analagous to "row" and "column"
for x in range(len(grid[0]) + 1 - line_len):
    for y in range(len(grid)+ 1 - line_len):
        baja = []
        for i in range(line_len):
            baja.append(grid[x+i][y+i])
            
        check_product(baja)
        
#check japans (shorthand for diagnal bottom-left to 
#top-right element analagous to "row" and "column"
for x in range(line_len -1, len(grid[0])):
    for y in range(len(grid)+ 1 - line_len):
        japan = []
        for i in range(line_len):
            japan.append(grid[x-i][y+i])
            
        check_product(japan)


answer = largest_product

#boiler plate text for printing the answer 
#and copying it to the clipboard
print(answer)
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)