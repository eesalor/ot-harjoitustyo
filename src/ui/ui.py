from tkinter import ttk, constants
from services.task_service import task_service

class UI:
    def __init__(self, root):
        self._root = root
        self._task_entry = None


    def start(self):

        create_label= ttk.Label(master=self._root, text="Create new task")
        self._task_entry = ttk.Entry(master=self._root)

        button = ttk.Button(master=self._root, text="Create", command=self._handle_button_click)

        create_label.grid(padx=5, pady=5)
        self._task_entry.grid(row=0, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(row=0, column=2, sticky=(constants.E, constants.W))
        
        self._root.grid_columnconfigure(1, weight=1)

    def _handle_button_click(self):
        entry_value = self._task_entry.get()

        task_service.create_task(entry_value)
