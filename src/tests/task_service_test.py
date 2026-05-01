import unittest
from entities.task import Task
from entities.category import Category
from services.task_service import task_service, InvalidTaskError
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

        self.category_repository.create_category(Category(self.category))

    def test_create_task_with_empty_task_title_entry(self):
        with self.assertRaises(InvalidTaskError):
            self.service.create_task(title="", date="22.03.2027", category=None)

    def test_create_task_with_too_long_task_title(self):
        with self.assertRaises(InvalidTaskError):
            self.service.create_task(title=f"{101*"n"}", date="22.03.2027", category=None)

    def test_create_task_with_empty_task_date_entry(self):
        with self.assertRaises(InvalidTaskError):
            self.service.create_task(title="Code", date="", category=None)

    def test_create_task_with_invalid_task_date_entry(self):
        with self.assertRaises(InvalidTaskError):
            self.service.create_task(title="Code", date="12.2.2000", category=None)

        with self.assertRaises(InvalidTaskError):
            self.service.create_task(title="Code", date="not date in form dd.mm.yyyy", category=None)

    def test_create_task_without_category(self):
        category_none = None
        result = self.service.create_task(self.title, self.date, category_none)
        category_id = None

        self.assertEqual(result, self.task_repository.create_task(Task(self.title, self.date), category_id))

    def test_create_task_with_category(self):
        category = self.category
        result = self.service.create_task(self.title, self.date, category)

        self.assertEqual(result, self.task_repository.create_task(Task(self.title, self.date), 1))

    def test_get_uncompleted_tasks(self):
        completion_status = self.completed
        result = self.service.get_tasks(completion_status)
        self.assertEqual(result, self.task_repository.get_uncompleted_tasks())

    def test_get_completed_tasks(self):
        completion_status = True
        result = self.service.get_tasks(completion_status)
        self.assertEqual(result, self.task_repository.get_completed_tasks())

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

    def test_get_categories_with_id(self):
        result = self.service.get_categories_with_id()

        self.assertEqual(result, self.category_repository.get_categories_with_id())

    def test_get_categories(self):
        result = self.service.get_categories()

        self.assertEqual(result, self.category_repository.get_categories())

    def test_create_category_with_existing_category(self):
        category = "Studies"
        self.service.create_category(category)

        categories = self.service.get_categories()

        self.assertEqual(len(categories), 1)

    def test_create_category_with_non_existing_category(self):
        category = "Work"
        self.service.create_category(category)

        categories = self.service.get_categories()

        self.assertEqual(len(categories), 2)

    def test_delete_category(self):
        self.service.delete_category(self.category)

        categories = self.service.get_categories()

        self.assertEqual(len(categories), 0)
