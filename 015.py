#!C:\Python33\python.exe
#https://projecteuler.net/problem=15
grid_length = 20 + 1
grid = [list()]*grid_length
grid[0] = [1]*grid_length

for row in range(1, grid_length):
	row_length = grid_length - row
	grid[row] = [0]*(row_length)
	grid[row][row_length - 1] = 2*grid[row - 1][row_length - 1]
	for column in range(row_length - 2, -1, -1):
		grid[row][column] = grid[row -1][column] + grid[row][column + 1]

answer = grid[-1][-1]

print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)
