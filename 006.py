#!C:\Python33\python.exe
#https://projecteuler.net/problem=6
from Prime import prime3

sumofsquares = 0
for i in range(1,100+1):
    sumofsquares += i**2
    
squareofsum = 0
for i in range(1,100+1):
    squareofsum += i
    
squareofsum = squareofsum**2

print(squareofsum - sumofsquares)
