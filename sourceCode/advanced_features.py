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
d = {'a': 1, 'b': 2, 'c': 3}
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








