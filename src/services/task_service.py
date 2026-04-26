from entities.task import Task
from entities.category import Category
from repositories.task_repository import task_repository
from repositories.category_repository import category_repository

class TaskService:
    """Luokka, joka vastaa sovelluslogiikasta."""

    def __init__(self):
        """Luokan konstruktori, joka muodostaa sovelluslogiikasta huolehtivan palvelun."""

        self._task_repository = task_repository
        self._category_repository = category_repository

    def create_task(self, title, date, category):
        """Luo uuden tehtävän, joka sisältää tehtävän kuvauksen, määräajan ja kategorian.
        Mahdollisesta kategoriasta lisätään id numero.

        Args:
            title: Tehtävän kuvaus merkkijonona.
            date: Tehtävän määräaika merkkijonona.
            category:
               Kategoria merkkijonona. Vapaaehtoinen.
        """

        task = Task(title, date)

        if category:
            category_id = self._category_repository.get_category_id(category)
        else:
            category_id = None

        return self._task_repository.create_task(task, category_id)

    def get_all_tasks(self):
        """Palauttaa kaikki luodut tehtävät.

        Returns:
            Palauttaa kaikki luodut tehtävät sanakirjana,
            jossa avaimena on tehtävän id ja arvona tehtävä Task-oliona.
        """

        return self._task_repository.get_all_tasks_as_objects()

    def get_tasks_with_categories(self):
        """Palauttaa kaikki luodut tehtävät.

        Returns:
            Palauttaa kaikki luodut tehtävät sanakirjana,
            jossa avaimena on tehtävän id ja arvona tehtävä tehtävä Task-oliona.
        """

        categories = self._category_repository.get_categories_with_id()

        return self._task_repository.get_tasks_with_categories(categories)

    def get_uncompleted_tasks_with_categories(self):
        """Palauttaa kaikki tekemättömät tehtävät.

        Returns:
            Palauttaa kaikki tekemättömät tehtävät sanakirjana,
            jossa avaimena on tehtävän id ja arvona tehtävä tehtävä Task-oliona.
        """

        categories = self._category_repository.get_categories_with_id()

        return self._task_repository.get_uncompleted_tasks_with_categories(categories)

    def get_completed_tasks_with_categories(self):
        """Palauttaa kaikki tehdyt tehtävät.

        Returns:
            Palauttaa kaikki tehdyt tehtävät sanakirjana,
            jossa avaimena on tehtävän id ja arvona tehtävä tehtävä Task-oliona.
        """

        categories = self._category_repository.get_categories_with_id()

        return self._task_repository.get_completed_tasks_with_categories(categories)

    def get_uncompleted_tasks(self):
        """Palauttaa kaikki tekemättömät tehtävät ilman kategoriaa.

        Returns:
            Palauttaa kaikki tekemättömät tehtävät sanakirjana,
            jossa avaimena on tehtävän id ja arvona tehtävä tehtävä Task-oliona.
        """

        return self._task_repository.get_uncompleted_tasks()

    def get_completed_tasks(self):
        """Palauttaa kaikki tehdyt tehtävät ilman kategoriaa.

        Returns:
            Palauttaa kaikki tehdyt tehtävät sanakirjana,
            jossa avaimena on tehtävän id ja arvona tehtävä tehtävä Task-oliona.
        """

        return self._task_repository.get_completed_tasks()

    def delete_task(self, task_id):
        """Poistaa tehtävän.

        Args:
            task_id: Poistettavan tehtävän id.
        """

        return self._task_repository.delete_task(task_id)

    def set_completed(self, task_id):
        """Asettaa tehtävän tehdyksi.

        Args:
            task_id: Tehtävän id, jonka perusteella kyseinen tehtävä merkitään tehdyksi.
        """

        return self._task_repository.set_completed(task_id)

    def set_uncompleted(self, task_id):
        """Asettaa tehtävän tekemättömäksi.

        Args:
            task_id: Tehtävän id, jonka perusteella kyseinen tehtävä merkitään tekemättömäksi.
        """

        return self._task_repository.set_uncompleted(task_id)

    def get_categories_with_id(self):
        """Palauttaa kaikki kategoriat.

        Returns:
            Palauttaa kategoriat ja niiden id:t sanakirjana, jossa avaimena on kategorian id
            ja arvona Category-olion merkkijonoesitys.
        """

        return self._category_repository.get_categories_with_id()

    def get_categories(self):
        """Palauttaa kaikki kategoriat listana.

        Returns:
            Palauttaa kaikki kategoriat listana, joka sisältää Category-olioiden
            merkkijonoesityksiä.
        """

        return self._category_repository.get_categories()

    def create_category(self, category):
        """Luo uuden kategorian, jos kategoriaa ei ole vielä olemassa.

        Args:
            category: Kategoria merkkijonona.

        Returns:
            Jos kategoria on jo olemassa, palauttaa kyseisen kategorian.
        """

        existing_category = self._category_repository.find_category_by_name(category)

        if not existing_category:

            category = Category(title=category)

            return self._category_repository.create_category(category)

        return category

    def delete_category(self, category):
        """Poistaa kategorian tehtävistä ja kategorioiden joukosta.

        Args:
            category: Poistettava kategoria merkkijonona"""

        category_id = self._category_repository.get_category_id(category)

        self._task_repository.delete_category_from_task(category_id)

        self._category_repository.delete_category(category_id)

task_service = TaskService()
