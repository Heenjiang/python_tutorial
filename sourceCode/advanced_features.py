#For this kind of operation that often takes the specified index range, the loop is very tedious. Therefore, Pyhton provides the Slice
#operator, which can greatly simplify this operation
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[0:3])#print(L[:3])
# #L[0:3] indicates that is starts at index 0 and ends at index 3, but does not include index 3. That is, the index 0,1,2 is exactly 3 
# #elements. If the first index is 0, it can also be omitted

# #Similarly, since Python supports L[-1] to take the penultimate element, it also supports the penultimate slice
# print(L[-2:])#Remember that the index of the penultimate
# print(L[-2:-1])

# L = list(range(100))

# print(L[:10:2])
# print(L[::5])
# #Copy a list
# print(L[:])

#A tuple is also a list, the only difference is that the tuple is immutable. Therefore, tuple can also be sliced, but the result of
#the operation is still tuple
# T = (0, 1, 2, 3, 4)
# print(T[:3])

#The string 'xxxx' can also be regarded as a list, and each element is a character. Therefore,strings can also be sliced, but the 
#result is still a string
# my_str = 'ABCDEFG'
# print(my_str[:3])

#Summary: In many programming languages, a variety of interception function are provided for strings(for example, substring), in fact,
#the purpose is to slice string. Python has no interception function for strings. It only needs a slicing operation, which is very simple



#TASK: Use the slice operation to implement a trim() function that removes spaces at the beginning and end of the string.
#Be careful not to call the strip() method of strings

# def trim(s):
#     #Inspecting parameter's type
#     if isinstance(s, str) == False:
#         raise TypeError('The parameter must be a string')
#     #Determine if it is an empty string
#     if len(s) == 0:
#         return ''
#     #Removing the beginning spaces
#     if s[0:1] == ' ':
#         while s[0:1] == ' ':
#             s = s[1:len(s)]
#             #If the string is all spaces
#             if s == '':
#                 return ''
#     #Removing the trailing spaces
#     if s[-1:] == ' ':
#         while s[-1:] == ' ':
#             s = s[:len(s)-1]
#     #Retrun the result
#     return s
# print(trim(1))


#If a list or tuple is given, we can traverse the list or tuple throught a for loop. This kind of traversal is called interation
#In Pyhton, iteration is done by for...in, and in many language such as C, iteration is done by subscripting.
#It can be seen that Python's for loop is more abstract than C's for loop, because Python's for loop can be used not only on list or
#tuple, but also on other iterable objects.
#Although the data type of list has subscripts, many other data types have no subscripts. However, as long as it is an iterable object,
#is can be iterated with or without subscripts, such as dictionary
# d = {'a': 1, 'b': 2, 'c': 3}
#Because the storage of dictionary is not arranged in the order of list, the result order of iteration is likely to be different each time
# for key in d:
#     print(key)
# #iterating value
# for value in d.values():
#     print(value)
# #Iterate key and value simultaneously
# for key, value in d.items():
#     print(key,' ', value)

#SO HOW DO YOU DETERMINE IF AN OBJECT IS AN ITERABLE OBJECT?
#Answer: Through the iterable type of the collection module

# from collections import Iterable
# print(isinstance('abs', Iterable))

#What if you want to implement a subscript loop like Java on a list?
#Answer: Python's built-in enumerate function can turn a list into an index-element pair, so that you can iterate both the index and
#the element itself in a for loop
# for i, value in enumerate(['a', 'b', 'c']):
#     print(i,' ', value)
# #Two varibles are referenced at the same time, which is very common in Python
# for x,y in [(1,1), (2,4), (3,9)]:
#     print(x,' ',y)

#TASK: Please use iteration to find the minimum and maximum values in a list and return a tuple
# def findMinAndMax(L):
#     #Check if the elements in the list are valid
#     for e in L:
#         if isinstance(e,(int, float)) == False:
#             raise TypeError('All elements in the list must be int or float type')
#     #Check the length of list
#     if len(L) < 2:
#         raise TypeError('Length of the list must be greater than 2')
#     #Initialize variables
#     min = L[0]
#     max = L[0]
#     #Iterating 
#     for e in L:
#         if max < e:
#             max = e
#         if min > e:
#             min = e
#     #return the result in tuple data type
#     return min, max
# print(findMinAndMax([3,5,1,5,0,78,35,67,24]))

#List comprehensions is a very simple but powerful built-in generator that can be used to create list
#How to generate [x*x,....]
# L = [x * x for x in range(1,11)]
# print(L)
#Filter out even squares only
# L = [x * x for x in range(1, 11) if x % 2 == 0]
# print(L)
#You can also use a two-layer loop to generate a full permutation
# L = [m + n for m in 'ABC' for n in 'XVZ']
# print(L)
#Using list generators, you can write very concise code. For example, listing all file and directory names in the current directory 
# #can be achieved with a single line of code
# import os
# print([d for d in os.listdir('.')])#os.listdir can list files and dictionary
#List comprehensions can also use two variables to generate a list
# d = {'x' : 'A', 'y' : 'B', 'z' : 'C'}
# print([k + '=' + v for k, v in d.items()])
#Finally, make all the strings in a list to lowercase
# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])
#TASK:  If the list contains both strings and intergers, there is no lower() method for non-string types, so the list generator will 
#report an error. Please modify the list generator to ensure that it can be executed correctly
# L = ['Hello', 'World', 12, 'Apple']
# print([s.lower() for s in L if isinstance(s,str)])

