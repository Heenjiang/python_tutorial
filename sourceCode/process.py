from multiprocessing import Process
import os

#The multiprocessing module provides a Process class to represent a process object.
#The following example demonstrates starting a child process and waiting for it to end:

#The code to be executed by the child process
# def run_proc(name):
#     print('Run child process %s (%s)' %(name, os.getpid()))

# if __name__ == '__main__':
#     print('Parent process %s' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start...')
#     p.start()
#     p.join()
#     print('Child process end.')

#If you want to start a large number of child processes, you can use proccess pool to creat child 
#process in batches:
# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' %(name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3) 
#     end = time.time()
#     print('Task %s runs %0.2f seconds' %(name, end - start))

# if __name__ == '__main__':
#     print('Parent process %s' %os.getpid)
#     p = Pool()
#     for i in range(10):
#         #Create child proccesses asynchronously
#         p.apply_async(long_time_task, args=(i, ))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done...')

#Many times, the child process is not itself, but an external process. After we create the child
#process, we need to control the input and output of the child process.
#The 'subprocess' module allows us to easily start a subprocess and then contol its inputs and outputs
#The following example shows how to run the command 'nslookup www.python.org' in Python code, which
#has the same effect as running directly from the command line
# import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

#If the child process still needs inputs, you can enter it through the communicate() method:
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, 
stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

#There must be communication between processes, and the operating system provides many mechanisms to
#implement inter-process communication. Python's multiprocessing module wraps the underlyinng mechanism
#and provides multiple ways to exchange data, such as Queue, Pipes
#Let's take Queue as an example, create two child process in the parent process, one writes data 
#to the Queue an another one reads data from the Queue
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('Process to write %s' % os.getpid())
    for value in ['A', 'B', 'C', 'D']:
        print('Put %s to queue' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    q = Queue()
    pr = Process(target=read, args=(q,))
    pw = Process(target=write, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    #The 'pr' process is an endless loop. You cannot wait for it to end. You can only forcefullly
    #terminate it
    pr.terminate()