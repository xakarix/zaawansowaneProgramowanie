import sqlite3
import uuid

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


def add_task():
    task_id = str(uuid.uuid4())
    status = "pending"

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(
        """
                   INSERT INTO tasks (id, status)
                   VALUES (?, ?)
                   """,
        (task_id, status),
    )

    conn.commit()
    conn.close()
    print(f"New Task: {task_id}, status: {status}")


initialize_db()
add_task()
