from entities.task import Task
from database_connection import get_database_connection

class TaskRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_task(self, task: Task, category_id):
        cursor = self._connection.cursor()

        cursor.execute("""INSERT INTO Tasks (title, date, category_id, completed)
                    VALUES (?, ?, ?, 0)""",
                       [task.title, task.date, category_id])

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

    def get_all_tasks_as_objects(self):
        cursor = self._connection.cursor()
        tasks = cursor.execute("""SELECT id, title, date, completed, category_id
                               FROM Tasks""").fetchall()
        all_task_objects = {}

        for row in tasks:
            task_id = row[0]
            task = Task(row[1], row[2])
            completed = row[3]
            if completed == 1:
                task.completed = True
            task.category = row[4]

            all_task_objects[task_id] = task

        return all_task_objects

    def get_tasks_with_categories(self, categories):

        cursor = self._connection.cursor()
        tasks = cursor.execute("""SELECT id, title, date, completed, category_id
                               FROM Tasks""").fetchall()

        all_task_objects = {}

        for row in tasks:
            task_id = row[0]
            task = Task(row[1], row[2])
            completed = row[3]

            if completed == 1:
                task.completed = True

            category_id = row[4]
            if category_id:
                task.category = categories[category_id]

            all_task_objects[task_id] = str(task)

        return all_task_objects

    def get_uncompleted_tasks_with_categories(self, categories):

        cursor = self._connection.cursor()
        tasks = cursor.execute("""SELECT id, title, date, completed, category_id FROM Tasks
                               WHERE completed = 0""").fetchall()

        uncompleted_task_objects = {}

        for row in tasks:
            task_id = row[0]
            task = Task(row[1], row[2])
            task.completed = False
            category_id = row[4]
            if category_id:
                task.category = categories[category_id]

            uncompleted_task_objects[task_id] = str(task)

        return uncompleted_task_objects

    def get_completed_tasks_with_categories(self, categories):

        cursor = self._connection.cursor()
        tasks = cursor.execute("""SELECT id, title, date, completed, category_id FROM Tasks
                               WHERE completed = 1""").fetchall()

        completed_task_objects = {}

        for row in tasks:
            task_id = row[0]
            task = Task(row[1], row[2])
            task.completed = True
            category_id = row[4]
            if category_id:
                task.category = categories[category_id]

            completed_task_objects[task_id] = str(task)

        return completed_task_objects


    def get_uncompleted_tasks(self):
        cursor = self._connection.cursor()

        tasks = cursor.execute("SELECT id, title, date, completed FROM Tasks").fetchall()

        all_uncompleted_tasks = {}

        for row in tasks:
            task_id = row[0]
            task = Task(row[1], row[2])
            completed = row[3]
            if completed == 0:
                all_uncompleted_tasks[task_id] = str(task)

        return all_uncompleted_tasks

    def get_completed_tasks(self):
        cursor = self._connection.cursor()

        tasks = cursor.execute("SELECT id, title, date, completed FROM Tasks").fetchall()

        all_completed_tasks = {}

        for row in tasks:
            task_id = row[0]
            task = Task(row[1], row[2])
            completed = row[3]
            if completed == 1:
                all_completed_tasks[task_id] = str(task)

        return all_completed_tasks

    def delete_task(self, task_id):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Tasks WHERE id = ?", [task_id])

        self._connection.commit()

    def set_completed(self, task_id):
        cursor = self._connection.cursor()

        cursor.execute("UPDATE Tasks SET completed = 1 WHERE id = ?",
                        [task_id])

        self._connection.commit()

    def set_uncompleted(self, task_id):
        cursor = self._connection.cursor()

        cursor.execute("UPDATE Tasks SET completed = 0 WHERE id = ?",
                        [task_id])

        self._connection.commit()

    def delete_category_from_task(self, category_id):
        cursor = self._connection.cursor()

        cursor.execute("""UPDATE Tasks SET category_id = ?
                       WHERE category_id = ?""", [None, category_id])

        self._connection.commit()

task_repository = TaskRepository(get_database_connection())
