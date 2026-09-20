# Stage 4: OOP Design

Stage 4 focuses on object-oriented programming, properties, class methods, static methods, inheritance, and composition.

Create a new file named `stage4.py`. Do not change earlier stage files for this stage.

## 1. Report Class

Create a class named `Report`.

Requirements:

- it should store a title
- it should be able to hold a list of tasks
- it should have a property for the title
- it should raise an error if the title is empty
- it should have a class method that builds a report from tasks
- it should have a static method for percentage formatting
- it should have `__len__` and `__repr__`

Example structure:

```python
class Report:
    def __init__(self, title):
        ...

    @property
    def title(self):
        ...

    @title.setter
    def title(self, value):
        ...

    @classmethod
    def from_tasks(cls, tasks, title="Study Report"):
        ...

    @staticmethod
    def format_percentage(value):
        ...

    def __len__(self):
        ...

    def __repr__(self):
        ...
```

Test it with:

```python
class StudyTask:
    def __init__(self, topic, status, hours):
        self.topic = topic
        self.status = status
        self.hours = hours


tasks = [
    StudyTask("Python", "done", 2),
    StudyTask("Functions", "active", 3),
    StudyTask("OOP", "planned", 4),
]

report = Report.from_tasks(tasks, title="Weekly Study Plan")
print(report)
print(len(report))
print(Report.format_percentage(75))
```

Expected behavior:

- `report.title` is accessible
- the report stores the tasks
- `len(report)` returns the number of tasks
- `Report.format_percentage(75)` returns `75.0%`

## 2. Status Summary

Add a method to `Report` that calculates counts by status.

Example:

```python
print(report.status_summary())
```

This could return something like:

```python
{"planned": 1, "active": 1, "done": 1}
```

You may also add methods such as:

- `total_hours()`
- `completion_percentage()`

These should use the task data and not rely on global state.

## 3. DetailedReport Child Class

Create a child class named `DetailedReport`.

Requirements:

- it must inherit from `Report`
- it must call `super().__init__()`
- it should add extra behavior, such as a detailed summary
- it should still use the parent methods

Example:

```python
class DetailedReport(Report):
    def __init__(self, title, tasks):
        super().__init__(title)
        self.tasks = tasks
```

You may add extra methods like:

- `add_task(task)`
- `task_count_by_status()`
- `topic_overview()`

## 4. Composition with TokenCounter

Create a small helper class named `TokenCounter`.

Requirements:

- it should be a separate class
- `DetailedReport` should use it using composition
- do not inherit from it

Example:

```python
class TokenCounter:
    def __init__(self, model_name="demo"):
        self.model_name = model_name

    def count_words(self, text):
        ...
```

Use it inside `DetailedReport` like this:

```python
self.token_counter = TokenCounter()
```

This shows composition: the report contains a helper object instead of becoming a token counter itself.

## 5. Reflection Questions

Answer these after completing the stage:

1. What is the difference between a class and an instance?
2. Why is a property useful in a class like `Report`?
3. Why does `super()` help in a child class?
4. What is the difference between inheritance and composition?
5. Why is `@classmethod` useful for creating objects from data?
6. Why is `@staticmethod` useful for utility logic?

## Completion Checklist

Stage 4 is complete when:

- `Report` stores a title and tasks
- the title property validates empty values
- `from_tasks` builds a report from task objects
- `format_percentage` works correctly
- `__len__` and `__repr__` are implemented
- `DetailedReport` inherits from `Report` and uses `super()`
- a `TokenCounter` is used by composition
- you can explain each concept in your own words
