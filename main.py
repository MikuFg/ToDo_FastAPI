from fastapi import FastAPI
from models import Task
import json

app = FastAPI()

json_file = "tasks.json"


def get_all_tasks(file):
    try:
        with open(file, 'r+', encoding="UTF-8") as f:
            data = json.load(f)
    except Exception as e:
        return {}

    print(data)
    return data


def add_task(file, new_task: Task):
    data = get_all_tasks(json_file)

    cur_id = 1

    if data == {}:
        cur_id = 1
    else:
        for key in data.keys():
            cur_id += 1


    data[cur_id] = {"shortname":new_task.shortname, "description":new_task.description, "iscompleted":new_task.iscompleted}

    try:
        with open(file, 'w', encoding='UTF-8') as f:
            json.dump(data, f, ensure_ascii = False, indent = 4)

    except Exception as e:
        return e
    
    return {"result":"new task was added!"}


def update_status(id, file):
    data = get_all_tasks(json_file)

    if data == {}:
        return "No task was added("

    for key, values in data.items():
        if key == id:

            if values["iscompleted"] == False:
                values["iscompleted"] = True

            else:
                values["iscompleted"] = False

            try:
                with open(file, 'w', encoding='UTF-8') as f:
                    json.dump(data, f, ensure_ascii = False, indent = 4)

            except Exception as e:
                return e

    return "All good"



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
    update_status(task_id, json_file)

    return{"Result":"All good!"}
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)