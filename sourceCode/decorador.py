'''
Now, suppose we want to enhance the functionality of the new() function, for example, print a log before and after a function call, but do not
modify the definition of the now() function. This way of dynamically adding functionality during code execution is called "Decorator"
In essence, a decorator is a higher-order function that returns a function. Therefore, we need to define a decorator that can print logs.
Which can be defined as follows:
'''
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s()' %func.__name__)
#         return func(*args, **kw)
#     return wrapper

# @log
# def now():
#     print('2015-3-25')

# print(now())
'''
Because log() is a decorator that returns a function, the original now() function still exists, but now the 'now' variable of the same name points
to the new function, so calling now() will execute the new function, that is the on which returned by the log() functiuon: wrapper()
The wrapper() function's parameter definition is (*args, **kw), so the wrapper() function can accept calls with any parameters.
Inside the wrapper() function, first print the log and then immediately call the original function
'''

#If the decorator itself needs to pass in parameters, it is necessary to write a higher-order function that returns a decorator
#which will be more complicated to write
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s' %(text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# @log('executes')
# def now():
#     print('2015-3-25')

# now()#executes now \n 2015-3-25

'''
There is no problem with the definition of the above two decorators, but one final step is needed. Because we said that functions are also 
objects, it has attributes such as __name__, but when you go to see the functions after decorator decoration, thier __name__ has changed from 
the original "now" to "wrapper"
'''
'''
Because the name "wrapper" is from the function "wrapper" which returned by the decorator, and you need to copy the original function's __name__
and other attributes into the wrapper() function, otherwise, some code that depends on the function signature will execute incorrectly
And there is a built-in functions in Python moudle called functools.wraps does the copy things, so complete decorator is writted as follows 
'''
import functools
import time

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s()' %func.__name__)
#         return func(*args, **kw)
#     return wrapper

# def log_with_parameters(ms):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s()' %(ms, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#TASK 1：Please design a decorator that can act on any function and print the execution time of the function
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         start_time = time.time()
#         result = fn(*args, **kw)
#         end_time = time.time()
#         print('The execution time of the function %s is %f ms' %(fn.__name__, end_time - start_time))
#         return result
#     return wrapper
# #Test
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')

def log(text_or_fn):
    if isinstance(text_or_fn, str):
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                print('%s , call %s()' %(text_or_fn, fn.__name__))
                return fn(*args, **kw)
            return wrapper
        return decorator
    else:
        fn = text_or_fn
        print(fn)#test_log_without_parameters
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            print('call %s()' %fn.__name__)
            return fn(*args, **kw)
        return wrapper

@log('Function is execting!')
def test_log_with_parameters():
    # print(time.time())
    pass

@log
def test_log_without_parameters():
    # print(time.time())
    pass





