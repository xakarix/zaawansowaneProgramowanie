import time

filename = "tasks.txt"


def consume_tasks():
    while True:
        pending_tasks = []
        updated_tasks = []

        try:
            with open(filename, "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    updated_tasks.append(task)
                    if "status: pending" in task:
                        pending_tasks.append(task)

        except FileNotFoundError:
            print("file doesn't exist")
            time.sleep(5)
            continue

        if pending_tasks:
            task = pending_tasks.pop(0)
            task_part = task.split(", ")
            task_id = task_part[0].split(": ")[1]
            print(f"Now consuming task: {task_id}")

            in_progress_task = task.replace("pending", "in_progress")
            for i, t in enumerate(updated_tasks):
                if task_id in t:
                    updated_tasks[i] = in_progress_task
                    break

            with open(filename, "w") as file:
                file.writelines(updated_tasks)

            time.sleep(30)

            done_task = in_progress_task.replace("in_progress", "done")
            for i, t in enumerate(updated_tasks):
                if task_id in t:
                    updated_tasks[i] = done_task
                    break

            with open(filename, "w") as file:
                file.writelines(updated_tasks)
            print(f"Task {task_id} is done!")
        else:
            print("No pending tasks. Waiting..")
            time.sleep(5)


consume_tasks()
