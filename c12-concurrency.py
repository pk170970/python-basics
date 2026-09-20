# Concurrency means doing multiple tasks in overlapping time periods.

# It does not always mean they run at the exact same time.
# It is useful when tasks are waiting on something, like:
# file reading
# network requests
# database calls
# waiting for user input
# Think of it like:

# one person cooking while another is waiting for the oven
# tasks are interleaved

# 2) Parallelism
# Parallelism means running multiple tasks truly at the same time.

# This usually needs multiple CPU cores.
# It is useful for heavy computations.
# Think of it like:

# 4 workers doing 4 different jobs at the same time

import time

def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 finished")

def task2():
    print("Task 2 started")
    time.sleep(2)
    print("Task 2 finished")

# task1()
# task2()
#Above one runs one after another, in sequential way not parallel way


#Below is concurrent version

import threading

def task1():
    print('task 1 started')
    time.sleep(2)
    print('task 1 finished')

def task2():
    print('task 2 started')
    time.sleep(2)
    print('task 2 finished')

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# t1.start() #starts the thread
# t2.start()

# t1.join() # it is used to wait for a thread or process to finish before continuing the main program
# t2.join() #So if you want the main program to wait until the threads are done, you use join

# downloading files, reading from database, network request, waiting for user input 

# It creates a new thread inside the same program.
# That thread can run task1() while the main program keeps running.
# The operating system decides which thread gets CPU time.
# Threads share the same memory space.
# They do not each get their own separate Python interpreter.





#Multiprocessing or Paralleisim
# multiprocessing is used when you want to run separate tasks truly at the same time.

# Main idea
# each task gets its own process
# each process has its own memory
# each process runs in parallel on different CPU core if available
# this is good for heavy CPU work

import multiprocessing

def worker():
    print('worker process is running')

#“Only run this code in the main program, not in every child process.”
# if __name__ == '__main__':
#     p = multiprocessing.Process(target=worker)
#     p.start()
#     p.join()
#     print('main process fininshed')

# multiprocessing creates a new process
# that process re-imports your file
# without the main guard, it may recursively create more processes
# if __name__ == "__main__": prevents that




# The GIL prevents normal Python threads from doing CPU-heavy Python work truly in parallel, but it does not prevent them from overlapping while waiting.

def crunch_number():
    print(f'{threading.current_thread().name} starting counting')
    count = 0
    for _ in range(1000_00_00):
        count+=1
    print(f'{threading.current_thread().name} ended count process')

thread1 = threading.Thread(target=crunch_number, name = 'thread 1')
thread2 = threading.Thread(target=crunch_number, name = 'thread 2')

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()
end = time.time()

print(f'Total time: {end - start:.2f} sec')

# Your code demonstrates:

# How to create threads.
# How to run the same function in separate threads.
# How CPU-heavy work behaves with Python threads.
# That the GIL prevents these threads from using Python code on multiple CPU cores simultaneously.
# It does not mean that both counting loops are executing at exactly the same instant.



# let's use multiprocessing

def crunch_number2():
    print('starting counting')
    count = 0
    for _ in range(1000_00_00):
        count+=1
    print('ended count process')


if __name__ == '__main__':
    start = time.time()
    process1 = multiprocessing.Process(target=crunch_number2)
    process2 = multiprocessing.Process(target=crunch_number2)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end = time.time()

    print(f'Total time: {end - start:.2f} sec')

# Now each process has its own Python interpreter and its own GIL, so the operating system can run them on separate CPU cores.

# Small CPU task:
# threads may appear faster because they start faster

# Large CPU task:
# processes may be faster because they can use multiple CPU cores