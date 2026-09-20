# Stage 2: Files and Reports

Stage 1 converted **one line** into **one validated `StudyTask`**.

Stage 2 connects many lines together:

```text
file -> load_tasks -> list[StudyTask] -> summarize/search -> Report file
```

For this stage, work only on these functions:

- `load_tasks`
- `save_report`
- `summarize`
- `search_tasks`
- `task_stream`

Do not work on decorators, OOP reports, threads, processes, asyncio, tokenization, or the CLI yet.

## 1. `load_tasks(path)`

Read `sample_tasks.txt` and return a list of `StudyTask` objects.

Requirements:

- use `with open(...)`
- read the file line by line
- skip blank lines
- call your existing `parse_task(line)` for each non-blank line
- catch expected parsing or validation errors for an individual line
- print or record which line was skipped
- allow the other valid lines to continue loading
- reject duplicate `task_id` values using a set

Expected result with the supplied sample file:

```python
len(tasks) == 7
```

Do not use `eval` or silently catch every possible exception.

## 2. `save_report(report, path)`

The `report` argument will be a string for this stage.

Requirements:

- open the destination with write mode
- use UTF-8 encoding
- write the report
- close the file automatically with `with`

Example use:

```python
save_report("Study Hub Report", Path("report.txt"))
```

## 3. `summarize(tasks)`

Return a dictionary containing:

```python
{
    "total_tasks": 7,
    "by_status": {
        "planned": 3,
        "active": 2,
        "done": 2,
    },
    "total_hours": 18.5,
    "unique_tags": {"functions", "lambda", "scope"},
    "completion_percentage": 28.57,
}
```

The exact hours and status counts should be calculated from the file, not hard-coded.

Requirements:

- count tasks by status
- add all task hours
- collect unique tags in a set
- calculate completed tasks divided by total tasks times 100
- handle an empty task list without division by zero
- use at least one meaningful comprehension

A useful formula is:

```text
completed tasks / total tasks * 100
```

## 4. `search_tasks(tasks, query)`

Return tasks whose topic contains the query, ignoring case.

Examples:

```python
search_tasks(tasks, "python")
search_tasks(tasks, "FUNCTION")
```

Both searches should work regardless of capitalization.

Requirements:

- do not modify the original task list
- return a list
- return an empty list when there are no matches
- strip surrounding whitespace from the query

## 5. `task_stream(path)`

This is the memory-efficient version of `load_tasks`.

Requirements:

- make it a generator function using `yield`
- read one line at a time
- validate each line through `parse_task`
- yield valid tasks one by one
- skip invalid lines with a useful message
- do not return the complete list

Check that it is really a generator:

```python
stream = task_stream(Path("sample_tasks.txt"))
print(type(stream))
print(next(stream))
```

## Required tests

Run these checks before asking for review:

```python
from pathlib import Path

data_path = Path("sample_tasks.txt")
tasks = load_tasks(data_path)
print(len(tasks))
print(summarize(tasks))
print(search_tasks(tasks, "FUNCTION"))

report_text = str(summarize(tasks))
save_report(report_text, Path("stage_2_report.txt"))
print(Path("stage_2_report.txt").read_text(encoding="utf-8"))

stream = task_stream(data_path)
print(type(stream))
print(next(stream))
```

Also test:

- a missing file
- an empty file
- a file with one malformed row
- a file with duplicate IDs
- a search with no matches
- an empty list passed to `summarize`

## Completion rule

Stage 2 is complete when:

- all seven sample tasks load
- the summary is calculated rather than hard-coded
- the report file is created and readable
- search works without changing the original list
- `task_stream` yields tasks one at a time
- invalid rows do not stop valid rows from loading

When finished, send me your five Stage 2 functions and test output. I will review only this stage before we continue.
