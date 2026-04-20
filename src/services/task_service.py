from entities.task import Task
from repositories.task_repository import task_repository

class TaskService:
    def __init__(self):
        self._task_repository = task_repository

    def create_task(self, title, date):
        task = Task(title, date)
        return self._task_repository.create_task(task)

    def get_all_tasks(self):
        return self._task_repository.get_all_tasks()

    def delete_task(self, task_id):
        return self._task_repository.delete_task(task_id)

    def set_completed(self, task_id):
        return self._task_repository.set_completed(task_id)

task_service = TaskService()
