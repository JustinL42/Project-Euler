#!C:\Python33\python.exe
#https://projecteuler.net/problem=18

f = open('018_triangle.txt', 'r')
triangle = list(f)

class Node:    

    def __init__(self, ln, indx):
        self.line = ln
        self.index = indx
        self.value = int(triangle[ln][indx:indx+2])
    
    def left(self):
        left_node = Node(self.line + 1, self.index)
        return left_node
        
    def right(self):
        right_node = Node(self.line + 1, self.index + 3)
        return right_node
        
root = Node(0, 0)
path = []
frontier = [root]
best_path = []
best_total = 0

while len(frontier):
    node = frontier.pop()
    path.append(node.value)
    if node.line < len(triangle) - 1:
        frontier.append(node.left())
        frontier.append(node.right())
    else:
        total = sum(path)
        if total > best_total:
            best_total = total
            best_path = path
        if len(frontier):
            backtrack_to = frontier[-1].line
            path = path[:(backtrack_to)]
        

answer = best_total

print(answer)
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(answer)
