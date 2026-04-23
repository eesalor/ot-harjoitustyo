from entities.category import Category
from database_connection import get_database_connection

class CategoryRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_category(self, category: Category):
        cursor = self._connection.cursor()
        print(category.title)

        cursor.execute("INSERT INTO Categories (title) VALUES (?)",
                       [category.title])

        self._connection.commit()

    def get_categories_with_id(self):
        cursor = self._connection.cursor()

        categories = cursor.execute("SELECT id, title FROM Categories").fetchall()

        all_categories = {}

        for row in categories:
            category_id = row[0]
            category = Category(row[1])
            all_categories[category_id] = str(category)

        return all_categories

    def get_categories(self):
        cursor = self._connection.cursor()

        categories = cursor.execute("SELECT title FROM Categories").fetchall()

        all_categories = []

        for row in categories:
            category = Category(row[0])
            all_categories.append(str(category))

        return all_categories

    def get_category_id(self, category):
        cursor = self._connection.cursor()

        result = cursor.execute("SELECT id FROM Categories WHERE title = ?", [category]).fetchall()
        for row in result:
            category_id = row[0]

        return category_id

    def find_category_by_name(self, category):
        cursor = self._connection.cursor()

        result = cursor.execute("""SELECT title FROM Categories
                                WHERE title = ?""", [category]).fetchone()

        if result:
            return True

        return False

    def delete_category(self, category_id):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Categories WHERE id = ?", [category_id])

        self._connection.commit()

category_repository = CategoryRepository(get_database_connection())
