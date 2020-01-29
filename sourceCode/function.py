# -*- coding: utf-8 -*-
#To call a function, you need to know the name and parameters of the function
#A function name is actually a reference to a function object. You can assign a function name to a variable, which is equivalent to
#an "alias" for this function
#P.S
# a = abs()
# a(-1)

#Use Python's built-in hex() function to convert an integer to a hexadecimal string
# n1 = 255
# n2 = 1000

# print('The hexadecimal representation of %d is %s' %(n1, hex(n1)))
# print('The hexadecimal representation of %d is %s' %(n2, hex(n2)))

# In Python, to define a function, use the def statement. Write the function name, parenthese, the parameters in parentheses, and the colon: ,
#Then, write the functin body in an indented block. The return value of the function is returned by return statement

# def my_abs(x):
#     if x >= 0 :
#         return x
#     else:
#         return -x

# print(my_abs(-99))

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0 :
#         return x
#     else:
#         return -x

# print(my_abs('a'))

# import math

# def move(x, y, step, angle):
#     x1 = x + step * math.cos(angle)
#     y1 = y + step * math.sin(angle)
#     return x1, y1

# # x, y = move(100, 100, 60, math.pi / 6)
# r = move(100, 100, 60, math.pi / 6)
# print(r)

# import math

# def quadratic(a, b, c):
#     if (not isinstance(a, (int, float))) and (not isinstance(b, (int, float))) and (not isinstance(a, (int, float))):
#         raise TypeError('parameters not valid')
#     else:
#         x1 = (-b + math.sqrt(b*b - 4*a*c)) / (2 * a)
#         x2 = (-b - math.sqrt(b*b - 4*a*c)) / (2 * a)
#         return x1, x2

# print(quadratic(2, 1, -3))

#Python's function definition is very simple, but it is very flexible. In addition to the normally defined mandatory parameters,
#you can also use default parameters, variable parameters, and keyword parameters, so that the interface defined by the function can 
#not only handle complex patameters, but also simplify the caller's code

# #1 Mandatory parameters
# def power(x, n):
#     s = 1
#     while n > 0:
#         s = s * x
#         n -= 1
#     return s
# print(power(5,2))

# #2 Default parameters P.S What are the benefits of using default parameters? 
# The biggest benefit is that it can reduce the difficulty of calling functions
# def power1(x, n=2):
#     if n == 2:
#         return x*x
#     else:
#         s = 1
#         while n > 0:
#             s = s * x
#             n -= 1
#         return s
# print(power1(2,3))

# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)

# enroll('Sarah', 'F')
# enroll('Bob', 'M', 7)
#When there are multiple default parameters, when calling , you can provide the default parameters in order, or you can provide some of
#the default parameters out of order. When some default parameters are not provided in order, you need to write the parameter name
# enroll('Adam', 'M', city='Tianjin')

#The default parameters are useful, but they can also fall into the pit if used incorrectly. The default parameter has a big pit, as
#demonstrated below
# def add_end(L=[]):
#     L.append('End')
#     return L

# #When you call normally, the result seems to be good
# print(add_end([1, 2, 3]))
# print(add_end(['X', 'Y', 'Z']))

# #When you call with default parameters, the result is right at first
# print(add_end())
# #But when 'add_end()' is called again, the result is wrong
# print(add_end())

#Why this happen when 'add_end()' function is called at second time?
#Here is the explanation:
#When a Python function is defined, the value of the default parameter 'L' is calculated->[], because the default parameter 'L' is 
#also a variable that points to the object->[]. Each time the function is called, if the content of 'L' is changed. The content of the
#default parameters will change the next time it is called, and it will no longer be [] when the function is called



#!!!!!!! One thing to keep in mind when defining default parameters: default parameters must point to immutable objects!!

#To modify the above example, we can use the immutable object 'None':
# def add_end1(L=None):
#     if L is None:
#         L = []
#     L.append('End')
#     return L
# #Now, no matter how many times it is called, there will be no problem
# print(add_end1())
# print(add_end1())


