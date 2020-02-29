#Multitasking can be performed by multiple processes or by multiple threads within a process.
#We mentioned earlier that a process is composed of serveral threads, and a process has at least one
#thread.
#Because threads are execution units directly supported by operating system, high-level languages
#usually have built-in multithreading support, and Python is no exception. Python threads are real
#Posix threads, not simulated threads

#To start a thread is to pass in a function and create a thread instance, then call start() to execute
import time, threading

#Code executed by the new thread
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s is running... %d' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.currentThread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.currentThread().name)