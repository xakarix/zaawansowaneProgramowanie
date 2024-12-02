import uuid


def save_task(filename="tasks.txt"):
    task_id = uuid.uuid4()
    task = f"id: {task_id}, status: pending\n"

    with open(filename, "a") as file:
        file.write(task)

    print(f"Zapisano do pliku {filename}: {task.strip()}")


save_task()
