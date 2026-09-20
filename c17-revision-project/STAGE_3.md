# Stage 3: Functions and Decorators

Stage 3 focuses on decorators, `*args`, `**kwargs`, pure functions, `functools.wraps`, and `time.perf_counter()`.

Create a new file named `stage3.py`. Do not change `stage2.py` for this stage.

## 1. Timing Decorator

Create a decorator named `timed`.

Requirements:

- accept a function
- create an inner wrapper
- wrapper accepts `*args` and `**kwargs`
- record the start time using `time.perf_counter()`
- call the original function
- record the ending time
- print how long the function took
- return the original function's result
- use `functools.wraps`

Test it with:

```python
@timed
def add(first, second):
    return first + second

result = add(2, 3)
print(result)
```

Expected result:

```text
5
```

The timing output will be different each time.

## 2. Decorator With Arguments

Test that the decorator works with a function that accepts positional arguments, keyword arguments, and returns a value:

```python
@timed
def create_topic_summary(topic, status="planned"):
    return f"{topic}: {status}"

print(create_topic_summary("Python", status="active"))
```

## 3. `*args`

Create:

```python
def choose_topics(*topics):
    ...
```

Test:

```python
result = choose_topics("Python", "Functions", "OOP")
print(result)
```

Understand that `topics` is a tuple:

```python
("Python", "Functions", "OOP")
```

## 4. `**kwargs`

Extend the function:

```python
def choose_topics(*topics, **options):
    ...
```

Test:

```python
choose_topics(
    "Python",
    "Functions",
    "OOP",
    status="active",
    limit=2,
)
```

Understand that `options` is a dictionary:

```python
{
    "status": "active",
    "limit": 2,
}
```

The function should return only the first `limit` topics when a limit is provided.

## 5. Pure Function

Create a pure function:

```python
def calculate_average(values):
    ...
```

Requirements:

- use only its arguments
- return the result
- do not modify global variables
- do not print
- do not write to a file
- return the same result for the same input

Test:

```python
print(calculate_average([2, 4, 6]))
```

Expected result:

```text
4.0
```

Handle an empty list clearly. You may return `0` or raise `ValueError`, but choose one behavior and understand why.

## 6. Reflection Questions

Answer these after completing the stage:

1. Why does a decorator receive a function?
2. Why does the wrapper need `*args` and `**kwargs`?
3. Why is `functools.wraps` useful?
4. What is the difference between `*args` and `**kwargs`?
5. Why is `calculate_average` a pure function?
6. What would make a function impure?

## Completion Checklist

Stage 3 is complete when:

- `timed` works with different functions
- the wrapper accepts positional and keyword arguments
- the original return value is preserved
- `functools.wraps` preserves the original function name
- `choose_topics` uses both `*args` and `**kwargs`
- `calculate_average` is pure
- empty input is handled deliberately
- you can explain each concept in your own words
