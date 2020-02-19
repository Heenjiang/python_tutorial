'''
Reading and writing files is the most common IO operation. Python has built-in functions for reading
and writing files, and its usage is compatible with C.
Before reading and writing files, we must first understand that the functions of reading and writing 
files on disk are provided by the operating system. Modern operating systems do not allow ordinary 
programs to directly operate the disk. Therefore, reading and writing files is to request operating
system to open a file object(usually called a file descriptor), and then read data from this file
object(read files) or write files to this file object(write files) through the interface provided by 
the operating system
'''

#read files; Identifier 'r' means read
# f = open('E:\python_tutorial\sourceCode\iofiletest.txt', 'r')
#If the file is successfully opened, then call the 'read()' method could get the entire contents of 
#the file at once
# print(f.read())
'''
output:
hello, this is Nicole!!
hello, here is lucas!!
hello, here is zoey from German!!
'''
#The final step is to call the 'close()' method to close the file. The file must be closed after use,
#because the file object will occupy the operating system resources, and the number of files that the
#operating system can open at the same time is also limited
# f.close()

#Because file reading and writing may generate IOError, 'f.close()' will not be called after an error
#occurs. So, in order to ensure that the file can be closed properly regardless of whether there is 
#an error, we can use 'try...finally' block statement to achieve
# try: 
#     f = open('E:\python_tutorial\sourceCode\iofiletest.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
#But it's too cumbersome to be so every time, so Pyhton introduce the with statement to automatically
#call the 'close()' method
# with open('E:\python_tutorial\sourceCode\iofiletest.txt', 'r') as f:
#     print(f.read())

#If the file is small, 'read()' is the most convenient way to read it at once; if the file size is unknown
#it is better to call 'read(size)' repeatedly; if it is a configuration file, 'readlines()' is the most
#convenient way to read all configurations at once and it will return a list.
# with open('E:\python_tutorial\sourceCode\iofiletest.txt', 'r') as f:
#     print(f.readline())#hello, this is Nicole!!

# with open('E:\python_tutorial\sourceCode\iofiletest.txt', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())#strip() remove '\n' at the end
'''
output:
hello, this is Nicole!!
hello, here is lucas!!
hello, here is zoey from German!!
'''

#Read binary file
# with open('E:\python_tutorial\sourceCode\image.jpg', 'rb') as f:
#     print(f.read())#b'\\xff\\xd8\\xff\\xe1\\x00\\x18Exif\\x00\\x00...'

#Read non-UTF-8 encoded text file
# with open('E:\python_tutorial\sourceCode\\non-UTF-8_encoded_file.txt', 'r', encoding='gbk') as f:
#     print(f.read())

#When encountering some files with irregular encoding, you may encounter UnicodeDecodeError, because
#some illegally encoded characters may be mixed in the text file. In this case, the open() function 
#also receives an errors parameter, which indicates what to do if an encoding error is encountered.
#The easiest way is simply ignore
with open('E:\python_tutorial\sourceCode\\non-UTF-8_encoded_file.txt', 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())

#Writing a file is the same as reading a file. The only difference is that when calling the open() 
#function, passing in the identifier 'w' or 'wb' means writing a text file or a binary file
# with open('E:\python_tutorial\sourceCode\\non-UTF-8_encoded_file.txt', 'w', encoding='gbk') as f:
#     f.write('你好，我是nicoele')

'''
When we write files, the operating system often does not write the data to disk immediately, but puts it
in the memory cache, and then writes slowly when it is free. Only when the close() method is called, the
operating system guarantees that all unwritten data is written to disk
'''
#What if we want to append to the end of the file? we can pass the 'a' parameter instead of 'w' means
#append to the end of the file
# with open('E:\python_tutorial\sourceCode\\non-UTF-8_encoded_file.txt', 'a', encoding='gbk') as f:
#     f.write('你好，我是Nicole\n')
# with open('E:\python_tutorial\sourceCode\\non-UTF-8_encoded_file.txt', 'r', encoding='gbk', errors='ignore') as f:
#     print(f.read())


# 文件路径不能用反斜杠‘\’。举个例子，如果我传入的文件路径是这样的：
# sys.path.append('c:\Users\mshacxiang\VScode_project\web_ddt')

# 则会报错SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: tr

# 原因分析：在windows系统当中读取文件路径可以使用\,但是在python字符串中\有转义的含义，如\t可代表TAB，\n代表换行，所以我们需要采取一些方式使得\不被解读为转义字符。目前有3个解决方案

# 1、在路径前面加r，即保持字符原始值的意思。

# sys.path.append(r'c:\Users\mshacxiang\VScode_project\web_ddt')

# 2、替换为双反斜杠

# sys.path.append('c:\\Users\\mshacxiang\\VScode_project\\web_ddt')

# 3、替换为正斜杠

# sys.path.append('c:/Users/mshacxiang/VScode_project/web_ddt')
# 
