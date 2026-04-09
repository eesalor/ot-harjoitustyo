import unittest
from entities.task import Task
from services.task_service import task_service
from repositories.task_repository import task_repository

class TestTaskService(unittest.TestCase):
    def setUp(self):
        self.service = task_service
        self.task_repository = task_repository
        self.title = "Write some unit tests"
        self.date = "2026-04-04"

    def test_create_task(self):
        result = self.service.create_task(self.title, self.date)
        self.assertEqual(result, self.task_repository.create_task(Task(self.title, self.date)))

    def test_get_all_tasks(self):
        self.service.create_task(self.title, self.date)
        result = self.service.get_all_tasks()

        self.assertEqual(result, self.task_repository.get_all_tasks())

    def test_delete_task(self):
        self.service.create_task(self.title, self.date)
        result = self.service.delete_task(1)

        self.assertEqual(result, self.task_repository.delete_task(1))
