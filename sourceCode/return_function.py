#In addition to accepting functions as parameters, higher-order functions cans also return functiona as result values
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum
#When we call lazy_sum(), what is returned is not the result of the sum, but the sum function
f = lazy_sum(1, 3, 5, 7)
print(f)#<function lazy_sum.<locals>.sum at 0x00AF0268>
#When the function f is called, the result of the sum is actually calculated
print(f())#16
#In this example, we define the function sum in the function lazy_sum, and the internal function sum can refer to the parameters and local variables
#of the external function lazy_sum. When lazy_sum returns the function sum, the relevant parameters and variables are stored in the returned
#function. This kind of program structure called "Closure", and it has great power

#Please note that when we call lazy_sum(), each call will return a new function, even if the same parameters are passed in
f1 = lazy_sum(1, 2, 3, 4, 5)
f2 = lazy_sum(1, 2, 3, 4, 5)
print(f1 == f2)#false

#One thing to keep in mind when returning closures: Do not reference any loop variable in the return functin, or variable that will change later
#What if you must reference a loop variable? 
#The method is to create another function, and bind the current value of the loop variable with the parameters of the function. Regardless of
#how the loop variable is subsequently changed, the value bound to the function parameter remain unchanged.
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f(i):
#              return i*i
#         fs.append(f(i))
#     return fs
# print(count())

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
# f1, f2, f3 = count()
# print(count())#[<function count.<locals>.f.<locals>.g at 0x00AD03D0>, 
#<function count.<locals>.f.<locals>.g at 0x00AD0418>, <function count.<locals>.f.<locals>.g at 0x00AD0460>]s
# print(f1(), f2(), f3())

#Using a closure to return a counter function, each time it is called it returns and incremented integer
# def createCounter():
#     n = 0
#     def counter():
#         nonlocal n
#         n += 1
#         return n
#     return counter
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

#A function can return a calculation result or a function. When returning a function, keep in mind that the function is not executed immediately
#do not refrence any variable that may change in the return function


