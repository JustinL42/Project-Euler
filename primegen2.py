#!C:\Python33\python.exe
import sys

def primegen(number, stepsize, prime_list=[]):
  import math

  if len(prime_list) == 0:
    startnum = 2
  else:
    startnum = prime_list[-1]
  stepsize = min(stepsize, number+1-startnum)
  print('stepsize:', stepsize)
  endnum = stepsize + startnum
  num_array = []
  num_set = {}
  while True:
    #reset the num_set
    if startnum == 2:
      num_array = [True]*(stepsize)
      #check current primearray 
      for num in range(startnum, endnum):
        if num_array[num-startnum]:
          for factor in range(num**2, endnum, num):
            num_array[factor-startnum] = False
        
      #extract primes from the array
      for num in range(startnum, endnum):
        if num_array[num-startnum]:
          prime_list.append(num)
      
    else:
      print(5)
      num_set = set(range(startnum, endnum))
      print(5.25)
      #go through primelist
      for prime in prime_list:
        first_composite = max(math.ceil(startnum/prime)*prime, prime**2)
        num_set -= set(range(first_composite, endnum, prime))
      
      print(5.75)
      prime_list.extend(num_set)
      print(6)

    if endnum < number+1:
      startnum, endnum = endnum, endnum+stepsize
    else:
      prime_list.sort()
      return prime_list

if __name__ == '__main__':
  try:
    number = int(sys.argv[1])

  except IndexError:
    print('This function requires an integer')
    print('e.g. primegen 1305')
  else:
    try:
      step_size = int(sys.argv[2])
    except IndexError:
      step_size = 1000000
    print(primegen(number, step_size))
