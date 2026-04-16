from tkinter import ttk, constants
from tkinter import *
import tkinter as tk
from services.task_service import task_service

class TaskView:
    def __init__(self, root, update_task_view):
        self._root = root
        self._frame = None
        self._update_task_view = update_task_view
        self._task_title = None
        self._task_date = None
        self._all_tasks = None
        self._listbox = None
        self._listbox_dictionary = None
        self._selected_task_id = None

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._show_task_list()
    
    def _show_task_list(self):

        create_label= ttk.Label(master=self._frame, text="Create new task")
        task_title_label = ttk.Label(master=self._frame, text="Task")
        task_date_label = ttk.Label(master=self._frame, text="Date")

        self._task_title = ttk.Entry(master=self._frame)
        self._task_date = ttk.Entry(master=self._frame)
        
        button = ttk.Button(master=self._frame, text="Create", command=self._handle_create_button_click)

        create_label.grid(padx=5, pady=5)
        task_title_label.grid(row=0, column=1,padx=5, pady=5)
        task_date_label.grid(row=0, column=2, padx=5, pady=5)

        self._task_title.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._task_date.grid(row=1, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        
        button.grid(row=1, column=3, sticky=(constants.E, constants.W))
        self._all_tasks = self._get_all_tasks()
        
        label = ttk.Label(master=self._frame, text="Task list:")
        label.grid(padx=5, pady=5)

        self._listbox = Listbox(master=self._frame)

        self._listbox_dictionary = {}

        n = 0
        if len(self._all_tasks) != 0:
            for row in self._all_tasks.items():
                self._listbox_dictionary[n] = row
                self._listbox.insert(tk.END, row[1])
                n += 1

        self._listbox.grid(column=1, sticky=(constants.E, constants.W))
        self._listbox.bind('<<ListboxSelect>>', self._select_task)

        delete_button = ttk.Button(master=self._frame, text="Delete selected task", command=self._handle_delete_button_click)
        delete_button.grid(column=3, sticky=(constants.E, constants.W))

        self._root.grid_columnconfigure(1, weight=1)

    def _handle_create_button_click(self):
        title = self._task_title.get()
        date = self._task_date.get()

        if title:
            task_service.create_task(title, date)

        self._update_task_view()

    def _handle_delete_button_click(self):
        if self._selected_task_id:
            task_service.delete_task(self._selected_task_id)

            self._update_task_view()

    def _get_all_tasks(self):
        all_tasks = task_service.get_all_tasks()
        
        return all_tasks

    def _select_task(self, event):
        index = event.widget.curselection()[0]
        self._selected_task_id = self._listbox_dictionary[index][0]
