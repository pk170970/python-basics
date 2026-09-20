from threading import Lock, Thread

class StudyTask:
    def __init__(self, topic, status, hours):
        self.topic = topic
        self.status = status
        self.hours = hours


tasks1 = [
    StudyTask("Python", "done", 2),
    StudyTask("Functions", "active", 3),
    StudyTask("OOP", "planned", 4),
    StudyTask("AI", "planned", 4),
]

tasks2 = [
    StudyTask("Javascript", "done", 2),
    StudyTask("typescript", "active", 2),
    StudyTask("Angular", "planned", 4),
]

counts = {'planned': 0, 'active': 0, 'done': 0}
lock = Lock()

def threaded_status_counts(tasks):
    with lock:
        for task in tasks:
            if task.status == 'planned':
                counts['planned'] += 1
            elif task.status == 'active':
                counts['active'] += 1
            elif task.status == 'done':
                counts['done'] += 1
    return counts

# t1 = Thread(target=threaded_status_counts, args=(tasks1,))
# t2 = Thread(target=threaded_status_counts, args=(tasks2,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# print(counts)

#Above version is good but it blocks the whole update block, one threads waits
# while other is working. 
# Let's make a common pattern where each thread have it's own count and then it locks once and merge into dic 

# What is missing in your version
# 1) Less real parallelism
# Your code does this:
# with lock:
#     for task in tasks:
#         ...
# So one thread holds the lock while it processes its entire list.

# That means the second thread waits a lot, which reduces concurrency.
# local_counts = ...
# with lock:
#     shared_counts[key] += local_counts[key]

# This keeps the lock held only for the final merge, not for the whole task loop.

def count_local(tasks):
    local_counts = {'planned': 0, 'active': 0, 'done': 0}
    for task in tasks:
        if task.status == 'planned':
            local_counts['planned'] += 1
        elif task.status == 'active':
            local_counts['active'] += 1
        elif task.status == 'done':
            local_counts['done'] += 1
    return local_counts

def threaded_status_safe_count(tasks):
    local = count_local(tasks)
    with lock:
        for key in counts:
            counts[key] += local[key]
    return counts

# t1 = Thread(target=threaded_status_safe_count, args=(tasks1,))
# t2 = Thread(target=threaded_status_safe_count, args=(tasks2,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# print(counts)



# ----------------------------- Process based hours total --------------------
from multiprocessing import Process, Queue, Value


def worker(tasks, queue:Queue):
    total_hours = 0
    for task in tasks:
        total_hours += task.hours
    queue.put(total_hours)

def process_hour_totals(tasks):
    queue = Queue()
    process = Process(target=worker, args=(tasks, queue))
    process.start()
    process.join()
    return queue.get()

def count_worker(counter):
    for _ in range(5):
        with counter.get_lock():
            counter.value +=1



# if __name__ == "__main__":
#     print(process_hour_totals(tasks1))
#     counter = Value('i', 0)
#     p1 = Process(target=count_worker, args=(counter,))
#     p2 = Process(target=count_worker, args=(counter,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print(counter.value)



# When we want to send multiple values or result as messages then Queue is better
# When we want one shared number or flag or object in multiprocessing, then we use Value 



# ---------------------------Async report -----------------------
import asyncio

async def async_report():
    async def job(name, delay, fail = False):
        await asyncio.sleep(delay) #it simulates watiing like network call
        if fail:
            raise ValueError(f'{name} fails')
        return f'{name} ok'

    tasks = [
        asyncio.create_task(job('task1', 0.2)), # this starts background async task
        asyncio.create_task(job('task2', 0.3)),
        asyncio.create_task(job('task3', 5, True)),
    ]

    results = await asyncio.gather(*tasks, return_exceptions= True) #waits for all task to finish
    return results

# print(asyncio.run(async_report()))



async def cancel_preview():
    task = asyncio.create_task(asyncio.sleep(10))
    try:
        await asyncio.sleep(0.1)
        task.cancel()
        await task
    except asyncio.CancelledError:
        print('Cleanup: task is cancelled')



# Process Pool Executor

# This is good when you have:

# many independent tasks
# same function applied to many inputs
# automatic load distribution
# The pool takes care of worker management for you.

# Create a function named tokenize_in_process(text_chunks).

# Requirements:

# use ProcessPoolExecutor
# each process counts tokens for a chunk of text
# combine the results in the parent process

from concurrent.futures import ProcessPoolExecutor

def count_chunks(text_input):
    return len(text_input.split(','))

def tokenize():
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(count_chunks, ['hello, ram i amd, goood', 'ram , rama, ratte ratte nikli re umariya']))
        return results

if __name__ == "__main__":
    print(tokenize())