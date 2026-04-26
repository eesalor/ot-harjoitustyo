from entities.task import Task
from database_connection import get_database_connection

class TaskRepository:
    """Luokka, joka vastaa tehtäviin liittyvistä tietokantaoperaatioista."""

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: SQL-tietokantayhteyttä edustava Connection-olio.
        """

        self._connection = connection

    def create_task(self, task: Task, category_id):
        """Tallentaa uuden tehtävän tietokantaan.

        Args:
            task: Task-oliomuodossa oleva tehtävä, joka tallennetaan tietokantaan.
            category_id: Tehtävään liittyvän kategorian id, joka tallennetaan tietokantaan.
        """

        cursor = self._connection.cursor()

        cursor.execute("""INSERT INTO Tasks (title, date, category_id, completed)
                    VALUES (?, ?, ?, 0)""",
                       [task.title, task.date, category_id])

        self._connection.commit()

    def get_all_tasks(self):
        """Palauttaa kaikki tehtävät.

        Returns:
            Palauttaa kaikki tehtävät sanakirjana, jossa avaimena on tehtävän id ja
            arvona tehtävät Task-oliomuodossa.
        """

        cursor = self._connection.cursor()
        tasks = cursor.execute("SELECT id, title, date, completed FROM Tasks").fetchall()
        all_tasks = {}

        for row in tasks:
            task_id = row[0]
            task = Task(row[1], row[2])
            completed = row[3]
            if completed == 1:
                task.completed = True
            all_tasks[task_id] = str(task)

        return all_tasks

    def get_all_tasks_as_objects(self):
        """Palauttaa kaikki tehtävät.

        Returns:
            Palauttaa kaikki tehtävät sanakirjana, jossa avaimena on tehtävän id ja
            arvona tehtävät Task-oliomuodossa.
        """

        cursor = self._connection.cursor()
        tasks = cursor.execute("""SELECT id, title, date, completed, category_id
                               FROM Tasks""").fetchall()
        all_task_objects = {}

        for row in tasks:
            task_id = row[0]
            task = Task(row[1], row[2])
            completed = row[3]
            if completed == 1:
                task.completed = True
            task.category = row[4]

            all_task_objects[task_id] = task

        return all_task_objects

    def get_tasks_with_categories(self, categories):
        """Palauttaa kaikki tehtävät.

        Args:
            categories: Kategoriat ja niiden id:t sanakirjana, jossa avaimena on kategorian id
            ja arvona Category-olion merkkijonoesitys.

        Returns:
            Palauttaa kaikki tehtävät sanakirjana, jossa avaimena on tehtävän id ja
            arvona tehtävät Task-olion merkkijonoesityksinä.
        """

        cursor = self._connection.cursor()
        tasks = cursor.execute("""SELECT id, title, date, completed, category_id
                               FROM Tasks""").fetchall()

        all_task_objects = {}

        for row in tasks:
            task_id = row[0]
            task = Task(row[1], row[2])
            completed = row[3]

            if completed == 1:
                task.completed = True

            category_id = row[4]
            if category_id:
                task.category = categories[category_id]

            all_task_objects[task_id] = str(task)

        return all_task_objects

    def get_uncompleted_tasks_with_categories(self, categories):
        """Palauttaa kaikki tekemättömät tehtävät.

        Args:
            categories: Kategoriat ja niiden id:t sanakirjana, jossa avaimena on kategorian id
            ja arvona Category-olion merkkijonoesitys.

        Returns:
            Palauttaa kaikki tekemättömät tehtävät sanakirjana, jossa avaimena on tehtävän id ja
            arvona tehtävät Task-olion merkkijonoesityksinä.
        """

        cursor = self._connection.cursor()
        tasks = cursor.execute("""SELECT id, title, date, completed, category_id FROM Tasks
                               WHERE completed = 0""").fetchall()

        uncompleted_task_objects = {}

        for row in tasks:
            task_id = row[0]
            task = Task(row[1], row[2])
            task.completed = False
            category_id = row[4]
            if category_id:
                task.category = categories[category_id]

            uncompleted_task_objects[task_id] = str(task)

        return uncompleted_task_objects

    def get_completed_tasks_with_categories(self, categories):
        """Palauttaa kaikki tehdyt tehtävät.

        Args:
            categories: Kategoriat ja niiden id:t sanakirjana, jossa avaimena on kategorian id
            ja arvona Category-olion merkkijonoesitys.

        Returns:
            Palauttaa kaikki tehdyt tehtävät sanakirjana, jossa avaimena on tehtävän id ja
            arvona tehtävät Task-olion merkkijonoesityksinä.
        """

        cursor = self._connection.cursor()
        tasks = cursor.execute("""SELECT id, title, date, completed, category_id FROM Tasks
                               WHERE completed = 1""").fetchall()

        completed_task_objects = {}

        for row in tasks:
            task_id = row[0]
            task = Task(row[1], row[2])
            task.completed = True
            category_id = row[4]
            if category_id:
                task.category = categories[category_id]

            completed_task_objects[task_id] = str(task)

        return completed_task_objects

    def get_uncompleted_tasks(self):
        """Palauttaa kaikki tekemättömät tehtävät ilman kategoriaa.

        Returns:
            Palauttaa kaikki tekemättömät tehtävät sanakirjana, jossa avaimena on tehtävän id ja
            arvona tehtävät Task-olion merkkijonoesityksinä.
        """
        cursor = self._connection.cursor()

        tasks = cursor.execute("SELECT id, title, date, completed FROM Tasks").fetchall()

        all_uncompleted_tasks = {}

        for row in tasks:
            task_id = row[0]
            task = Task(row[1], row[2])
            completed = row[3]
            if completed == 0:
                all_uncompleted_tasks[task_id] = repr(task)

        return all_uncompleted_tasks

    def get_completed_tasks(self):
        """Palauttaa kaikki tekemättömät tehtävät ilman kategoriaa.

        Returns:
            Palauttaa kaikki tekemättömät tehtävät sanakirjana, jossa avaimena on tehtävän id ja
            arvona tehtävät Task-olion merkkijonoesityksinä.
        """

        cursor = self._connection.cursor()

        tasks = cursor.execute("SELECT id, title, date, completed FROM Tasks").fetchall()

        all_completed_tasks = {}

        for row in tasks:
            task_id = row[0]
            task = Task(row[1], row[2])
            completed = row[3]
            if completed == 1:
                all_completed_tasks[task_id] = repr(task)

        return all_completed_tasks

    def delete_task(self, task_id):
        """Poistaa tehtävän tietokannasta.

        Args:
            task_id: Poistettavan tehtävän id.
        """

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Tasks WHERE id = ?", [task_id])

        self._connection.commit()

    def set_completed(self, task_id):
        """Asettaa tehtävän tilan tehdyksi.

        Args:
            task_id: Tehtävän id, jonka perusteella tehtävä tila päivitetään tehdyksi.
        """

        cursor = self._connection.cursor()

        cursor.execute("UPDATE Tasks SET completed = 1 WHERE id = ?",
                        [task_id])

        self._connection.commit()

    def set_uncompleted(self, task_id):
        """Asettaa tehtävän tilan tehdyksi.

        Args:
            task_id: Tehtävän id, jonka perusteella tehtävä tila päivitetään tekemättömäksi.
        """

        cursor = self._connection.cursor()

        cursor.execute("UPDATE Tasks SET completed = 0 WHERE id = ?",
                        [task_id])

        self._connection.commit()

    def delete_category_from_task(self, category_id):
        """Poistaa tehtäviin liitetyn kategorian tietokannasta.

        Args:
            category_id: Poistettavan kategorian id, joka poistetaan tietokannassa
            olevista tehtävistä.
        """

        cursor = self._connection.cursor()

        cursor.execute("""UPDATE Tasks SET category_id = ?
                       WHERE category_id = ?""", [None, category_id])

        self._connection.commit()

task_repository = TaskRepository(get_database_connection())
