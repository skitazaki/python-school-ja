print('=' * 40 )
a, b = 1,2
def p(a, b):
    print("a=%d, b=%d, a+b=%d" %  (a, b, a + b))
p( a, b)
if a < b :
  a, b = b, a
p(a, b+ 1)
import os, sys
