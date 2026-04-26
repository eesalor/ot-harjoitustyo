class Task:
    """Luokka, joka määrittelee tehtävän.

    Attributes:
        title: Merkkijonoarvo, joka kuvaa tehtävän nimeä.
        date: Merkkijonoarvo, joka kuvaa tehtävän määräaikaa.
        completed: Boolen-arvo, joka kuvaa, onko tehtävä tehty vai ei.
        category: Merkkijonoarvo, joka kuvaa tehtävän aihekategoriaa.
    """

    def __init__(self, title, date, completed=False, category=None):
        """Luokan konstruktori, joka luo uuden tehtävän.

        Args:
            title: Merkkijonoarvo, joka kuvaa tehtävän nimeä.
            date: Merkkijonoarvo, joka kuvaa tehtävän määräaikaa.
            completed:
                Oletusarvoltaan False.
                Boolen-arvo, joka kuvaa, onko tehtävä tehty vai ei.
            category:
                Oletusarvoltaan None.
                Merkkijonoarvo, joka kuvaa tehtävän aihekategoriaa.
        """

        self.title = title
        self.date = date
        self.completed = completed
        self.category = category

    def __str__(self):
        if self.completed is False:
            if not self.category:
                return f"{self.date:15} {self.title:30} (No category)"

            return f"{self.date:15} {self.title:30} {self.category}"

        if not self.category:
            return f"{self.date:15} {self.title:30} (No category)"

        return f"{self.date:15} {self.title:30} {self.category}"

    def __repr__(self):
        return f"({self.title}, {self.date}, {self.category}, {self.completed})"
