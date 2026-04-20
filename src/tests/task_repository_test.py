import unittest
from entities.task import Task
from repositories.task_repository import task_repository
from initialize_database import initialize_database

class TestTaskRepository(unittest.TestCase):
    def setUp(self):
        self.database = task_repository
        initialize_database()

        self.task1 = Task("Write some unit tests", "2026-04-04")
        self.task2 = Task("Refactor your code", "2026-05-05")

    def test_create_task(self):
        task_title = "Write down working hours"
        task_date = "2026-04-09"
        self.task3 = Task(task_title, task_date)
        self.database.create_task(self.task3)
    
        self.assertEqual(self.task3.title, "Write down working hours")
        self.assertEqual(self.task3.date, "2026-04-09")

    def test_get_all_tasks_returns_tasks(self):
        self.database.create_task(self.task1)
        self.database.create_task(self.task2)
        tasks = self.database.get_all_tasks()

        self.assertEqual(tasks, {1: "Write some unit tests 2026-04-04", 2: "Refactor your code 2026-05-05"})

    def test_delete_task(self):
        self.database.create_task(self.task1)
        self.database.create_task(self.task2)

        self.database.delete_task(1)
        self.database.delete_task(2)

        tasks = self.database.get_all_tasks()

        self.assertEqual(tasks, {})

    def test_set_task_completed_updates_completed_status(self):
        self.database.create_task(self.task1)

        self.database.set_completed(1)

        tasks = self.database.get_all_tasks_as_objects()

        self.assertEqual(tasks[1].completed, True)

    def test_tasks_have_right_completed_status(self):
        self.database.create_task(self.task1)
        self.database.create_task(self.task2)

        self.database.set_completed(1)

        tasks_as_objects = self.database.get_all_tasks_as_objects()

        self.assertEqual(tasks_as_objects[1].completed, True)
        self.assertEqual(tasks_as_objects[2].completed, False)

        tasks = self.database.get_all_tasks()

        self.assertEqual(tasks[1], f"{self.task1.title} {self.task1.date} (completed)")
        self.assertEqual(tasks[2], f"{self.task2.title} {self.task2.date}")
