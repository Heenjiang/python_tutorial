'''
If you want to prevent internal attributes from being accessed externally, you can prefix the attribute name with two underscores__.
In Python, if the instance's variable name starts with __, it become a private variable (private). Internally accessible, externally inaccessible
'''
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def print_score(self):
        print('%s: %s' %(self.__name, self.__score))
bart = Student('Nicole', 99)
bart.print_score()
'''
This ensures that external code cannot modify the internal state of the object at will, so that the code is more robust through the protection
of access restriction
But what if the external code wants to get the name and score? You can add get_name() and get_score methods to the Student class
# '''
# class Student(object):

#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
    
#     def print_score(self):
#         print('%s: %s' %(self.__name, self.__score))
    
#     def get_name(self):
#         return self.__name

#     def get_score(self):
#         return self.__score
'''
What if you want to allow exrernal code to modify the variables? You can add the set_score() method to the Student class
'''

# class Student(object):

#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
    
#     def print_score(self):
#         print('%s: %s' %(self.__name, self.__score))
    
#     def get_name(self):
#         return self.__name

#     def get_score(self):
#         return self.__score

#     def set_name(self, score):
#         self.__score = score

'''
You may ask, the orgininal one can also modify the instance's variables by directly using bart.score = 99.Why define a method?
Answer: Because in the method, you can check the parameters to avoid passing invalid parameters

def Student(object):
    ...

    def set_score(self, score):
        if isinstance(score, (int, float)) == False:
            raise TypeError('The score parameter is invalid')
        elif 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('Bad value') 
'''
'''
It should be noted that in Python, the variable names similar to '__xx__' that is start with a double underscore and end with a double underscore.
They are special variable. Special variable are directly asscessible. So you can not use names such as __name__ and __score__
Sometimes you will see instance variable names that begin with an underscore, such as _name. Such instance variable are accessible form the 
outside. However, according to the convention, when you see such a variable, it means "Although i can be accessed, please treat me as a private
variable and do not access it at will"
'''
#TASK: Please hide the gender field of the following Student object, use get_gender() and set_gender() to access and set the attribute, 
#and check the parameter validity:
# class Student(object):

#     def __init__(self, name, gender):
#         self.__name = name
#         self.__gender = gender
    
#     def get_gender(self):
#         return self.__gender
    
#     def set_gender(self, gender):
#         genderDic = {'male': 2, 'female': 1, 'other': 0}
#         if isinstance(gender, str) == False:
#             raise TypeError('Parameter is invalid!')
#         elif isinstance(genderDic[gender.lower()], int) == False:
#             raise TypeError('Parameter is invalid!')
#         else:
#             self.__gender = gender
# #TEST:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')



    
