'''
What if you want to manipulate these direcories and files in a Python program? 
In fact, the commands provided by the operating system just simply call the interface functions 
provided OS, and also Python has some built-in modules can directly call those interface funcions
provided by operating system
Like os，os.path, shutil module
'''
#os module
import os

# print(os.name)#posix: Linux, Unix or Mac os x, nt: Windows
# print(os.uname())#Windows does not have this interface function

#os.environ
# print(os.environ)
# print(os.environ.get('PATH'))

#os.path
# print(os.path.abspath("."))
#os.path.join()
# print(os.path.join(os.path.abspath("."), 'testdir'))
#Different operating systems will show different
#outputs, cause the delimiter in Linux is '/', in Windows is '\'

#create a directory
# os.mkdir(os.path.join(os.path.abspath("."), 'testdir'))

#remove a directory
# os.rmdir(os.path.join(os.path.abspath("."), 'testdir'))

#os.path.split()
# print(os.path.split(os.path.join(os.path.abspath("."), 'testdir.txt')))
#!!!!These functions for merging and spliting paths do not require directories and files to exist,
#they only operate on strings!!!   
 
#Finally, look at how to use Python's features to filter files or directories

#List all directories under current directory
# print([x for x in os.listdir('.') if os.path.isdir(x)])

#List all .py files
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.split(x)[1] == '.py'])