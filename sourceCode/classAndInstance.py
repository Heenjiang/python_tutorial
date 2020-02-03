'''
The most important concept of object-oriented is the 'Class' and 'Instance', we must keep in mind that classes are abstract templates
A class is a template for creatig instances, and an instance is a specific object. The data owned by each instance is independent of each other
and doesn't affect each other;
A method is a function that is bound to an instance. Unlikely ordinary functions, methods can directly access the data of the instance;
By calling the method on the instance, we directly manipulate the data inside the object, but do not need to know the implementation details 
inside the method;
Unlike static languages, Python allows you to bind any data to instance variable, that is,for two instance variables, although they are different
instances of the same class, they may have different variable names
'''

#Define a classs:
#class: keyword
#Student: class name
#object: base class or super class
# class Student(object):
#     pass
#Instantiate:
# bart = Student()
# print(bart)#<__main__.Student object at 0x007761C0>
#You can bind properties to an instance variable
# bart.name = 'Bart Simpson'
# print(bart.name)#Bart Simpson

'''
Since the class can serve as a template, you can force some properties that we think must be bound to be filled in when creating the instance
By defining a special method: __init()__, when creating an instance, assign values
'''
class Student(object):
    '''
    Note that the first parameter of the __init__ is always 'self', which indicates the created instance itself. Therefore, inside the  __init__
    method, you can bind various properties to 'self', because variable 'self' points to the created instance itself.
    Since there is the __init__() method, when creating an instance, you can not pass in empty parameters. You must pass parameters that match the
    __init__() method, but 'self' does not need to be passed. The Python interpreter itself will pass the instance variable into the __init__()
    method
    '''
    def __init__(self, name, score):
        self.name = name
        self.score = score
#Instantiate
bart = Student('Bart Simpson', 59)
print('Student\'s name:%s;\nStudent\'s score: %d' %(bart.name, bart.score))

