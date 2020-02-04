'''
In OOP(Object Oriented Programming), when we define a class, we can inherit from an existing class. The new class is called a subclass, and the
inherited class is called a base class, or a superclass
'''
#Base class or Super class
class Animal(object):
    
    def run(self):
        print('Animal is running')

#SubClass 1
# class Dog(Animal):
#     pass
# #Subclass 2
# class Cat(Animal):
#     pass

#Test
# dog = Dog()
# dog.run()#Animal is running

# cat = Cat()
# cat.run()#Animal is running

'''
Whart are the benefits of inheritance? 
The biggest benefit is that the subclass gets the full functionality f the parent class. Because 'Dog' and 'Cat' ad its subclass have nothing
to do and automatically have the run() method
'''

'''
When the same run() method exists in the subclass and the parent class, the method 'run()' of subclass will overwrite the method 'run()'
of the parent class. When the code runs, the run() of the subclass will always be called. In this way, we get another benefit of inheritance:
polymorphism
'''
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):
     
     def run(self):
         print('Cat is running...')

#Test
# dog = Dog()
# dog.run()#Dog is running...

# cat = Cat()
# cat.run()#Cat is running...

#To understand the benefits of polymorphism, we need to write another function
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())#Animal is running x2
run_twice(Dog())#Dog is running... x2

'''
In fcat, any function or method that relies on 'Animal' as a parameter can run without modification because of polymorphism
'''

'''
For a variable, we only need to know that it is an 'Animal' type, and we can safely call the run() method without knowing its subclass,
wheather the specific run() method is applied to 'Animal', 'Dog', or 'Cat' on the instance, casue this is determined by the exact type of the
instance at runtime.
This is the real power of polymorphism: The caller only needs to call a function or method, regardless of details, and when we add a new 
subclass of 'Animal', just make sure that the run() method is written correctly no matter how the original code is called. This is the famous
'open and close' principle:
Open to extension: Allows to add 'Animal' subclass
Closed for modification: No need to modify functions such as run_twice()  that rely on 'Animal' type 
'''


'''
For a static language(such as Java), if you nedd to pass in an 'Animal' type, the object passed in must be an 'Animal' type or a subclass of it,
But for dynamic languages like Python, you don't necessarily need to pass in the 'Animal' type. We just need to ensure that the incoming object
has a run() method.
For example:

'''
class Timer(object):
    
    def run(self):
        print('Start...')

#Test:
run_twice(Timer())#Start... x2

'''
This is the 'duck type' of dynamic languages. It doesn't require a strict inheritance system. 
As long as an object "Looks like a duck and walks like a duck", it can be regarded as a duck
'''
