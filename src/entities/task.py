class Task:
    def __init__(self, title, date, completed=False):
        self.title = title
        self.date = date
        self.completed = completed

    def __repr__(self):
        if self.completed is False:
            return f"{self.title} {self.date}"

        return f"{self.title} {self.date} (completed)"
