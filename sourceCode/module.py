'''
Python itself has a lot of very useful built-in modules. Once installed, these modules can be used immediately.
Let's take the built-in sys module as an example and write a hello module
'''
#!/usr/bin/env python3
# -*- coding: tuf-8 -*-

'a test module'

__author__ = 'Hoen'

import sys#Import the module

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s' %args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()

'''
Lines 1 and 2 are standard comments. The line 1 comment allows this hello.py file to run directly on Unix/Linux/Mac. 
The line 2 comment indicates that the hello.py file itself uses standard UTF-8 econding;
The fourth line is a string indicating the documentation comment of the module. The first string og any module is considered as the documentation comment of the module;
The sixth line is the __author__ variable to write the author in, so that others can admire you name when you open the source code;
The above is the standard file template of the Python module. Of course, youcan delete all of them without writing, but it is certainly correct to do things according to the standard
'''

'''
When we run the hello module dile on the command line, the Python interpreter sets a special variable __name__ to __main__, and if the 'hello' module is imported elsewhere, the if judgment 
will fail. Therefore, this kind of "if test" can let a module executes some additional code when run from the command line, the most common usage which is to run tests
'''