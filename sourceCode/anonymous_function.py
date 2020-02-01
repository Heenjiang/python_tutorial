# -*- coding: utf-8 -*-
'''
When we pass in a function, sometimes it is not necessary to explicitly define the function, it is more convenient to pass in the anonymous function
directly. 
In python, limited support is provided fot anonymous functions. Take the map() function as an example. When calculating f(x) = x2, in 
addition to defining a function for f(x), you can also directly pass in an anonymous function
'''
# anonymous_function = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6]))
# print(anonymous_function)

'''
The keyword lambda indicates an nonymous function, and the x before the colon indicates a function parameter.
One limitation of anonymous function is that there can only one statement. You do not need to write return value is the result of the expression
There is a benefit to using anonymous functions, because functions have no names, so you don't have to worry about function name conflicts.
In addition, an anonymous function is also a function object, You can also assign an anonymous function to a variable, and then use the vaiable
to call the function
'''
# f = lambda x: x * x
# print(f)#<function <lambda> at 0x003502B0>
# print(f(5))#25

'''
Similarly, you can return anonymous functions as return values
'''
# def build(x, y):
#     return lambda: x * x + y * y
# f = build(1,2)
# print(f)#<function build.<locals>.<lambda> at 0x010E0268>
# print(f())#5

'''
Please transform the following code with anonymous functions
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
'''

# L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
# print(filter(lambda n: n % 2 == 1, range(1, 20)))#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]