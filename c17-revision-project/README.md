# Python Revision Test: Study Hub

Build a command-line **Study Hub** that reads study tasks from a file, validates them, calculates progress, and produces reports using several execution styles.

This is a revision test, not a copy-paste tutorial. Complete the TODOs in `starter.py` without looking up a complete solution. You may use Python documentation for syntax and standard-library APIs.

## How we will work

Do not try to complete the whole file at once. Work through one stage at a time. For each stage, implement only the named TODOs, run the small checks, and ask for a review before moving forward. Start with [STAGE_1.md](STAGE_1.md), then continue with [STAGE_2.md](STAGE_2.md) and [STAGE_3.md](STAGE_3.md).

## Concepts being tested

- variables, strings, numbers, booleans, lists, tuples, dictionaries, sets and membership
- indexing, unpacking, mutation, `get`, `set`, `frozenset`, and `bytearray`
- `if`/`elif`/`else`, conditional expressions, `match`, `for`, `while`, `range`, `enumerate`, `zip`, `continue`
- functions, return values, default arguments, `*args`, `**kwargs`, scope, pure functions, lambdas, `map`, `filter`, sorting, the walrus operator
- list, set and dictionary comprehensions
- generator functions, generator expressions, `yield`, `send`, `yield from`, `next`, and `close`
- decorators and `functools.wraps`
- classes, constructors, instance/class/static methods, properties, setters, inheritance, composition, `super`, MRO, and operator overloading
- custom exceptions, `try`/`except`/`else`/`finally`, validation and graceful failure
- reading, writing, appending and safely closing files
- Pydantic models, `Field`, `Literal`, field/model validators, computed fields and serialization
- threads, locks, processes, `Queue`, `Value`, asyncio tasks, `gather`, cancellation, `to_thread`, and a process pool
- tokenization with `tiktoken`

## Rules

1. Work only in `starter.py` and add small helper modules only when you can explain why.
2. Use the sample file first, then test empty files, malformed rows, duplicate IDs, invalid statuses, negative hours and missing files.
3. Keep the program usable from the terminal. Do not hide errors with a bare `except`.
4. Do not remove a TODO until the related behavior works.
5. Before asking for help, write down what you expected, what happened, and the smallest input that reproduces it.

## Run

From this folder:

```powershell
..\c16-tokenization\venv\Scripts\python.exe starter.py
```

Install the two external packages if needed:

```powershell
..\c16-tokenization\venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Assessment stages

### Stage 1: Data and validation

See [STAGE_1.md](STAGE_1.md) for the focused instructions and tests.

Implement `StudyTask`, validation, and `parse_task`. A task has:

- `task_id`: positive integer
- `topic`: at least 3 characters
- `status`: exactly `planned`, `active`, or `done`
- `hours`: number from 0 through 100
- optional `tags`: list of strings

The input file uses this format:

```text
id|topic|status|hours|tag1,tag2
```

Malformed rows must be reported and skipped rather than crashing the whole program.

### Stage 2: Files and core Python

See [STAGE_2.md](STAGE_2.md) for the focused instructions and tests.

Implement `load_tasks`, `save_report`, `summarize`, `search_tasks`, and `task_stream`.

Use a context manager for files. `task_stream` must be a generator that yields one validated task at a time. The summary must include counts by status, total hours, unique tags, and completion percentage.

Use at least one list comprehension, set comprehension, dictionary comprehension, `enumerate`, `zip`, `filter` or `map`, and a lambda in meaningful places.

### Stage 3: Functions and decorators

Implement `timed` with `functools.wraps`. Apply it to one report function. The wrapper must accept arbitrary positional and keyword arguments and return the wrapped result.

Add a function that accepts `*topics` and `**options`, and explain in a short comment or docstring how scope is being used. Include one pure function and keep file or global state out of it.

### Stage 4: OOP design

Create a `Report` class with a property for the title, a class method that builds a report from tasks, a static method for percentage formatting, and `__len__` or `__repr__`.

Create a `DetailedReport` child class that extends `Report` with `super()`. Use composition for a small `TokenCounter` object instead of inheriting from it.

### Stage 5: Concurrency

Implement these as separate functions:

- `threaded_status_counts`: two or more threads read independent pieces of work and combine results safely with a `Lock`.
- `process_hour_totals`: use a process and a `multiprocessing.Queue` to return a result to the parent.
- `async_report`: use `asyncio.create_task` or `gather` for at least three simulated I/O tasks. Catch one task failure with `return_exceptions=True`.
- `cancel_preview`: start a timer-like task, cancel it, catch `asyncio.CancelledError`, and perform cleanup.
- `tokenize_in_process`: use `ProcessPoolExecutor` to count tokens for text chunks.

Protect process-starting code with `if __name__ == "__main__":`.

### Stage 6: Tokenization and final CLI

Use `tiktoken.encoding_for_model("gpt-4o")` in `TokenCounter`. Report token IDs, token count, and decoded text for a short preview. Finish a menu using `match` with these commands:

- `1`: show summary
- `2`: search by topic
- `3`: show token information
- `4`: run concurrency demonstrations
- `5`: save a report and quit

The menu must handle invalid input without terminating unexpectedly.

## Self-check scenarios

Before grading, verify these cases manually:

- normal sample data produces a non-zero completion percentage
- a missing file gives a useful message
- a row with `hours=abc` is skipped and explained
- duplicate task IDs are rejected or clearly handled
- a search with no matches returns an empty result cleanly
- the lock-protected counter reaches the expected total
- async cancellation prints cleanup output
- a report can be saved and opened again
- the program still works when tags are empty

## Deliverables

- completed `starter.py`
- one saved report file generated by the program
- a short `REFLECTION.md` answering:
  1. Which concept was easiest and why?
  2. Which bug took the longest to understand?
  3. When would you choose a thread, process, or async task here?
  4. What would you improve before calling this production-ready?
