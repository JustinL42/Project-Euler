#!C:\Python33\python.exe
import sys

def primegen(number, stepsize):
  import math
  stepsize = min(stepsize, number-1)
  print('stepsize:', stepsize)
  prime_list = []
  startnum = 2
  endnum = stepsize + startnum
  num_array = [True]*(stepsize)
  while True:
    #reset the num_array
    if startnum > 2:
      for state in num_array:
        state = True
    
    #go through primelist
    for prime in prime_list:
      first_composite = max(math.ceil(startnum/prime)*prime, prime**2)
      for composite in range(first_composite, endnum, prime):
        try:
          num_array[composite-startnum] = False
        except IndexError:
          print('out of bounds')
          # print('prime:', prime)
          # print('first_composite:', first_composite)
          # print('startnum:', startnum)
          # print('endnum:', endnum)
          # print('composite:', composite)
          return prime_list
        
    #check current primearray 
    if startnum == 2:
      for num in range(startnum, endnum):
        if num**2 > endnum-1:
          break
          
        if num_array[num-startnum]:
          for factor in range(num**2, endnum, num):
            num_array[factor-startnum] = False

    #extract primes from the array
    for num in range(startnum, endnum):
      if num_array[num-startnum]:
        prime_list.append(num)
        #print(len(prime_list))
    
    if endnum < number+1:
      startnum, endnum = endnum, endnum+stepsize
    else:
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
