from pydantic import BaseModel, Field
from typing import Literal

class StudyTask(BaseModel):
    task_id:int = Field(gt=0)
    topic:str = Field(min_length=3)
    status:Literal['planned','active','done']
    hours:float = Field(ge=0, le=100)
    tags:list[str]


def parse_task(line):
    listline = [item.strip() for item in line.split('|')]
    if len(listline) != 5:
        raise ValueError('line provided should contains 5 fields')
    task_id = int(listline[0])
    topic = clean_topic(listline[1])
    status = listline[2]
    hours = validate_done_task(float(listline[3]), status)
    tags = clean_tags(listline[4])
    return StudyTask(task_id= task_id, topic = topic, status= status, hours = hours, tags = tags)

def clean_topic(topic):
    return topic.strip()

def clean_tags(tag):
    tags = [item for item in tag.split(',') if item != '']
    return [item.strip() for item in tags]

def validate_done_task(hours, status):
    if hours == 0 and status == 'done':
        raise ValueError('Task rejected due to 0 hours')
    return hours


if __name__ == "__main__":
    print(parse_task("2|Functions and scope|active|3|functions,lambda,scope"))
    print(parse_task("3|  Generators  |planned|2| generators, decorators "))
