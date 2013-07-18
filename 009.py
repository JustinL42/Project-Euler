import math

minc = int(math.floor(1000*math.sqrt(2)/(2+math.sqrt(2))))
maxc = 1000//2

count = 0
for c in range(minc, maxc):
  c2 = c**2
  for a in range(1, (1000-c)//2 + 1):
    count += 1
    if c2 == a**2 + (1000 - a -c)**2:
      print(a, (1000 - a -c), c)
      print('count:', count)

print('count:', count)