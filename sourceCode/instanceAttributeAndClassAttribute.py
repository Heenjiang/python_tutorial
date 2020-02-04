#TASK: In order to count the number of students, you can add a class attribute to the students class, which is automatically added every time 
#when an attribute is created

class Student(object):
    count = 0

    def __init__(self, name):
        self.__name = name
        Student.count += 1
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
