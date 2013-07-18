#!C:\Python33\python.exe
#https://projecteuler.net/problem=4
import pally
import pickle

x = 999
y = 999

lst = []
mlt = []

for x in range(999,99,-1):
  for y in range(999,x-1,-1):
    if pally.is_pallindrome(str(x*y)):
      lst.append(x*y)
      mlt.append((x,y))
      mlt.append((y,x))

f = open('f.txt', 'w')

for x, y in mlt:
  f.write('{}, {}\n'.format(x, y))
pickle.dump(mlt, f)
print(max(lst))



# def idec(i, j):
  # i -= 1
  # print(i, j)
  # if pally.is_pallindrome(str(i*j)):
    # print i*j
    # return None
  # else:
    # jdec(i, j)
    
    
# def jdec(i, j):
  # j -= 1
  # print(i, j)
  # if pally.is_pallindrome(str(i*j)):
    # print i*j
    # return None
  # else:
    # idec(i, j)

    

    
# eye, jay = 999, 999

# idec(eye, jay)