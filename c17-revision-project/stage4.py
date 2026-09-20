class Report:

    def __init__(self, title):
        self._title = title
        self.tasks = []

    @property #this gives controlled access of attribute
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if(not value.strip()):
            raise ValueError('Title cannot be empty')
        self._title = value

    @classmethod
    def from_tasks(cls, tasks, title="study report"):
        report = cls(title)
        report.tasks = tasks
        return report


    @staticmethod
    def format_percentage(value):
        return f'{float(value):.2f}%'

    def __len__(self):
        return len(self.tasks) # so with this len(report) works natually

    def __repr__(self):
        return f"Report(title={self.title!r}, task_count={len(self.tasks)})"

    def status_summary(self):
        summary = {
            'planned': 0,
            'active':0,
            'done':0
        }
        for task in self.tasks:
            if task.status.lower() == 'planned':
                summary['planned'] += 1
            elif task.status.lower() == 'active':
                summary['active'] += 1
            elif task.status.lower() == 'done':
                summary['done'] += 1
        return summary


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
print(report.status_summary())


#Composition: Use another object inside object instead of inheriting it
class TokenCounter:
    def __init__(self):
        self.model_name = 'demo'

    def count_words(self, text):
        return len(text.split())


class DetailedReport(Report):
    def __init__(self, title, tasks):
        super().__init__(title) #super calls the parent constructor, child gets what all parent behaviour
        self.tasks = tasks
        self.token_counter = TokenCounter()
        # Here detailedreport contains tokencounter, it is not a subclass.
        # it uses helper object when needed 




































# """Stage 4: OOP design for the Study Hub project.

# This file introduces the Report, DetailedReport, and TokenCounter concepts
# from the project README. It keeps the code simple enough to understand while
# showing the patterns used in a larger Python application.
# """

# from __future__ import annotations


# class TokenCounter:
#     """A small helper object used by composition instead of inheritance."""

#     def __init__(self, model_name: str = "study-hub") -> None:
#         self.model_name = model_name

#     def count_words(self, text: str) -> int:
#         words = text.split()
#         return len(words)

#     def preview(self, text: str, limit: int = 10) -> dict:
#         words = text.split()
#         selected = words[:limit]
#         return {
#             "model": self.model_name,
#             "word_count": len(words),
#             "preview_words": selected,
#             "preview_text": " ".join(selected),
#         }


# class Report:
#     """Represents a summary report built from a list of study tasks."""

#     def __init__(self, title: str) -> None:
#         self._title = title
#         self.tasks = []

#     @property
#     def title(self) -> str:
#         return self._title

#     @title.setter
#     def title(self, value: str) -> None:
#         if not value.strip():
#             raise ValueError("Title cannot be empty.")
#         self._title = value

#     @classmethod
#     def from_tasks(cls, tasks, title: str = "Study Report") -> "Report":
#         """Create a report from a collection of tasks."""
#         report = cls(title)
#         report.tasks = list(tasks)
#         return report

#     @staticmethod
#     def format_percentage(value: float) -> str:
#         return f"{value:.1f}%"

#     def __len__(self) -> int:
#         return len(self.tasks)

#     def __repr__(self) -> str:
#         return (
#             f"Report(title={self.title!r}, task_count={len(self)}, "
#             f"status_summary={self.status_summary()})"
#         )

#     def status_summary(self) -> dict:
#         counts = {"planned": 0, "active": 0, "done": 0}
#         for task in self.tasks:
#             status = getattr(task, "status", "planned")
#             if status in counts:
#                 counts[status] += 1
#         return counts

#     def total_hours(self) -> float:
#         return sum(getattr(task, "hours", 0) for task in self.tasks)

#     def completion_percentage(self) -> float:
#         if not self.tasks:
#             return 0.0
#         done_count = sum(1 for task in self.tasks if getattr(task, "status", "") == "done")
#         return (done_count / len(self.tasks)) * 100


# class DetailedReport(Report):
#     """A more detailed report that composes a TokenCounter."""

#     def __init__(self, title: str, tasks, token_counter: TokenCounter | None = None) -> None:
#         super().__init__(title)
#         self.tasks = list(tasks)
#         self.token_counter = token_counter or TokenCounter()

#     def add_task(self, task) -> None:
#         self.tasks.append(task)

#     def token_preview_for_topic(self, topic: str) -> dict:
#         text = f"Topic: {topic} summary for study planning and revision practice."
#         return self.token_counter.preview(text)

#     def __repr__(self) -> str:
#         return (
#             f"DetailedReport(title={self.title!r}, task_count={len(self)}, "
#             f"completion={self.format_percentage(self.completion_percentage())})"
#         )


# class StudyTask:
#     """Simple task placeholder used for demonstration in this stage."""

#     def __init__(self, topic: str, status: str, hours: float) -> None:
#         self.topic = topic
#         self.status = status
#         self.hours = hours


# if __name__ == "__main__":
#     tasks = [
#         StudyTask("Python basics", "done", 3),
#         StudyTask("Functions and scope", "active", 2),
#         StudyTask("OOP design", "planned", 4),
#         StudyTask("Concurrency", "done", 5),
#     ]

#     report = Report.from_tasks(tasks, title="Weekly Study Plan")
#     print(report)
#     print(f"Task count: {len(report)}")
#     print(f"Completion: {report.format_percentage(report.completion_percentage())}")
#     print(f"Total hours: {report.total_hours()}")

#     token_counter = TokenCounter("demo-counter")
#     detailed = DetailedReport("Detailed Weekly Study Plan", tasks, token_counter)
#     print(detailed)
#     print(detailed.token_preview_for_topic("OOP design"))

#     # Reflection questions for Stage 4
#     # 1. A class groups data and behavior in one object.
#     # 2. A property protects data and lets you validate changes.
#     # 3. A class method builds objects from other inputs.
#     # 4. Composition is useful when an object needs another helper without inheriting all of its behavior.
#     # 5. A static method is useful for utility logic that does not depend on instance state.
