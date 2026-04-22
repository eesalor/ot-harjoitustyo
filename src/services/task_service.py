from entities.task import Task
from entities.category import Category
from repositories.task_repository import task_repository
from repositories.category_repository import category_repository

class TaskService:
    def __init__(self):
        self._task_repository = task_repository
        self._category_repository = category_repository

    def create_task(self, title, date, category):
        task = Task(title, date)

        if category:
            category_id = self._category_repository.get_category_id(category)
        else:
            category_id = None

        return self._task_repository.create_task(task, category_id)

    def get_all_tasks(self):
        return self._task_repository.get_all_tasks()

    def get_uncompleted_tasks(self):
        return self._task_repository.get_uncompleted_tasks()

    def get_completed_tasks(self):
        return self._task_repository.get_completed_tasks()

    def delete_task(self, task_id):
        return self._task_repository.delete_task(task_id)

    def set_completed(self, task_id):
        return self._task_repository.set_completed(task_id)

    def set_uncompleted(self, task_id):
        return self._task_repository.set_uncompleted(task_id)

    def get_categories(self):
        return self._category_repository.get_categories()

    def create_category(self, category):
        category = Category(title=category)

        return self._category_repository.create_category(category)

task_service = TaskService()
