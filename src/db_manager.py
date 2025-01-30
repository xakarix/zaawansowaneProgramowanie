import sqlite3

DATABASE_FILE = "tasks.db"

def initialize_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            file_path TEXT,
            status TEXT,
            people_count INTEGER
        )    
    """)

    conn.commit()
    conn.close()

def add_task(file_path, status="pending", task_id=None, people_count=None):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (
            id,
            file_path,
            status,
            people_count
        )
        VALUES (?, ?, ?, ?)
    """, (task_id, file_path, status, people_count))

    conn.commit()
    conn.close()

    return task_id

def update_task(task_id, status, people_count=None):
    print(f"Updating task {task_id} with status: {status} and people_count: {people_count}")
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    if people_count is not None:
        cursor.execute("""
            UPDATE tasks SET status = ?, people_count = ? WHERE id = ? 
        """, (status, people_count, task_id))
    else:
        cursor.execute(""" 
            UPDATE tasks SET status =? WHERE id = ?""",
        (status, task_id))

    conn.commit()
    conn.close()


def pending_tasks():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tasks WHERE status = 'pending'
    """)
    
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def in_progress_tasks():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tasks WHERE status = 'in progress'
    """)
    
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def done_tasks():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tasks WHERE status = 'done'
    """)
    
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def get_task(task_id):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tasks WHERE id = ?
    """, (task_id,))
    
    task = cursor.fetchone()
    conn.close()

    if task:
        task_dict = {
            "id": task[0],
            "file_path": task[1],
            "status": task[2],
            "people_count": task[3]
        }
        return task_dict
    else:
        return None


initialize_database()
