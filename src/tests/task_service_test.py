import unittest
from entities.task import Task
from entities.category import Category
from services.task_service import task_service
from repositories.task_repository import task_repository
from repositories.category_repository import category_repository
from initialize_database import initialize_database

class TestTaskService(unittest.TestCase):
    def setUp(self):
        self.service = task_service
        self.task_repository = task_repository
        self.category_repository = category_repository

        initialize_database()

        self.title = "Write some unit tests"
        self.date = "4.4.2030"
        self.completed = False
        self.category = "Studies"

    def test_create_task_without_category(self):
        category_none = None

        result = self.service.create_task(self.title, self.date, category_none)

        category_id = None

        self.assertEqual(result, self.task_repository.create_task(Task(self.title, self.date), category_id))

    def test_get_all_tasks(self):
        result = self.service.get_all_tasks()

        self.assertEqual(result, self.task_repository.get_all_tasks_as_objects())

    def test_delete_task(self):
        result = self.service.delete_task(1)

        self.assertEqual(result, self.task_repository.delete_task(1))

    def test_set_completed(self):
        result = self.service.set_completed(1)

        self.assertEqual(result, self.task_repository.set_completed(1))

    def test_set_uncompleted(self):
        self.service.set_completed(1)

        result = self.service.set_uncompleted(1)

        self.assertEqual(result, self.task_repository.set_uncompleted(1))