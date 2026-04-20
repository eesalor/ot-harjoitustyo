from entities.task import Task
from database_connection import get_database_connection

class TaskRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_task(self, task: Task):
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO Tasks (title, date, completed) VALUES (?, ?, 0)",
                       [task.title, task.date])

        self._connection.commit()

    def get_all_tasks(self):
        cursor = self._connection.cursor()
        tasks = cursor.execute("SELECT id, title, date, completed FROM Tasks").fetchall()
        all_tasks = {}

        for row in tasks:
            task_id = row[0]
            task = Task(row[1], row[2])
            completed = row[3]
            if completed == 1:
                task.completed = True
            all_tasks[task_id] = str(task)

        return all_tasks

    def delete_task(self, task_id):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Tasks WHERE id = ?", [task_id])

        self._connection.commit()

    def set_completed(self, task_id):
        cursor = self._connection.cursor()

        cursor.execute("UPDATE Tasks SET completed = 1 WHERE id = ?",
                        [task_id])

task_repository = TaskRepository(get_database_connection())
