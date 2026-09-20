# asyncio lets python handle many waiting task efficiently usually under one thread. For example network request, reading files, database queries, timers, user input. While one task is waiting, another task can run, this we called as concurrency.

# Normal synchronous code
import time

# def task(name):
#     print(f'{name} started')
#     time.sleep(2)
#     print(f'{name} ended')

# task('A')
# task('B')
# A starts , A ends then B starts and B ends. total time: 4s as it runs line by line

import asyncio

# Async fxn
async def task(name):
    print(f'{name} started')
    await asyncio.sleep(2)
    print(f'{name} ended')

# result = task('A') # this return a coroutine object, calling it doesn't execute immediately
# print(result)

# async def main():
#     await task('a')
#     await task('b')

# asyncio.run(main()) # to start the program

# Above program still takes 4s because we wait for A completly before starting B. await pauses the current async function, but above there is no other task to run


async def main():
    task_a = asyncio.create_task(task("A"))
    task_b = asyncio.create_task(task("B"))
    await task_a
    await task_b

# How execution happens:
# 1. task('A') runs and returns a coroutine.
# 2. asynio.create_task put this coroutine into a event loop which schedule this task to be run later.
# 3. same for b, first and second step happens
# 4. Now, as task_a is await, event loop gets the time to run first coroutine
# 5. it prints started A, then it sees asyncio.sleep(2) so this pause the task for 2s and event loop starts the another task('B') coroutine object and do the same, pause this also for 2s
# 6. After 2s passed, both function prints ended A and ended B, like this in 2s both the function is run

# we can schedule the coroutine and put in event loop so we can wait for all of them to finish using gather

# async def main():
#     await asyncio.gather(
#         task('A'),
#         task('B')
#     )
    #gather waits for all the task concurrently, not one after another

# async def fetch_data(name, seconds):
#     print(f"{name} started")
#     await asyncio.sleep(seconds)
#     print(f"{name} finished")
#     return f"{name} data"

# async def main():
#     results = await asyncio.gather(
#         fetch_data('A', 2),
#         fetch_data('B', 1),
#         fetch_data('C', 3)
#     )
#     print(results)

# asyncio.run(main())

# We can see in output that B finished first, then A and thhen C but gather preserve the order so we get A,B,C 

# async def processing(item,delay):
#     print(f'processing {item}')
#     await asyncio.sleep(delay)

#     if item == 'banana':
#         raise ValueError('Banana failed')
#     print(f'processed {item}')
#     return item

# async def main():
#     results = await asyncio.gather(
#         processing('milk', 2),
#         processing('tea', 3),
#         processing('banana', 1),
#         return_exceptions=True
#     )
#     print(results)

# asyncio.run(main())

# gather() does not stop when one task fails. It returns the exception as one result, while the other tasks continue. can also write inside try except
# async def main():
#     try:
#         results = await asyncio.gather(
#             process_item("apple", 2),
#             process_item("banana", 1),
#             process_item("orange", 3),
#         )
#         print(results)
#     except ValueError as error:
#         print(f"Error: {error}")


# Create a task named timer that:

# Prints "Timer started".
# Waits for 5 seconds.
# Prints "Timer finished".
# In main():

# Start the task with asyncio.create_task().
# Wait for 2 seconds.
# Cancel the task.
# Catch asyncio.CancelledError inside the timer.
# Print "Timer cleanup complete" when cancelled.
# Predict the output before running it.

# async def timer():
#     try:
#         print('Timer started')
#         await asyncio.sleep(5)
#         print('Timer finished')
#     except asyncio.CancelledError:
#         print('Timer cleanup completed')

# async def main():
#     if __name__ == '__main__':
#         task1 = asyncio.create_task(timer())
#         await asyncio.sleep(2)
#         task1.cancel()
#         await task1

# asyncio.run(main())


# ------------------Async io with Threads ----------------------------------

def read_file(name, seconds):
    print(f"{name} started")
    time.sleep(seconds)
    print(f"{name} finished")
    return f"{name} loaded"

async def main():
    result = await asyncio.gather(
        asyncio.to_thread(read_file, 'A', 2),
        asyncio.to_thread(read_file, 'B', 1),
        asyncio.to_thread(read_file, 'C', 3),
    )
    print(result)

asyncio.run(main())

# asyncio.to_thread() runs each blocking read_file() call in a worker thread, so time.sleep() does not block the event loop.
# One precise wording detail: time.sleep() still blocks each worker thread, but it does not block the asyncio event loop or the main async task.