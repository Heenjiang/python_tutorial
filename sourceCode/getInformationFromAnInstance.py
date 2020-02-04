#When we get a reference to an object, how do we know waht type the object is and what methods are available?
#type() built-in function
#Basic types can be judged with type()
# print(type(123))#<class 'int'>
# print(type(None))#<class 'NoneType'>
#If a vaiable points to a function or class, you can also use type() to determine
# print(type(abs))#<class 'builtin_function_or_method'>
# print(type(123)==type(345))#True

#You can directly write int, str, etc. to determine the basic data type, but what if you want to determine whether an object is a function?
#Can use constants defined in the type() function
# import types
# def fn(object):
#     pass
# print(type(fn)==types.FunctionType)
# print(type(abs) == types.BuiltinFunctionType)
# print(type(lambda x: x) == types.LambdaType)
# print(type((x for x in range(10))) == types.GeneratorType)

#For class inheritance, using type() is very inconvienient. We need to determine the type of the class , we can use the isinstance() function
#isinstance(variable, ClassName)
#Basic types that can be judged with type() can also be judged with isinstance()
print(isinstance(123, int))
#And also you can determine whether a vaiable is one of some types. For example, the follwing code can determine whether it is a list or tuple
print(isinstance([1, 2, 3, 4], (list, tuple)))

#Always use isinstance() first to determine the type
#If you want to get all the properties and methods of an object, you can use the dir() function, which returns a list contains strings, for example
#get all properties and methods of a str object
print(dir('ABC'))