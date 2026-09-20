# Stage 1: One Task In, One Valid Task Out

Ignore every TODO except these three areas for now:

- `StudyTask.clean_topic`
- `StudyTask.clean_tags`
- `StudyTask.validate_done_task`
- `parse_task`

Do not implement files, reports, threads, processes, asyncio, tokenization, or the menu yet.

## Goal

Turn this input line:

```text
2|Functions and scope|active|3|functions,lambda,scope
```

into one `StudyTask` object with:

```python
StudyTask(
    task_id=2,
    topic="Functions and scope",
    status="active",
    hours=3.0,
    tags=["functions", "lambda", "scope"],
)
```

## Your tasks

1. In `clean_topic`, remove whitespace around the topic.
2. In `clean_tags`, convert the tag text into a list. Strip each tag and ignore empty tags.
3. In `validate_done_task`, reject a `done` task whose hours are `0`.
4. In `parse_task`:
   - split the line using `|`
   - require exactly five fields
   - convert the ID to `int`
   - convert hours to `float`
   - pass all values into `StudyTask`
   - let invalid data raise a useful exception for now

## Small tests to run

Add these temporary calls at the bottom of the file, or run them from a Python prompt by importing the module:

```python
print(parse_task("2|Functions and scope|active|3|functions,lambda,scope"))
print(parse_task("3|  Generators  |planned|2| generators, decorators "))
```

Then test that each case fails:

```python
parse_task("0|Python|planned|2|")
parse_task("4|Py|done|0|")
parse_task("5|Python|unknown|2|")
parse_task("6|Python|active|abc|")
parse_task("bad row")
```

You should see validation or parsing exceptions. That is correct for Stage 1. Do not catch and hide them yet.

## What to understand before moving on

Be able to explain:

- Why `StudyTask(...)` is better than passing an unchecked dictionary around.
- What `Field(gt=0)` and `Field(ge=0, le=100)` do.
- Why the `mode="before"` validators run before Pydantic converts values.
- Why `Literal[...]` rejects an unknown status.
- Why `parse_task` should focus on one line while `load_tasks` will later focus on the whole file.

## Completion rule

You are finished with Stage 1 when:

- both valid examples create the expected object
- all five invalid examples raise an understandable error
- you can explain the five points above in your own words

Then send me your `StudyTask` and `parse_task` code, plus any error output. I will review it and give you only the next small change.
