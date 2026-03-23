from entities.task import Task
from database_connection import get_database_connection

class TaskRepository:
    def __init__(self, connection):
        self._connection = connection


    def create_task(self, task: Task):
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO Tasks (title) VALUES (?)",
                       [task.title])
      
        self._connection.commit()

        
task_repository = TaskRepository(get_database_connection())
