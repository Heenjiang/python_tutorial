'''
Is it possiable to both check parameters and access class variable in a simple way like Clas.Attribute?
Rememebr that decorators can dynamically add functionality to functions? For class methods, decorators also work. Python's built-in @property
decorator is responsible for turning a method into a property call
'''

# class Student(object):

#     @property
#     def score(self):
#         return self._score
    
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0~100')
#         self._score = value

# s = Student()
# s.score = 60
# print(s.score)
# s.score = 800#    raise ValueError('score must between 0~100') :ValueError: score must between 0~100

'''
Summary: @property is widely used in class definitions. allowing caller to write short code, and at the same time ensure that necessary 
parameters are checked. In this way, the possibility of errors is reduced when the program is running
'''

#TASK:Please use the @property to add 'width' and 'height' attributes to a 'Screen' Class and a read-only attribute 'resolution'
class Screen(object):

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def resolution(self):
        return self._height * self._width


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')