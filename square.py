from math import *
def my_sqrt(a):
  x = 3
  while True:
     y = (x + a/x) / 2
     if y == x:
        break
     x = y
  return float(x)



def test_sqrt(a):
    a = 1
    while a <= 25:
        diff = abs(my_sqrt(a) - sqrt(a))
        print( "a = ", a)
        print("my_sqrt: ", my_sqrt(a))
        print("math.sqrt: ", sqrt(a))
        print("diff: ", diff)
        a = a + 1


test_sqrt(1)
