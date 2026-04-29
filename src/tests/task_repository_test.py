import unittest
from entities.task import Task
from repositories.task_repository import task_repository
from initialize_database import initialize_database

class TestTaskRepository(unittest.TestCase):
    def setUp(self):
        self.database = task_repository
        initialize_database()

        self.task1 = Task("Write some unit tests", "28.04.2026", False, 2)
        self.task2 = Task("Refactor your code", "5.5.2026", False, None)
        self.database.create_task(self.task1, 2)
        self.database.create_task(self.task2, None)

    def test_create_task_without_category_id(self):
        title = "Write down working hours"
        date = "9.4.2026"
        completed = False
        category_id = None
        self.task3 = Task(title, date, completed, category_id)
        self.database.create_task(self.task3, category_id)

        self.assertEqual(self.task3.title, "Write down working hours")
        self.assertEqual(self.task3.date, "9.4.2026")
        self.assertEqual(self.task3.completed, False)
        self.assertEqual(self.task3.category, None)

    def test_create_task_with_category_id(self):
        title = "Write down working hours"
        date = "9.4.2026"
        completed = False
        category_id = 3
        self.task3 = Task(title, date, completed, category_id)
        self.database.create_task(self.task3, category_id)

        self.assertEqual(self.task3.title, "Write down working hours")
        self.assertEqual(self.task3.date, "9.4.2026")
        self.assertEqual(self.task3.completed, False)
        self.assertEqual(self.task3.category, 3)

    def test_get_all_tasks_returns_tasks(self):
        tasks = self.database.get_all_tasks()

        self.assertEqual(repr(tasks[1]), "(Write some unit tests, 28.04.2026, 2, False)")
        self.assertEqual(repr(tasks[2]), "(Refactor your code, 5.5.2026, None, False)")

    def test_get_completed_tasks_without_categories(self):
        self.database.set_completed(1)

        completed_tasks = self.database.get_completed_tasks()

        self.assertEqual(completed_tasks, {1: '(Write some unit tests, 28.04.2026, None, False)'})

    def test_get_uncompleted_tasks(self):
        self.database.set_completed(1)

        uncompleted_tasks = self.database.get_uncompleted_tasks()

        self.assertEqual(uncompleted_tasks, {2: '(Refactor your code, 5.5.2026, None, False)'})

    def test_delete_task(self):
        self.database.delete_task(1)
        self.database.delete_task(2)

        tasks = self.database.get_all_tasks()

        self.assertEqual(tasks, {})

    def test_set_task_completed_updates_completed_status(self):
        self.database.set_completed(1)

        tasks = self.database.get_all_tasks()

        self.assertEqual(tasks[1].completed, True)

    def test_set_task_uncompleted_updates_completed_status(self):
        self.database.set_completed(1)
        self.database.set_uncompleted(1)

        tasks = self.database.get_all_tasks()

        self.assertEqual(tasks[1].completed, False)

    def test_tasks_have_right_completed_status(self):
        self.database.create_task(self.task1, 2)
        self.database.create_task(self.task2, None)

        self.database.set_completed(1)

        tasks = self.database.get_all_tasks()

        self.assertEqual(tasks[1].completed, True)
        self.assertEqual(tasks[2].completed, False)

        self.assertEqual(repr(tasks[1]), "(Write some unit tests, 28.04.2026, 2, True)")
        self.assertEqual(repr(tasks[2]), "(Refactor your code, 5.5.2026, None, False)")

