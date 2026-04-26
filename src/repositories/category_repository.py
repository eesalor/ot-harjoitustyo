from entities.category import Category
from database_connection import get_database_connection

class CategoryRepository:
    """Luokka, joka vastaa kategroioihin liittyvistä tietokantaoperaatioista."""

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: SQL-tietokantayhteyttä edustava Connection-olio.
        """

        self._connection = connection

    def create_category(self, category: Category):
        """Tallentaa uuden kategorian tietokantaan.

        Args:
            category: Category-oliomuodossa oleva kategoria, joka tallennetaan tietokantaan.
        """

        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO Categories (title) VALUES (?)",
                       [category.title])

        self._connection.commit()

    def get_categories_with_id(self):
        """Palauttaa kategoriat ja niiden id:t.

        Returns:
            Palauttaa kategoriat ja niiden id:t sanakirjana, jossa avaimena on kategorian id
            ja arvona Category-olion merkkijonoesitys.
        """
        cursor = self._connection.cursor()

        categories = cursor.execute("SELECT id, title FROM Categories").fetchall()

        all_categories = {}

        for row in categories:
            category_id = row[0]
            category = Category(row[1])
            all_categories[category_id] = str(category)

        return all_categories

    def get_categories(self):
        """Palauttaa kaikki kategoriat listana.

        Returns:
            Palauttaa kaikki kategoriat listana, joka sisältää Category-olioiden
            merkkijonoesityksiä.
        """

        cursor = self._connection.cursor()

        categories = cursor.execute("SELECT title FROM Categories").fetchall()

        all_categories = []

        for row in categories:
            category = Category(row[0])
            all_categories.append(str(category))

        return all_categories

    def get_category_id(self, category):
        """Palauttaa kategorian id:n, joka haetaan tietokannasta kategorian nimen perusteella.

        Args:
            category: Kategorian nimi merkkijonona.

        Returns:
            Palauttaa kategorian id:n.
        """
        cursor = self._connection.cursor()

        result = cursor.execute("SELECT id FROM Categories WHERE title = ?", [category]).fetchall()
        for row in result:
            category_id = row[0]

        return category_id

    def find_category_by_name(self, category):
        """Etsii, löytyykö tietokannasta kategoriaa nimellä

        Args:
            category: Kategorian nimi merkkijonona.

        Returns:
            Palauttaa True, jos kategoria on tietokannassa.
            Palauttaa False, jos kategoriaa ei ole tietokannassa.
        """

        cursor = self._connection.cursor()

        result = cursor.execute("""SELECT title FROM Categories
                                WHERE title = ?""", [category]).fetchone()

        if result:
            return True

        return False

    def delete_category(self, category_id):
        """Poistaa kategorian tietokannasta.

        Args:
            category_id: Poistettavan tehtävän id, jonka perusteella kategoria poistetaan.
        """

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Categories WHERE id = ?", [category_id])

        self._connection.commit()

category_repository = CategoryRepository(get_database_connection())
