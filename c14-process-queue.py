import threading
from multiprocessing import Process, Queue, Value
import time
import os

# Each process has separate memory:
# Process 1:
#     result = 10

# Process 2:
#     result = 20

# Even if both variables have the same name, they are different copies. Changing result in Process 1 does not change it in Process 2.

# multiprocessing.Queue and multiprocessing.Value provide controlled ways to communicate.

# count = 0
# def cpu_heavy():
#     global count
#     print('Starting heavy task')
#     for _ in range(10**7):
#         count+=1
#     print('heavy task done')

# start = time.time()
# threads =  [threading.Thread(target=cpu_heavy) for i in range(2)]
# [t.start() for t in threads]
# [t.join() for t in threads]

# print(f'Total time: {time.time() - start:.2f} sec')

#Above same task if done using process

# if __name__ == '__main__':
#     start = time.time()
#     processes =  [Process(target=cpu_heavy) for i in range(2)]
#     [t.start() for t in processes]
#     [t.join() for t in processes]

#     print(f'Total time: {time.time() - start:.2f} sec')


#Now let's do it using queue
def worker(result_queue):
    result = 20 + 20
    print(f'worker process {os.getpid()} produced: {result}')
    result_queue.put(result)

if __name__ == "__main__":
    result_queue = Queue()
    process = Process(target=worker, args=(result_queue,))
    process.start()

    result = result_queue.get()
    print(f'main process recieved: {result}')
    process.join()


# Child process:
#     result = 40
#     queue.put(result)

# Queue:
#     transfers 40

# Main process:
#     queue.get()
#     receives 40


# multiprocessing.Value is useful when two or more processes need to access the same simple value, such as a number or Boolean.
counter = Value('i', 0)
# "i" means integer
# 0 is the starting value
# counter.value is the actual shared number

