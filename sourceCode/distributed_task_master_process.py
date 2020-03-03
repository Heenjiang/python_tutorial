#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #Among Thread and Process, Process should be preferred because Process is more stable, and process
#can be distributed to multiple machines, and thread can only be ditributed to multiple CPUs on the
#same machine.

#A master process can act as a sheduler. Rely on network communication to distribute tasks among 
#multiple other processes on different servers.

#For example, if we already have a multi-process program for communication through Queue running on 
#the same machine, now because the multiple-processing task is heavy, we want to distribute process
#of the task and the process of processing the task to two machines. How to use implement that?

import time, random, queue
from multiprocessing.managers import BaseManager

#For sending tasks
task_queue = queue.Queue()
#For reciving results
result_queue = queue.Queue()

#Inherited from BaseManager
class QueueManager(BaseManager):
    pass

def gettask():
    return task_queue

def getresult():
    return result_queue
    
def master_process():
    #Register both queues to the network, the callable parameter is associated with the Queue object
    QueueManager.register('get_task_queue', callable=gettask)
    QueueManager.register('get_result_queue', callable=getresult)
    #Bind to port 5000 and set the vertification code 'abc'
    manager = QueueManager(address=('127.0.0.1',5000), authkey=b'abc')
    #Start the Queue
    manager.start()
    #Get access to the Queue object over the network
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    #Put a few tasks in
    for i in range(10):
        n = random.randint(0,100000)
        print('Put task %d...' % n)
        task.put(n)
    #Read results from the result_queue
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
    #shut down the manager
    print('master exit...')

#Please note that when we write multi-process programs on one machine, the created Queue can be used
#direcctly, but in a distributed multi-process environment, adding tasks to the Queue cannot directly
#operate on the original task_queue, because that bypasses the encapsulation of the QueueManager, it
#must be added through the Queue interface obtained by manager.get_task_queue()
if __name__ == '__main__':
    master_process()

# #!/usr/bin/env python3
# # -*- coding:utf-8 -*-
# import random, time, queue
# from multiprocessing.managers import BaseManager

# # Queue for send tasks
# task_queue = queue.Queue()
# # Queue for accept results
# result_queue = queue.Queue()

# # Create a QueueManager herited from BaseManager
# class QueueManager(BaseManager):
#     pass

# def gettask():
#     return task_queue

# def getresult():
#     return result_queue

# def do_task_master():
#     # Register the two queues to network, argument callable references to Queue object
#     # QueueManager.register('get_task_queue', callable=lambda: task_queue)
#     # QueueManager.register('get_result_queue', callable=lambda: result_queue)

#     # When run under windows, it not support bind through lambda
#     QueueManager.register('get_task_queue', callable=gettask)
#     QueueManager.register('get_result_queue', callable=getresult)

#     # Bind port to 5000, set authentication code as 'abc'
#     manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

#     # Start queue
#     manager.start()

#     # Acquire Queue that used to access through network
#     task = manager.get_task_queue()
#     result = manager.get_result_queue()

#     # Put some tasks into task Queue
#     for i in range(10):
#         n = random.randint(0, 10000)
#         print('Put task %d...' % n)
#         task.put(n)

#     # Read result from result queue
#     print('Try get results...')
#     for i in range(10):
#         try:
#             r = result.get(timeout=10)
#             print('Result: %s' % r)
#         except queue.Empty:
#             print('Result Queue is empty')

#     # Close
#     manager.shutdown()
#     print('Master exit')

# if __name__ == '__main__':
#     do_task_master()