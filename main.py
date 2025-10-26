from fastapi import FastAPI
from models import Task
import json

app = FastAPI()

json_file = "tasks.json"


def get_all_tasks(file) -> list[dict]:
    try:
        with open(file, 'r+', encoding="UTF-8") as f:
            data = json.load(f)
    except Exception as e:
        return []

    return [data]


def add_task(file, new_task: Task):
    data = get_all_tasks(json_file)

    data.append(new_task.model_dump())

    try:
        with open(file, 'w', encoding='UTF-8') as f:
            json.dump(data, f, ensure_ascii = False, indent = 4)

    except Exception as e:
        return e
    
    return {"result":"new task was added!"}


def update_status(id):
    data = get_all_tasks(json_file)

    if data == []:
        return "No task was added("

    for task in data:
        print(task)
        if task[0] == id:
            print(1)
            if task[-1] == False:
                print(1)
                task[-1] = True
            task[-1] = False

    return "Status was update!"



@app.get('/tasks')
async def tasks():
    data = get_all_tasks(json_file)

    return {"Result": data}

@app.post('/addTask')
async def new_task(insert_data: Task):
    add_task(json_file, insert_data)

    return{"Result":"all good)"}


@app.put('/taskUpdate/{task_id}')
async def taskUpdate(task_id):
    update_status(task_id)

    return{"Result":"All good!"}
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)