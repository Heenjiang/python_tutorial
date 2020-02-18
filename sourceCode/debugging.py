'''
Replacing print() with logging() is the third way. Compared with assert, logging does
not throw an error, and can be output to a file
'''
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' %n)
print(10 / n)
'''
Output:
INFO:root:n = 0
Traceback (most recent call last):
  File "e:/python_tutorial/sourceCode/debugging.py", line 11, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
'''

'''
This is the advantage of logging. It allows you to specify the level of logging informaiton
There are several levels such as debug, info, warning, and error. When we specify
level=INFO, logging.debug will not work. Similarly, when level=WARNING is specified
debug and infor will not work. In this way you can safely output information at 
different levels  without  deleting
Another advantage of logging is that through a simple configuration, a statement 
can be output to different places at the same time, such as console and files
'''