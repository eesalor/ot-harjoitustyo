from entities.task import Task
from database_connection import get_database_connection

class TaskRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_task(self, task: Task):
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO Tasks (title, date) VALUES (?, ?)",
                       [task.title, task.date])

        self._connection.commit()

    def get_all_tasks(self):
        cursor = self._connection.cursor()
        tasks = cursor.execute("SELECT id, title, date FROM Tasks").fetchall()
        all_tasks = {}

        for row in tasks:
            id = row[0]
            task = Task(row[1], row[2])
            all_tasks[id] = str(task)

        return all_tasks

    def delete_task(self, id):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Tasks WHERE id = ?", [id])

        self._connection.commit()


task_repository = TaskRepository(get_database_connection())
