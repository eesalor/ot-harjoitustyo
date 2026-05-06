import unittest
from datetime import date, timedelta
from entities.task import Task
from entities.category import Category
from services.task_service import TaskService, InvalidTaskError
from repositories.task_repository import task_repository
from repositories.category_repository import category_repository
from initialize_database import initialize_database

class TestTaskService(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.task_repository = task_repository
        self.category_repository = category_repository
        self.task_service = TaskService(task_repository, category_repository)

        self.task_1 = Task(title="Write some unit tests", date="4.4.2040", category="Studies")
        self.task_2 = Task(title="Refactor your code", date="5.5.2035", category=None)
        self.task_3 = Task(title="Update unit tests", date="6.6.2060", category="Studies")

    def create_test_task(self, task):
        self.task_service.create_task(task.title, task.date, task.category)

    def create_test_category(self):
        self.task_service.create_category("Studies")

    def test_create_task_without_category(self):
        self.task_1.category = None
        self.create_test_task(self.task_1)
        tasks = self.task_service.get_tasks(completion_status=False)
        categories = self.task_service.get_categories()

        self.assertEqual(tasks[1].title, "Write some unit tests")
        self.assertEqual(tasks[1].date, "4.4.2040")
        self.assertFalse(tasks[1].completed)
        self.assertIsNone(tasks[1].category)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(len(categories), 0)
        self.assertEqual(categories, [])

    def test_create_task_with_category(self):
        self.create_test_task(self.task_1)
        tasks = self.task_service.get_tasks(completion_status=False)
        categories = self.task_service.get_categories()

        self.assertEqual(categories, ['Studies'])
        self.assertEqual(self.task_service.get_categories_with_id(), {1: 'Studies'})
        self.assertEqual(tasks[1].title, "Write some unit tests")
        self.assertEqual(tasks[1].date, "4.4.2040")
        self.assertFalse(tasks[1].completed)
        self.assertEqual(tasks[1].category, "Studies")
        self.assertEqual(len(tasks), 1)

    def test_create_task_with_maximum_task_title_length(self):
        self.task_service.create_task(title=f"{100*"n"}", date="22.03.2027", category=None)

        self.assertEqual(len(self.task_service.get_tasks(False)), 1)

        self.task_service.create_task(title=f"{10*"n"}", date="22.03.2027", category="Studies")

        self.assertEqual(len(self.task_service.get_tasks(False)), 2)

    def test_create_task_with_empty_task_title_entry(self):
        with self.assertRaises(InvalidTaskError):
            self.task_service.create_task(title="", date="22.03.2027", category=None)

        self.assertEqual(len(self.task_service.get_tasks(False)), 0)
        self.assertEqual(len(self.task_service.get_tasks(True)), 0)

        with self.assertRaises(InvalidTaskError):
            self.task_service.create_task(title="", date="22.03.2027", category="Studies")

        self.assertEqual(len(self.task_service.get_tasks(False)), 0)
        self.assertEqual(len(self.task_service.get_tasks(True)), 0)

    def test_create_task_with_too_long_task_title(self):
        with self.assertRaises(InvalidTaskError):
            self.task_service.create_task(title=f"{101*"n"}", date="22.03.2027", category=None)

        self.assertEqual(len(self.task_service.get_tasks(False)), 0)

        with self.assertRaises(InvalidTaskError):
            self.task_service.create_task(title=f"{101*"n"}", date="22.03.2027", category="Studies")

        self.assertEqual(len(self.task_service.get_tasks(False)), 0)
        self.assertEqual(len(self.task_service.get_tasks(True)), 0)

    def test_create_task_with_current_date(self):
        current_date = date.today()
        self.task_1.date = current_date.strftime("%d.%m.%Y")

        self.create_test_task(self.task_1)

        tasks = self.task_service.get_tasks(completion_status=False)

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[1].title, "Write some unit tests")
        self.assertEqual(tasks[1].date, self.task_1.date)
        self.assertFalse(tasks[1].completed)
        self.assertEqual(tasks[1].category, "Studies")

    def test_create_task_with_yesterday(self):
        yesterday = date.today() - timedelta(days=1)
        self.task_1.date = yesterday.strftime("%d.%m.%Y")

        with self.assertRaises(InvalidTaskError):
            self.task_service.create_task(self.task_1.title, self.task_1.date, self.task_1.category)

    def test_create_task_with_empty_task_date_entry(self):
        with self.assertRaises(InvalidTaskError):
            self.task_service.create_task(title="Code", date="", category=None)

        self.assertEqual(len(self.task_service.get_tasks(False)), 0)

    def test_create_task_with_passed_task_date_entry(self):
        with self.assertRaises(InvalidTaskError):
            self.task_service.create_task(title="Code", date="12.2.2000", category=None)

        self.assertEqual(len(self.task_service.get_tasks(False)), 0)

        with self.assertRaises(InvalidTaskError):
            self.task_service.create_task(title="Code", date="12.2.2000", category="Studies")

        self.assertEqual(len(self.task_service.get_tasks(False)), 0)

    def test_create_task_with_invalid_task_date_entry(self):
        with self.assertRaises(InvalidTaskError):
            self.task_service.create_task(title="Code",
                                          date="This is not date in form dd.mm.yyyy",
                                          category=None)

        self.assertEqual(len(self.task_service.get_tasks(False)), 0)

        with self.assertRaises(InvalidTaskError):
            self.task_service.create_task(title="Code",
                                          date="This is not date in form dd.mm.yyyy",
                                          category="Studies")

        self.assertEqual(len(self.task_service.get_tasks(False)), 0)

    def test_get_uncompleted_tasks(self):
        self.create_test_task(self.task_1)
        self.create_test_task(self.task_2)
        self.task_service.set_completed(2)
        uncompleted_tasks = self.task_service.get_tasks(completion_status=False)

        self.assertEqual(uncompleted_tasks[1].title, "Write some unit tests")
        self.assertEqual(uncompleted_tasks[1].date, "4.4.2040")
        self.assertFalse(uncompleted_tasks[1].completed)
        self.assertEqual(uncompleted_tasks[1].category, "Studies")
        self.assertEqual(len(uncompleted_tasks), 1)

    def test_get_completed_tasks(self):
        self.create_test_task(self.task_1)
        self.create_test_task(self.task_2)
        self.task_service.set_completed(2)
        completed_tasks = self.task_service.get_tasks(completion_status=True)

        self.assertEqual(completed_tasks[2].title, "Refactor your code")
        self.assertEqual(completed_tasks[2].date, "5.5.2035")
        self.assertTrue(completed_tasks[2].completed)
        self.assertIsNone(completed_tasks[2].category)
        self.assertEqual(len(completed_tasks), 1)

    def test_delete_task(self):
        self.create_test_task(self.task_1)

        self.assertEqual(len(self.task_service.get_tasks(False)), 1)

        self.task_service.delete_task(1)

        self.assertEqual(len(self.task_service.get_tasks(False)), 0)

    def test_set_completed(self):
        self.create_test_task(self.task_1)
        self.task_service.set_completed(1)
        tasks = self.task_service.get_tasks(completion_status=True)

        self.assertTrue(tasks[1].completed)
        self.assertEqual(len(tasks), 1)

    def test_set_uncompleted(self):
        self.create_test_task(self.task_1)
        self.task_service.set_completed(1)
        self.task_service.set_uncompleted(1)

        tasks = self.task_service.get_tasks(completion_status=False)

        self.assertEqual(tasks[1].title, "Write some unit tests")
        self.assertEqual(tasks[1].date, "4.4.2040")
        self.assertEqual(tasks[1].category, "Studies")
        self.assertFalse(tasks[1].completed)
        self.assertEqual(len(tasks), 1)

    def test_get_categories_with_id(self):
        self.create_test_task(self.task_1)
        result = self.task_service.get_categories_with_id()

        self.assertEqual(result, {1: 'Studies'})

    def test_get_categories(self):
        self.create_test_task(self.task_1)
        categories = self.task_service.get_categories()

        self.assertEqual(categories, ['Studies'])

    def test_create_category_with_existing_category(self):
        self.create_test_category()
        categories = self.task_service.get_categories()
        self.assertEqual(len(categories), 1)

        self.task_service.create_category("Studies")
        categories = self.task_service.get_categories()

        self.assertEqual(len(categories), 1)

    def test_create_category_with_non_existing_category(self):
        self.create_test_category()
        categories = self.task_service.get_categories()

        self.assertEqual(len(categories), 1)

        self.task_service.create_category("Work")
        categories = self.task_service.get_categories()

        self.assertEqual(len(categories), 2)

    def test_delete_category(self):
        self.create_test_category()
        self.task_service.delete_category(self.task_1.category)
        categories = self.task_service.get_categories()

        self.assertEqual(len(categories), 0)
        self.assertEqual(categories, [])

    def test_delete_category_deletes_the_category_from_tasks(self):
        self.create_test_task(self.task_1)
        self.create_test_category()
        self.task_service.delete_category(self.task_1.category)
        tasks = self.task_service.get_tasks(False)

        self.assertEqual(tasks[1].title, "Write some unit tests")
        self.assertEqual(tasks[1].date, "4.4.2040")
        self.assertIsNone(tasks[1].category)
