import unittest
from entities.task import Task
from repositories.task_repository import task_repository
from initialize_database import initialize_database

class TestTaskRepository(unittest.TestCase):
    def setUp(self):
        self.database = task_repository
        initialize_database()
        self.task1 = Task("Write some unit tests")
        self.task2 = Task("Refactor your code")

    def test_create_task(self):
        task_title = "Write down working hours"
        self.task3 = Task(task_title)
        self.database.create_task(self.task3)
    
        self.assertEqual(self.task3.title, "Write down working hours")

    def test_get_all_tasks_returns_tasks(self):
        self.database.create_task(self.task1)
        self.database.create_task(self.task2)
        tasks = self.database.get_all_tasks()

        self.assertEqual(tasks, ["Write some unit tests", "Refactor your code"])
