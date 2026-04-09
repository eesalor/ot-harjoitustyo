class Task:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def __str__(self):
        return f"{self.title} {self.date}"

    def __repr__(self):
        return f"{self.title} {self.date}"