#With list comprehension, we can directly create a list. However, due to memory limitations, the list size is definitely limited. 
#Moreover, if you create a list of 1 million elements, it takes a lot of storage space. If we only need to access the first few elements
#the space occupaied by the vast majority of the latter elements will be wasted.
#So if the list elements can be deduced according to some algorithm, can we continously calculate the subsequent elements during the loop?
#This eliminates the need to create a complete list, which saves a lot of space. In python, this mechanism of looping while computing is
#called generator
# g = (x * x for x in range(10))
# print(g)
#Get the next return value of the generator through the next() function
# print(next(g))
#We said that the generator saves the algorithm. Each time next(g) is called, the value of the next element of g is calculated.
#Until the last element is calculated. When there are no more elements, a StopIteration error is thrown
#Of course, the above continuous call next(g) function is too perverted. The correct way is to use a for loop, because the generator is
#also an iterable object
# for n in g:
#     print(n)
#The generator is very powerful. If the calculation algorithm is kind of complicated, when a for loop similar to the list comprehension
#method cannot be implemented, you can also use functions to implement
#For example, the famous Fibonacci sequence, except for the first and second numbers, any number can be obtained by adding the two 
#numbers before it
#The Fibonacci sequence cannot be generated by using list comprehension, but it is easy to implement using functions
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n += 1
#     return 'done'
#Looking closely, it can be seen that the fib functiion actually defines the calculation rules of the Fibonacci sequence. 
#It can start from the first element and calculate any subsequent elements. This logic is actually very similar to a generator
#To turn the fib function into a generator, just change print(b) to yield b:
#This is another way to define a generator. If a function defination contains the yield keyword, the function is no longer a normal
#functionm but a generator

# def fib_generator(max):
#     n, a, b = 0, 0 ,1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n += 1
#     return 'done'

#Here, the hardest thing to understand is that the execution flow of generators and functions is different. Functions are executed 
#subquentially, and return when they encounter a return statement or the last line of function statements.
#The generator is executed every time when next(g) is called, and it returns when it encounters a yield statement. And when it is
#executed again, it continues to execute from the yield statement that was last returned

#But when calling the generator with a for loop, the return value of the generator's return statement cannot be obtained.
#If you want to get the return value, you must catch the StopIteration error.The return value is contained in the StopIteration value
# g = fib_generator(6)
# while True:
#     try: 
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value is:', e.value)
#         break

#TASK: Yang Hui triangle

# def yangHui_triangle(max):
#     L = [1]
#     S = []
#     n = 0
#     while n < max:
#         yield L
#         L = [1] + S +[1]
#         n += 1
#         S = []
#         for i in range(len(L) - 1):
#             S.append(L[i] + L[i+1])

# g = yangHui_triangle(6)
# for i in g :
#     print(i)

#We already know that there are sveral types of data that can be directly applied  to the for loop:
# one is the collection data type, such as list, tuple, dictionary, set, str,etc.;
# one is generator, which includes generator and generator function with yield keyword.
#These objects that can directly act on the for loop are called Iterable objects
#You can use isinstance() to check whether an object is an iterable object
# from collections import Iterable
# print(isinstance([], Iterable))
# print(isinstance({}, Iterable))
# print(isinstance('abc', Iterable))
# print(isinstance((), Iterable))

#The generator can not only operate on the loop, but also can be continuously called by the next() function and return the next value,
#until the StopIteration error is finally thrown to indicate that the next value cannot be returned
#An object that can be called by the next() function and keeps returning the next value is called an Iterator
#You can use isinstance() to check wheather an object is an Iterator.
from collections import Iterator
# print(isinstance((x for x in range(10)), Iterator))

#Generators are Iterator objects, but although list, and str are Iterable, they are not Iterators
#You can use the iter() function to turn list, dictionary, str, etc. Iterable object into Iterator
print(isinstance(iter([]), Iterator))
#You may ask, why aren't list, dictionary, str and other data types other than Iterator?
#This is because Python's Iterator represents a data stream
#Iterator objects can be called by next() and return the next value until a StopIteration error is thrown when there is no data
#You can think of the data stream as an ordered sequence, but we can't know the length of the sequence in advance. We can ony get the next value
#through next() function, so the calculation of Iterator is lazy, only when it is needed it will be calculated.
# Iterator can even represent an infinitely large data stream, such as all natural numbers. And using a list is never possible to store all 
# natual numbers 