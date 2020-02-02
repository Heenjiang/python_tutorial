'''
Python's functools module provides many useful functions, one of which is the partial function. It should be noted that the partial function here is no the same as the partial function in 
the mathematical sense.
When introducing of parameters, you can reduce the difficulty of function calls. Partial functions can also do this. For example:
'''

#The int() function can convert a string into an integer. When only a string is passed in,the int() function converts to decimal by default
#However, the int() function also provides an additional base parameter. The default calue is 10. If you pass in the base parameter, you can do n-ary conversion
# print(int('12345', base=8))
'''
Suppose you want to convert a large number of binary strings. It is very troublesome to pass int(x, base=2) every time. So we thought that we could define a function of int2() and pass base=2
by default
'''
# def int2(x, base=2):
#     return int(x, base)
#In this way, it is very convenient for us to convert binary
# print(int2('10000'))

'''
functools.parital is to help us create a parital function. We don't need to define int2() by ourselves. We can use the following code to create a new function int2()
'''
import functools
in2 = functools.partial(int, base=2)
print(in2('1000'))
'''
When creating a partial function, you can actually receive 3 parameters: function object, *args, and **kw
int2 = functools.partial(int, base=2) adtually fixed the keyword parameter 'base' of the int() function, which is:int2('10010') is equivalent to: kw = {'base': 2}  int('10010', **kw)

max2 = functools.partial(max, 10)
max2(5, 6, 7)
is equivalent to:
args = (10, 5, 6, 7)
max(*args)

'''




