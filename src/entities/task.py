class Task:
    def __init__(self, title, date, completed=False, category=None):
        self.title = title
        self.date = date
        self.completed = completed
        self.category = category

    def __repr__(self):
        if self.completed is False:
            return f"{self.title} {self.date} {self.category}"

        return f"{self.title} {self.date} (completed)"
