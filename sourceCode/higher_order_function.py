# -*- coding: utf-8 -*-
# Higher-order functions
# What is a Higher-order functions>
# Since a variable can point to a function and its parameters can receive variables, then a function can receive another function as a parameter.
# this kind of function is called a higher-order function
# def add(x, y, f):
#     return f(x) + f(y)
# print(add(-5, 6, abs))

#Let's look at the map first. The map() function accepts two parameters, a function and an Iterable. The map applies the passed function to 
#each element of the sequence in turn and returns the results as a new Iterator
#For example, if we have a function f(x) = x2, to apply this function to a list[1, 2, 3, 4, 5], we can use map(). The implementation is as 
#follow:

# def f(x):
#     return x * x
# r = map(f, [1, 2, 3, 4, 5])
# lr = list(r)
# print(lr)

#From the above loop code, you can understand at a glance: apply f(x) to each element of the list and generate a new list
#Therefore, map() is a higher-order function. In fact, it abstracts the rules of operation. Therefore, we can not only calculate simple f(x) = x2
#but also calculate any complex functions. For example, turning all the numbers in this list As a string

# print(list(map(str, [1, 2, 3, 4, 5, 6])))

#Reduce applies a function to a sequence[x1,x2,x3....]. This function must receive two parameters. Reduce continues the result and performs 
#the cumulative calculation with the next element of the sequence. The effect is:reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# from functools import reduce
# def add(x, y):
#     return x + y
# print(reduce(add, [1, 2, 3, 4, 5]))

#Convert the sequence [1, 3, 5, 7, 9] into an integer 13579
# from functools import reduce
# def convert(x, y):
#     return x * 10 + y 
# print(reduce(convert, [1, 3, 5, 7, 9]))

#The above example itself is not very useful, but if you consider that the string is also a sequence, with a slight modification to the above
#example, with map(), we can write a function that converts string to integer

# from functools import reduce
# def fn(x, y):
#     return x * 10 + y
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
# print(reduce(fn, list(map(char2num, '13579'))))

#The function organized into a str2int is:
# from functools import reduce
# digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return digits[s]
#     rs = reduce(fn, map(char2num, s))
#     return rs
# print(str2int('13579'))

#TASK 1: Use the map() to change the non-standard English name entered by user into the initial capital letter and other lower-case normal names
# def normalize(name):
#     return str.upper(name[:1]) + str.lower(name[1:])
# standardNames = map(normalize, ['adam', 'LISA', 'barT'])
# print(list(standardNames))

#TASK 2: Please write a prod() function that can take a list and use reduce() to multiply
# from functools import reduce
# def prod(l):
#     def multi(x, y):
#         return x * y
#     return reduce(multi, l)
# print(prod([3, 5, 7, 9]))

#TASK 3: Use a map and reduce to write a str2float function that converts the string '123.456' into a floating point number 123.456
# from functools import reduce
# def str2float(s):
#     if isinstance(s, str) == False:
#         raise TypeError('The parameter must be string type')
#     def integerPart(x, y):
#         return x * 10 + y
#     def decimalPart(x, y):
#         return x / 10 + y
#     intPart, deciPart = s.split('.')#Split str into two sunstrings based on '.'
#     deciPart = deciPart[::-1]
#     a1 = reduce(integerPart, map(int, intPart))
#     a2 = reduce(decimalPart, map(int, deciPart))
#     rs = a1 + a2 / 10
#     return rs
# print(str2float('123.456'))

#Python's built-in filter () function is used to filter sequences. 
#filter () applies the passed function to each element in turn, 
#and then decides whether to keep or discard the element based on whether the return value is True or False. 
#It can be seen that the high-order function of filter () is to correctly implement a "filter" function. 
#Note that the filter () function returns an Iterator, which is a lazy sequence, 
#so to force filter () to complete the calculation result, you need to use The list () function gets all the results and returns a list.
# def is_odd(n):
#     return n % 2 == 1
# print(list(filter(is_odd, [1, 2, 3, 4, 5])))

# def not_empty(s):
#     return s and s.strip()
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

#The key to using filter() as a higher-order function is to correctly implement a 'filter' function
#Note that the filter() function returns an Iterator, which is lazy seuquence, so to force the filter() to complete the calculation results
#you need to use the list() function to obtain all the results and return the list
'''
One method for calculating prime numbers is the Escher-sieve method, whose algorithm is very simple to understand:

First, list all natural numbers starting from 2, and construct a sequence:

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

Take the first number 2 of the sequence, which must be a prime number, and then use 2 to filter out multiples of 2 of the sequence:

3, 5, 7, 9, 11, 13, 15, 17, 19,...

Take the first number 3 of the new sequence, which must be a prime number, and then use 3 to filter out multiples of 3 of the sequence:

5, 7, 11, 13, 17, 19,...

Take the first number 5 of the new sequence, and then use 5 to sift out multiples of 5:

7, 11, 13, 17, 19,...

Keep sifting down to get all the prime numbers.

'''
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# def _not_divisible(n):
#     return lambda x: x % n >0
# def primes():
#     yield 2
#     it = _odd_iter()
#     while  True:
#         n = next(it)
#         if n > 500:
#             break
#         yield n
#         it = filter(_not_divisible, it)
# for n in primes():
#     print(n)

#TASK 1:The palindrome is a number that no matter read from left to right or right to left, both are same, such as 12321....
#Please use filter() to filter out the palindrome numbers
# def is_palindrome(n):
#     return str(n) ==  str(n)[::-1]

# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def sort(L):
#     def by_name(t):
#         return t[0]
#     def by_score(t):
#         return t[1]
#     print('sorting by name:', sorted(L, key=by_name))
#     print('sorting by score:', sorted(L, key=by_score, reverse=True))
# sort(L)