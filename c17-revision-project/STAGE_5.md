# Stage 5: Concurrency

Stage 5 focuses on threads, processes, locks, queues, asyncio, cancellation, and process pools.

Create a new file named `stage5.py`. Do not change earlier stage files for this stage.

## 1. Threaded status counts

Create a function named `threaded_status_counts(tasks)`.

Requirements:

- use at least two threads
- each thread reads independent work
- combine results safely using a `Lock`
- return a dictionary of counts by status

Example idea:

```python
from threading import Thread, Lock


def threaded_status_counts(tasks):
    counts = {"planned": 0, "active": 0, "done": 0}
    lock = Lock()
    # split work between threads and update the shared counts safely
    return counts
```

Important idea:

- threads share memory
- if two threads update the same dictionary at the same time, data can be lost or mixed
- a lock prevents that race condition

Test with a small list of task-like objects or dictionaries.

## 2. Process-based hour totals

Create a function named `process_hour_totals(tasks)`.

Requirements:

- use a `multiprocessing.Process`
- use a `multiprocessing.Queue`
- the worker process calculates total hours
- the parent process receives the result through the queue

Example idea:

```python
from multiprocessing import Process, Queue


def process_hour_totals(tasks):
    queue = Queue()
    process = Process(target=worker, args=(tasks, queue))
    process.start()
    process.join()
    return queue.get()
```

The important part is that process memory is separate from the parent process, so you must send the result back explicitly.

## 3. Async report

Create a function named `async_report()`.

Requirements:

- use `asyncio.create_task()` or `asyncio.gather()`
- run at least three simulated I/O tasks
- combine or print their results
- catch one task failure using `return_exceptions=True`

Example idea:

```python
import asyncio


async def async_report():
    async def job(name, delay, fail=False):
        await asyncio.sleep(delay)
        if fail:
            raise ValueError(f"{name} failed")
        return f"{name} ok"

    tasks = [
        asyncio.create_task(job("task1", 0.2)),
        asyncio.create_task(job("task2", 0.1)),
        asyncio.create_task(job("task3", 0.3, fail=True)),
    ]

    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results
```

Key concept:

- async tasks work cooperatively
- one task can fail without crashing the whole event loop if you handle exceptions deliberately

## 4. Cancel a task

Create a function named `cancel_preview()`.

Requirements:

- create a task that waits using `asyncio.sleep()` or a timer pattern
- cancel it
- catch `asyncio.CancelledError`
- print cleanup output after cancellation

Example structure:

```python
import asyncio


async def cancel_preview():
    task = asyncio.create_task(asyncio.sleep(10))
    try:
        await asyncio.sleep(0.1)
        task.cancel()
        await task
    except asyncio.CancelledError:
        print("Cleanup: task cancelled")
```

This shows how cancellation works in asyncio and why cleanup is important.

## 5. Process pool tokenization

Create a function named `tokenize_in_process(text_chunks)`.

Requirements:

- use `ProcessPoolExecutor`
- each process counts tokens for a chunk of text
- combine the results in the parent process

Example idea:

```python
from concurrent.futures import ProcessPoolExecutor


def count_chunk(chunk):
    return len(chunk.split())


def tokenize_in_process(text_chunks):
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(count_chunk, text_chunks))
    return sum(results)
```

This demonstrates that multiprocessing can distribute work across CPU processes for heavier tasks.

## 6. Main guard

Protect any process-starting code with:

```python
if __name__ == "__main__":
    ...
```

This is required because Windows starts child processes differently, and without this guard your script can re-import itself unexpectedly.

## 7. Reflection Questions

Answer these after completing the stage:

1. Why do we use a `Lock` with threads?
2. Why is a `Queue` needed for processes?
3. What is the difference between threads and processes?
4. Why is `asyncio.gather(..., return_exceptions=True)` useful?
5. Why do we cancel tasks and do cleanup?
6. Why is `if __name__ == "__main__":` important on Windows?

## Completion Checklist

Stage 5 is complete when:

- thread-safe counting works with a `Lock`
- process results are returned through a `Queue`
- async tasks run and failures are handled
- cancellation catches `asyncio.CancelledError`
- process pool work is split across chunks
- the main guard is used properly
- you can explain the difference between thread, process, and async patterns