#In Python functions, you can also define variable parameters. As the name implies, a variable number of parameters passed in, which
#can be one, two to any, or zero.

#Let us take a math problem as an example. Given a set of numbers: a, b, c..., please calculate a2+b2+c2+.... 
#1st method: To define this function, we must determine the input parameters.Since the number of parameters is uncertain, we first thought
#that we could pass in a, b, c... as a list or tuple. In this way, the function can be defined as follows:
# def my_calcuate(numbers):
#     sum = 0
#     for n in numbers:
#         sum += n * n
#     return sum
# #call this function:
# print(my_calcuate([1, 2, 3, 4]))
# print(my_calcuate((1, 2, 3, 4)))

# Change function parameters to variable 
# def my_calcuate(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n * n
#     return sum
# #If you use variable parameters, the way to call a function can be simplified to this
# print(my_calcuate(1, 2, 3, 4))
# #What if you already have a list or tuple?
# num = [1, 2, 3, 4]
# print(my_calcuate(*num))
# *num means that all elements of the num list are passed as variable parameters. This notation is quite useful and common

#Keyword parameters allow you to pass in zero ot any number of parameters with parameter names. These keyword parameters are
#automatically assembled into a dictionary inside the function
# def person(name, age, **kw):
#     print('name', name, 'age', age, 'other', kw)
# #The function person accepts the keyword parameters kw in addition to the required parameters name and age. 
# #When calling this function, you can only pass in the required parameters
# person('Hoen', 22)# result:name Hoen age 22 other {}
# #You can also pass in any number of keyword parameters
# person('Nicole', 23, city='Amsterdam', country='Netherland')#result:name Nicole age 23 other {'city': 'Amsterdam', 'country': 'Netherland'}

#Similar to variable parameters, you can also assemble a dictionary data structure first, and then convert the dictionary into keyword
#parameters and pass in
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, city=extra['city'], job=extra['job'])

#Of course, the above complex calls can be simplified
# extra = {'city': 'Dublin', 'job': 'Software Engineer'}#result:name Hoen age 24 other {'city': 'Dublin', 'job': 'Software Engineer'}
# person('Hoen', 24, **extra)
#**extra means that all key-values of this dictionary are passed to the functions's **kw parameters with keyword parameters. KW will get
#a dictionary. Note that the dictionary obtained by kw is a copy of extra. The changes to kw are not will affect extra outside the function

#If you want to restrict the names of keyword parameters, you can use named keyword parameters
#Unlike the keyword parameters **kw, named keyword parameters require a special delimiter*, and parameters after * are treated as named
#keyword parameters
# def person(name, age, *, city, job):
#     print('name:', name, 'age:', age, 'city:', city, 'job:',job)#result:name: Hoen age: 24 city: Dublin job: Software Engineer
# #call this function
# person('Hoen', 24, city='Dublin', job='Software Engineer')
#If there is already a variable parameter in the function defination, the following named keyword parameter no longer needs a special 
# #separater *
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)
# #call this function
# person('Hoen', 24,'handsome', 'funny', city='Dublin', job='Software Engineer')
#Named keyword parameters must be passed in a parameters name, which is different from positional parameters. If no named parameter is 
#passed, the call will report an error

#Named keyword parameters can have default values, simplifying the call
# def person(name, age, *, city='Dublin', job):
#     print(name, age, city, job)
# #call this function
# person('Hoen', 24, job='Software Engineer')#result:Hoen 24 Dublin Software Engineer
#!!!! When using named keyword parameters, pay special attention. If there are no variable parameters, you must add * as a special
#delimiter. If * is missing, the Python interpreter will not recognize positional parameters and named keyword parameters


#The order of parameter definition must be: required parameters, default parameters, variable parameters, and keyword parameters

#task : calculate the product of two numbers, please modify it a bit to accept one or more numbers and calculate the product

# def my_product(*numbers):
#     if(len(numbers)==0):
#         raise TypeError('Only one number cannot generate product')
#     else:
#         sum = 1
#         for n in numbers:
#             sum *= n
#         return sum
# #call this function
# print(my_product(1))
    
