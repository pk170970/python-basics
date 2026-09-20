import threading
import time
# without a lock

count = 0

def increment(name:str):
    global count
    for _ in range(1000):
        current_count = count
        time.sleep(0)
        count = current_count + 1
    print(f'user name is {name}')

t1 = threading.Thread(target=increment, args=('pratham',))
t2 = threading.Thread(target=increment, args=('rohan',))

t1.start()
t2.start()
t1.join()
t2.join()
print(f'Final value of counter: {count}')

# two threads shares same count but each thread has own current_count so one is overriding the other

count = 0
count_lock = threading.Lock()

def increment2(name:str):
    global count
    for _ in range(1000):
        with count_lock:
            count+=1
    print(f'user name is {name}')

t1 = threading.Thread(target=increment2, args=('pratham',))
t2 = threading.Thread(target=increment2, args=('rohan',))

t1.start()
t2.start()
t1.join()
t2.join()
print(f'Final value of counter: {count}')

# two threads shares same count but each thread has own current_count so one is overriding the other
# A lock prevents the race condition by allowing only one thread at a time to perform the complete operation:

# WIthout a lock 
# Thread 1 reads 10
# Thread 2 reads 10

# Thread 1 writes 11
# Thread 2 writes 11


#With a lock
# Thread 1 gets the lock
# Thread 1 reads 10
# Thread 1 writes 11
# Thread 1 releases the lock

# Thread 2 gets the lock
# Thread 2 reads 11
# Thread 2 writes 12
# Thread 2 releases the lock