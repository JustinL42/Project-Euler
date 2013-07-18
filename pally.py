#!C:\Python33\python.exe
import sys

def is_pallindrome(sequence):
  if len(sequence) == 1:
    return True
  if sequence[0] != sequence[-1]:
    return False
  if len(sequence) == 2:
    return True
  return is_pallindrome(sequence[1:-1])


if __name__ == '__main__':
  try:
    seq = sys.argv[1]

  except IndexError:
    print('This function requires an sequence')
    print('e.g. pally.py (1305)')
  else:
    print(is_pallindrome(str(seq)))
