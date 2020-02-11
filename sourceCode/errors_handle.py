'''
In the process of running a program, you can agree to return an error code in advance, so that
you can know wheather there is an error and the reason for the error. It is very common to return
an error code in calls provided by operating system. For example, the function open() that opens
a file and returns a file descriptor(that is, an integer) on success, and returns -1 on error
It is very inconvenient to use an error code to indicate wheather an error occurred, beacuse the
normal result that the functin itself should return is mixed with the error code, causing the
caller to use a lot of code to determine wheather an error has occurred  
'''
#High-level language usually have a set of try...except..finally... error handling mechanisms
#built-in, and Python is no exception
# try:
#     print('try...')
#     r = 10 / 0
#     print('result is:', r)
# except ZeroDivisionError as e:
#     print('expect: ',e)
# finally:
#     print('here is final statements!')
# print('This is end!')
'''
output:
try...
expect:  division by zero
here is final statements!
This is end!
'''

'''
When we think that some code block maybe will throw any execption, we can use 'try' to run this 
block of code. If the execution is something wrong, the subsequent code will not contiune to 
execute, but directly jump to the error handling code, that is the 'expect' statement block.
After 'except', if there is a 'finally' statement block, the 'finally' statement will be executed
and then the whole execution is completed
'''

'''
There should be many types of errors. If different types of errors occur, they should be handled
by different except blocks. Yes, there can be multiple except to catch different types of errors
'''
# try:
#     print('try..')
#     r = 10 / int('a')
#     print('result is:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZreoDivisionError:', e)
# finally:
#     print('Here is the final statement block!')
# print('End')
'''
output:
try..
ValueError: invalid literal for int() with base 10: 'a'
Here is the final statement block!
End
'''
#In addition, if no occurs, you can add an 'else' block after the except statement block
#When no error occurs, the 'else' statement is automatically executed.
# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result is: ', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('zeroDivisionError: ', e)
# else:
#     print('No error')
# finally:
#     print('Here is the \'finally\' statement')
# print('End')
'''
output:
try...
result is:  5.0
No error
Here is the 'finally' statement
End
'''

'''
Python errors are actually classes. And all error types are inherited from BaseException, so 
when using except, it is important to note that it not only catches errors of its type, but also
its subclass.
'''


# try:
#     foo()
# except ValueError as e:
#     print('ValueError:',e)
# except UnicodeError as e:
#     print('UnicodeError:',e)
'''
The second except will never catch UnicodeError, because UnicodeError is a subclass of 
ValueError. So if there is UnicodeError that is also caught by the first except
'''

'''
Another great benefit of using 'try...except...finally...' to catch errors is that it can e called
across nultiple layers, for example:
'''
# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error:', e)
#     finally:
#         print('finally...')
# main()
'''
Error: division by zero
finally...
'''

'''
If you don't catch the error, you natually ask the Python interpreter to print out the error stack, but
the program is also ended. Now that we can catch the error, we can print out the error stack, analyze the
cause of the error, and let the program contiune executing
Python's built-in logging module makes it easy to log error messages
'''
# import logging

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('s')
#     except Exception as e:
#         logging.exception(e)

# main()
# print('End')
'''
output:
ERROR:root:invalid literal for int() with base 10: 's'
Traceback (most recent call last):
  File "e:/python_tutorial/sourceCode/errors_handle.py", line 140, in main
    bar('s')
  File "e:/python_tutorial/sourceCode/errors_handle.py", line 136, in bar
    return foo(s) * 2
  File "e:/python_tutorial/sourceCode/errors_handle.py", line 133, in foo
    return 10 / int(s)
ValueError: invalid literal for int() with base 10: 's'
End
'''
#Through configuration, logging can also log errors to log files for troubleshooting afterwards

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n

# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise

# bar()
'''
In the bar() function, we have clearly caught the error, but after printing a ValueError.   
We throw the error through the raise statement. Isn't stupid?
In fact, this error handling is not stupid at all, but quite common.The purpose of catching error
is to record them for future tracking. And maybe the current caller does not know what to do with the
error, the most appropriate way is to continue to throw it up and let the top caller handle it 
'''
#If the raise statement takes no agruments, the current error will be thrown as it is.
#In addition, raise an Error in expect can also convert on type of error into another type

# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error!!')
'''
output:
Traceback (most recent call last):
  File "e:/python_tutorial/sourceCode/errors_handle.py", line 186, in <module>
    10 / 0
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "e:/python_tutorial/sourceCode/errors_handle.py", line 188, in <module>
    raise ValueError('input error!!')
ValueError: input error!!
'''

from functools import reduce

def str2num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

