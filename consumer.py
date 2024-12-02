import time
import sqlite3

db_name = "tasks.db"


def initialize_db():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(
        """ 
                   CREATE TABLE IF NOT EXISTS tasks (
                       id TEXT PRIMARY KEY,
                       status TEXT
                   )
                   """
    )

    conn.commit()
    conn.close()


def get_pending_tasks():
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """ 
                       SELECT id, status FROM tasks WHERE status = ?
                       """,
            ("pending",),
        )
        return cursor.fetchall()


def update_task(task_id: str, status: str):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """ 
                       UPDATE tasks SET status = ? WHERE id = ?
                       """,
            (status, task_id),
        )
        conn.commit()


def consume_tasks():
    while True:
        pending_tasks = get_pending_tasks()

        if pending_tasks:
            task_id, _ = pending_tasks[0]
            print(f"Now consuming task: {task_id}")

            update_task(task_id, "in_progress")

            time.sleep(30)

            update_task(task_id, "done")
            print(f"Task {task_id} is done.")
        else:
            print("No pending tasks. Waiting...")
            time.sleep(5)


initialize_db()
consume_tasks()
