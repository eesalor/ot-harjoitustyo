from entities.task import Task
from repositories.task_repository import task_repository

class TaskService:
    def __init__(self):
        self._task_repository = task_repository

    def create_task(self, entry):
        task = Task(entry)
        return self._task_repository.create_task(task)

    def get_all_tasks(self):
        return self._task_repository.get_all_tasks()
        

task_service = TaskService()
