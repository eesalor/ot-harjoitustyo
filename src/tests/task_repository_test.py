import unittest
from entities.task import Task
from entities.category import Category
from repositories.task_repository import task_repository
from repositories.category_repository import category_repository
from initialize_database import initialize_database

class TestTaskRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.database = task_repository
        self.categories_db = category_repository

        self.task1 = Task("Write some unit tests", "28.04.2026", False, 2)
        self.task2 = Task("Refactor your code", "5.5.2026", False, None)
        self.database.create_task(self.task1, 2)
        self.database.create_task(self.task2, None)

        self.categories_db.create_category(Category("Work"))
        self.categories_db.create_category(Category("Studies"))

        self.categories = self.categories_db.get_categories_with_id()

    def test_create_task_without_category_id(self):
        title = "Write down working hours"
        date = "9.4.2026"
        completed = False
        category_id = None
        self.task3 = Task(title, date, completed)
        self.database.create_task(self.task3, category_id)

        self.assertEqual(self.task3.title, "Write down working hours")
        self.assertEqual(self.task3.date, "9.4.2026")
        self.assertFalse(self.task3.completed)
        self.assertIsNone(self.task3.category)

    def test_create_task_with_category(self):
        title = "Write down working hours"
        date = "9.4.2026"
        completed = False
        category_id = 3
        self.task3 = Task(title, date, completed, category_id)
        self.database.create_task(self.task3, category_id)

        self.assertEqual(self.task3.title, "Write down working hours")
        self.assertEqual(self.task3.date, "9.4.2026")
        self.assertFalse(self.task3.completed)
        self.assertEqual(self.task3.category, 3)

    def test_get_tasks_returns_tasks(self):
        tasks = self.database.get_tasks()

        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[1].title, "Write some unit tests")
        self.assertEqual(tasks[1].date, "28.04.2026")
        self.assertEqual(tasks[1].category, "Studies")
        self.assertFalse(tasks[1].completed)
        self.assertEqual(tasks[2].title, "Refactor your code")
        self.assertEqual(tasks[2].date, "5.5.2026")
        self.assertIsNone(tasks[2].category)
        self.assertFalse(tasks[2].completed)

    def test_get_completed_tasks(self):
        self.database.set_completed(1)
        completed_tasks = self.database.get_completed_tasks()

        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(str(completed_tasks[1]), "28.04.2026 Write some unit tests Studies")

    def test_get_uncompleted_tasks(self):
        self.database.set_completed(1)

        uncompleted_tasks = self.database.get_uncompleted_tasks()

        self.assertEqual(len(uncompleted_tasks), 1)
        self.assertEqual(str(uncompleted_tasks[2]), "5.5.2026 Refactor your code (No category)")

    def test_delete_task(self):
        self.database.delete_task(1)

        tasks = self.database.get_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(repr(tasks), '{2: Refactor your code, 5.5.2026, None, False}')

        self.database.delete_task(2)
        tasks = self.database.get_tasks()

        self.assertEqual(len(tasks), 0)
        self.assertEqual(tasks, {})

    def test_set_task_completed_updates_completed_status(self):
        self.database.set_completed(1)
        tasks = self.database.get_tasks()

        self.assertTrue(tasks[1].completed, True)

    def test_set_task_uncompleted_updates_completed_status(self):
        self.database.set_completed(1)
        self.database.set_uncompleted(1)
        tasks = self.database.get_tasks()

        self.assertEqual(tasks[1].completed, False)

    def test_tasks_have_right_completed_status(self):
        self.database.set_completed(1)
        tasks = self.database.get_tasks()

        self.assertTrue(tasks[1].completed)
        self.assertFalse(tasks[2].completed)
