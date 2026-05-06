import unittest
from entities.category import Category
from repositories.category_repository import category_repository
from initialize_database import initialize_database

class TestTaskService(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.database = category_repository

        self.category1 = Category("Studies")
        self.database.create_category(self.category1)
        self.category2 = Category("Work")
        self.database.create_category(self.category2)

    def test_create_category(self):
        self.category3 = Category("Home")
        self.database.create_category(self.category3)

        categories = self.database.get_categories()

        self.assertEqual(len(categories), 3)
        self.assertEqual(categories, ['Studies', 'Work', 'Home'])

    def test_get_categories(self):
        categories = self.database.get_categories()

        self.assertEqual(len(categories), 2)
        self.assertEqual(categories, ['Studies', 'Work'])

    def test_get_categories_with_id(self):
        result = self.database.get_categories_with_id()

        self.assertEqual(result, {1: 'Studies', 2: 'Work'})

    def test_get_category_id(self):
        category_id_1 = self.database.get_category_id(self.category1.title)
        category_id_2 = self.database.get_category_id(self.category2.title)

        self.assertEqual(category_id_1, 1)
        self.assertEqual(category_id_2, 2)

    def test_find_category_by_name(self):
        self.assertTrue(self.database.find_category_by_name("Studies"))

        self.assertFalse(self.database.find_category_by_name("Home"))

    def test_delete_category(self):
        category_id = self.database.get_category_id(self.category1.title)

        self.database.delete_category(category_id)

        categories = self.database.get_categories()

        self.assertEqual(categories, ['Work'])

