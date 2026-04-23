class Task:
    def __init__(self, title, date, completed=False, category=None):
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
