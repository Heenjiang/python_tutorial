'''
When you see a variable or a function name like __slot__ in the form of __xxx__, you must pay attention to these, cause in Python, they have 
special uses.
We already know how to use __slots__, and we also know that the __len()__ method is to allow the class to act on the len() function
In additionm, there are many such special-purpose functions in the Python class that can help us customize the class
'''

#__str__
'''
__str()__ in Python is like the toString() function of a class in Java, which returns basic information about yhe class, but the calling way
is slightly different.
'''
# class Student(object):

#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name

#test
# print(Student('Nicole'))
#However, if you don't use the print() function but directly typing the variable, the printed instance's informations are still not good-looking
'''
>>> s = Student('Michael')
>>> s
<__main__.Student object at 0x109afb310>
'''
# There is a lazy way:
# class Student(object):
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
    
#     __repr__ = __str__

# s =  Student('Nicole')
# print(s)

'''
__iter__
__next__
If a class wants to be used in a for...in loop, like the list or tuple, it must implement an __iter__() method, which returns an iteration
object. Then the for..in loop will continue to call the iteration object.  The __next()__ method gets the next value until it encounters a 
StopIteration error
'''
# class Fib(object):

#     def __init__(self):
#         self.a, self.b = 0, 1
    
#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 100:
#             raise StopIteration()
#         return self.a

#test
# for n in Fib():
#     print(n)

#__getitem__
#To behave like a list and take out elements by subscripts, you need to implement the __getitem__() method
# class Fib(object):

#     def __init__(self):
#         self.a, self.b = 0, 1
    
#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 100:
#             raise StopIteration()
#         return self.a

#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a , b = b, a + b
#         return a

# print(Fib()[10])

'''
But list has a magic slicing method
And why an error was reported for Fib?
The reason is that the parameter passed to __getitem__() may be an int or a slice object, so it is necessary to determine
'''
class Fib(object):

    def __getitem__(self, n):
        if isinstance(n, int):
            a , b = 1, 1
            for x in range(n):
                a , b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
fib = Fib()
print(fib[0:5])

'''
In short, through above methods, our own define class could behave like the same as the list, tuple and dictionary.
This is entirely due to "duck type" of the dynamic language, and there is no need to force inherite of any interface
'''

#__getattr__
'''
Under normal circumstance, when we call a class method or property, if it does not exist, an error will be reported.
To avoid this error Python has a mechanism to write a __getattr__() method that returns an attribute dynamically
'''
# class Student(object):

#     def __init__(self, name):
#         self._name = name
#     #When calling a non-existing property, such as score, the Python interpreter will try to call __getattr__(self, 'score') to try to get
#     #the property(attribute)
#     def __getattribute__(self, attr):
#         if attr == 'score':
#             return 90


#Return a function is also perfectly fine:
# class Student(object):

#     def __init__(self, name):
#         self._name = name
#     #When calling a non-existing property, such as score, the Python interpreter will try to call __getattr__(self, 'score') to try to get
#     #the property(attribute)
#     def __getattribute__(self, attr):
#         if attr == 'age':
#             return lambda: 25


# #test
# s = Student('Nicole')
# #But the calling way should be like this:
# print(s.age())

#Note that __getattr__ is called only if no attribute are found. Existing arrtibute, such as name, are not looked up in __getattr__
'''
In addition, notice that any call such as s.abs will return None, because the __getaatr__() we defined returns None by default. To make
the class respond to only a few specific attributes, we must throw an AttributeError according to the convention
'''

# class Student(object):

#     def __init__(self, name):
#         self._name = name
#     #When calling a non-existing property, such as score, the Python interpreter will try to call __getattr__(self, 'score') to try to get
#     #the property(attribute)
#     def __getattribute__(self, attr):
#         if attr == 'age':
#             return lambda: 25
#         else:
#             raise AttributeError('\'Student\' object has no attribute: \'%s\'' % attr)

'''
What is the practical effect of this fully dynamic invocation feature?
The effect is that it can be called for completely dynamic situations
For example: Restfull Api
Dynamicly generate :'/status/user/timeline/list'
'''

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    
    def __str__(self):
        return self._path

    __repr__ = __str__

#test
print(Chain().status.user.timeline.list)#/status/user/timeline/list

'''
An object instance can have its own properties and methods. When we call an instace's method, we use instance.method() to call it. 
Can it be called directly on the instance itself? In python, the answer is yes.
Any class, just need to define a __call__() method, you can directly call the instance
'''

class Student(object):

    def __init__(self, name):
        self.name = name
    
    def __call__(self):
        print('I\'m a student, and my name is: %s' % self.name)

#test
s = Student('Nicole')
s()#I'm a student, and my name is: Nicole