'''
When we define a class and create an instance of the class, we can bind any property and method to the instance. This is the flexibility of 
the dynamic language. What if want to limit the properties of the instance? For example, only 'name' and 'age' attributes can be added to Student
instances
'''
class Student(object):
    __slots__ = ('name', 'age')

#Test 
s = Student()
s.name = 'Michael'
s.age = 16
#s.score = 99#AttributeError: 'Student' object has no attribute 'score'
'''
Because 'score' has not been palced in __slots__. you cannot bind the 'score' attribute to 'Student' class, and then attempting to bind 'score'
will get an AttributeError.
Note that the attributes defind using __slots__, __slots__ only work on the current class instance, and do not work on inherited sunclass,
Unless the __slots__ in also defined in the subclass, the arrtibutes allowed to be defined in the subclass are its own __slots__ plus the 
parent's __slots__
'''