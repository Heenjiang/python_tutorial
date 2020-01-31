#name = input("Please input a person's name:")
#print("I really miss you", name)
#print("1024 * 768 =", 1024 * 768)
#print("I'm ok")
#print('I\'m ok')
#print('I\'m learning\nPython')
#print('\\\n\\')
#print('\\\t\\')
#print(r'\\\\\t\\\\')
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,Lisa!'''
print(n, f, s1, s2, s3, s4)
print('%2d-%02d' %(3,1))
print('%.2f' %3.1415926)
# s1 = 72 
# s2 = 85
# r  = (s2 - s1)/72 * 100
# print('小明的成绩提升的百分点是：%.2f%%' % r)
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]

# print(L[0][0],L[1][1],L[2][2])
# height = 1.68
# weight = 70
# bmi = weight / (height * height)

# if bmi < 18.5:
#     print('体重过轻')
# elif bmi < 25:
#     print('体重正常')
# elif bmi < 28:
#     print('体重过重')
# elif bmi < 32:
#     print('肥胖')
# else:
#     print('严重肥胖') 
# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)

# sum = 0
# for x in range(101):
#     sum += x # sum = sum + x
# print("sum from 0 to 100:", sum)

#用while 循环计算< 100 的奇数之和 Use "while" loop calculate the sum of odd numbers less than 100
# sum = 0
# n = 1
# while n < 100:
#     sum += n
#     n = n + 2
# print('The sum of odd numbers less than 100 is: %d' %sum )

#Use a loop to print Hello, xxx! For each name in the list in turn
# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print('Hello, %s!' %name)

#Use a loop and a break statement to print number 1 to 10 
# n = 0
# while n < 100:
#     if n > 10:
#         break
#     print(n)
#     n += 1
# print('End')
#use a loop and continue statement to print all odd numbers less than 100
# for n in range(1,101):
#     if n % 2 == 0:
#         continue
#     print(n)
# print('End')

#Practice the dictionary data structure in python
# d = {'Michael' : 95, 'Bob' : 75, 'Tracy' : 85}
# print(d['Michael'])
# #Check if key is in dictionary
# if not('Jack' in d):#if d.get('Jack', -1) != -1: or d.get('Jack')     ps:Through the get() method provided by dictionary data structure, if the key doesn't exist return None, or the value specified by yourself
#     d['Jack'] = 100
#     print(d['Jack'])
