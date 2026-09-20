from stage1 import parse_task
from pathlib import Path

def load_tasks(path):
    see_ids = set()
    task_list = list()
    try:
        with open(path, 'r', encoding='utf-8') as sampleFile:
            for line_no, line in enumerate(sampleFile, start=1):
                if not line.strip():
                    print(f'Skipped line: {line_no}')
                    continue
                try:
                    task = parse_task(line)
                except (ValueError, TypeError) as error:
                    print(f'Skipped invalid line {line_no} and task_id:{task.task_id} with error: {error}')
                    continue

                if task.task_id in see_ids:
                    raise ValueError(f'Task id is duplicated for task_id: {task.task_id}')

                see_ids.add(task.task_id)
                task_list.append(task)

    except FileNotFoundError as e:
        print('Error: File not found')
        return []
    return task_list

def save_report(report: str, path):
    with open(path, 'w',-1, encoding='utf-8') as file:
        file.write(report)



def summarize(tasks):
    plannedTasks = 0
    activeTasks = 0
    doneTasks = 0
    totalHrs = 0
    unique_task = set()

    for task in tasks:
        if task.status.lower() == 'planned':
            plannedTasks += 1
        elif task.status.lower() == "active":
            activeTasks += 1
        elif task.status.lower() == 'done':
            doneTasks += 1
        totalHrs += task.hours
        [unique_task.add(tag) for tag in task.tags]

    return {
        "total_tasks": len(tasks),
        "by_status": {
            "planned": plannedTasks,
            "active": activeTasks,
            "done": doneTasks
        },
        "total_hours": round(totalHrs,2),
        "unique_tags": unique_task,
        "completion_percentage": round((doneTasks / len(tasks)) * 100,2) if len(tasks) > 0 else 0

    }

def search_tasks(tasks, query):
    return [task for task in tasks if query.lower() in task.topic.lower()]


def task_stream(path):
    task_list = []
    seen_ids = set()
    with open(path, 'r', encoding='utf-8') as file:
        for line_no, line in enumerate(file, start=1):
            if not line.strip():
                print(f'Skipped line {line_no}')
                continue
            try:
                task = parse_task(line)
                yield task
            except (ValueError, TypeError) as error:
                print(f'Skipped invalid line {line_no} and task_id:{task.task_id} with error: {error}')
                continue

            if task.task_id in seen_ids:
                raise ValueError(f'Task id is duplicated for task_id: {task.task_id}')

            seen_ids.add(task.task_id)
            task_list.append(task)


if __name__ == "__main__":
    tasks = load_tasks('sample_tasks.txt')
    save_report("Study Hub Report", "report.txt")
    # print(summarize(tasks))
    print(search_tasks(tasks, 'python'))
    print(search_tasks(tasks, 'FUNCTION'))