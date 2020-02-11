'''
When we need to define the constants, one way is to use uppercae variable to define integers
such as months. The advantage is simplicity, the disadvantage is that the type is int, which
can be changed. Python provides the Enum class to achieve this function
'''
'''
Enumeration types can be regarded as a kind of label or series of constans, usually used to represent
some specific limited set, such as week, month, state, etc.
'''
# from enum import Enum

# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3

# print(Color.RED)
'''
The above code creats a basic enumeration example. Unlike our ordinary class, it inherits
the Eunm class.
When using a class to get property, the output is not its value, but is the enumeration items.
This makes the code more readable. 
'''
#Compared with ordinary classes, enumerated classes do not allow the values of enumerated items
#to be modified directly outside the class
#And we can try to modify the value of the label in eunmeration class
# Color.RED = 1#    raise AttributeError('Cannot reassign members.') AttributeError: Cannot reassign members.

#It is not allowed to have the same key value in the enumeration class
# from enum import Enum

# class Color(Enum):
#     RED = 1#    raise TypeError('Attempted to reuse key: %r' % key) TypeError: Attempted to reuse key: 'RED'
#     RED = 2
#     BULE = 2
#     GREEN = 3

#In an enumeration class, they can have same value, but subsequent enumeration items are aliaes
#of the first
# class Color(Enum):
#     RED = 1
#     BLUE = 1
#     GREEN =2

# print(Color.BLUE)#Color.RED

#If you do not want to the same value in the enumeration class. Enum class also provides the
#corresponding processing methods:
# from enum import Enum
# from enum import unique

# @unique
# class Color(Enum):
#     RED = 1
#     GREEN = 1
#     BLUE = 2#raise ValueError('duplicate values found in %r: %s' % ValueError: duplicate values found in <enum 'Color'>: GREEN -> RED


#Basic operation of enumeration
# from enum import Enum

# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3

# print(Color.BLUE.value)#3
# print(Color.BLUE.name)#BLUE

# for v in Color:
#     print(v)

'''
Color.RED
Color.GREEN
Color.BLUE
'''

#Iterate over enumerated classes with the same value
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    BLACK = 1

# for v in Color:
#     print(v)
'''
output:
Color.RED
Color.GREEN
Color.BLUE
'''

#As you can see, key names with the same value are not output. But if you want to output, use 
#the following method to traverse:
# for k, v in Color.__members__.items():
#     print(k, v)

'''
output:
RED Color.RED
GREEN Color.GREEN
BLUE Color.BLUE
BLACK Color.RED
'''

#Enumeration comparison operation
print(Color.BLACK == Color.RED)#True :because the value of RED and BLACK are equal
print(Color.BLACK is Color.RED)#True :because the value of RED and BLACK are equal

#Enumeration type conversion
'''
if a == 1:
    pass
elif a == 2:
    pass
'''

#The above code is not very readable, because we don't know what the 1 and 2 represent. But 
#it would be different if there were enumerated classes
'''
if a == Color.RED.value:
    pass
elif a == Color.GREEN.value:
    pass
'''

#Compared to the first code, the latter code is much more readable. 
#So how do we convert the value of an enum into the name of an enumeration?
#For example, a = 1
#the only thing you need to do is just pass the variable to the enumeration class
a = 1
print(Color(a))#Color.RED

