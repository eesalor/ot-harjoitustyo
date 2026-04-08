class Task:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"{self.title}"
