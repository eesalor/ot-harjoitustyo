from tkinter import ttk, constants
from tkinter import *
import tkinter as tk
from services.task_service import task_service

from datetime import datetime, timedelta

class TaskView:
    def __init__(self, root, update_task_view):
        self._root = root
        self._frame = None
        self._update_task_view = update_task_view

        self._task_title_entry = None
        self._task_date_entry = None

        self._selected_uncompleted_task_id = None
        self._selected_completed_task_id = None

        self._listbox_uncompleted_tasks = None
        self._listbox_completed_tasks = None

        self._listbox_dict_uncompleted_tasks = None
        self._listbox_dict_completed_tasks = None

        self._task_error = False
        self._task_error_label = None
        self._task_error_label_var = None
        self._task_error_message = None

        self._date_error = False
        self._date_error_label = None
        self._date_error_label_var = None
        self._date_error_message = None

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_task_creation_form()

        self._show_errors()

        self._initialize_uncompleted_task_listbox()

        self._initialize_completed_task_listbox()

        set_completed_button = ttk.Button(
            master=self._frame,
            text="Set completed",
            command=self._handle_set_completed_button_click
            )

        set_completed_button.grid(
            column=1,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5)

        delete_button = ttk.Button(
            master=self._frame,
            text="Delete selected task",
            command=self._handle_delete_uncompleted_button_click
            )

        delete_button.grid(
            column=1,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

        set_uncompleted_button = ttk.Button(
            master=self._frame,
            text="Set uncompleted",
            command=self._handle_set_uncompleted_button_click
            )

        set_uncompleted_button.grid(
            row=7,
            column=3,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5)

        delete_button = ttk.Button(
            master=self._frame,
            text="Delete selected task",
            command=self._handle_delete_completed_button_click
            )

        delete_button.grid(
            row=8,
            column=3,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

        self._root.grid_columnconfigure(1, weight=1)
        self._root.grid_columnconfigure(2, weight=1)

    def _initialize_task_creation_form(self):
        create_label= ttk.Label(master=self._frame, text="Create new task")

        create_label.grid(row=0, column=0, padx=5, pady=5)

        self._initialize_task_field()

        self._initialize_date_field()

    def _initialize_task_field(self):
        task_title_label = ttk.Label(master=self._frame, text="Task*")

        self._task_title_entry = ttk.Entry(master=self._frame)

        task_title_label.grid(row=0, column=1, padx=5, pady=5)

        self._task_title_entry.grid(
            row=1,
            column=1,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

    def _initialize_date_field(self):
        task_date_label = ttk.Label(master=self._frame, text="Date (dd.mm.yyyy)*")

        self._task_date_entry = ttk.Entry(master=self._frame)

        task_date_label.grid(row=0, column=3, padx=5, pady=5)

        self._task_date_entry.grid(
            row=1,
            column=3,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

        create_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._handle_create_button_click
            )

        create_button.grid(row=1, column=7, sticky=(constants.E, constants.W))

    def _handle_create_button_click(self):
        title = self._task_title_entry.get()
        date = self._task_date_entry.get()

        self._validate_task_title_entry(title)
        self._validate_task_date_entry(date)

        self._task_error_label_var.set(self._task_error_message)

        self._date_error_label_var.set(self._date_error_message)

        if self._task_error or self._date_error:
            return

        task_service.create_task(title, date)

        self._update_task_view()

    def _show_errors(self):
        self._task_error_label_var = StringVar()
        self._task_error_label_var.set("")
        self._task_error_label = tk.Label(master=self._frame, textvariable=self._task_error_label_var, fg="red")
        self._task_error_label.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        self._date_error_label_var = StringVar()
        self._date_error_label_var.set("")
        self._date_error_label = tk.Label(master=self._frame, textvariable=self._date_error_label_var, fg="red")
        self._date_error_label.grid(row=2, column=3, columnspan=2, padx=5, pady=5)

    def _initialize_uncompleted_task_listbox(self):
        label = ttk.Label(master=self._frame, text="Uncompleted tasks:")
        label.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

        self._listbox = Listbox(master=self._frame, width=60)

        self._listbox.grid(column=1, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._uncompleted_tasks = task_service.get_uncompleted_tasks()

        self._listbox_dict_uncompleted_tasks = {}

        n = 0
        if len(self._uncompleted_tasks) != 0:
            for row in self._uncompleted_tasks.items():
                self._listbox_dict_uncompleted_tasks[n] = row
                self._listbox.insert(tk.END, row[1])
                n += 1

            self._listbox.bind('<<ListboxSelect>>', self._select_uncompleted_task)

    def _initialize_completed_task_listbox(self):
        label = ttk.Label(master=self._frame, text="Completed tasks:")
        label.grid(row=5, column=3, columnspan=2, padx=5, pady=5)

        self._listbox_completed_tasks = Listbox(master=self._frame, width=60)

        self._listbox_completed_tasks.grid(row=6, column=3, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._completed_tasks = task_service.get_completed_tasks()

        self._listbox_dict_completed_tasks = {}

        n = 0
        if len(self._completed_tasks) != 0:
            for row in self._completed_tasks.items():
                self._listbox_dict_completed_tasks[n] = row
                self._listbox_completed_tasks.insert(tk.END, row[1])
                n += 1

            self._listbox_completed_tasks.bind('<<ListboxSelect>>', self._select_completed_task)

    def _handle_delete_uncompleted_button_click(self):
        if self._selected_uncompleted_task_id:
            task_service.delete_task(self._selected_uncompleted_task_id)

            self._update_task_view()

    def _handle_delete_completed_button_click(self):
        if self._selected_completed_task_id:
            task_service.delete_task(self._selected_completed_task_id)

            self._update_task_view()

    def _handle_set_completed_button_click(self):
        if self._selected_uncompleted_task_id:
            task_service.set_completed(self._selected_uncompleted_task_id)

            self._update_task_view()

        else:
            return

    def _handle_set_uncompleted_button_click(self):
        if self._selected_completed_task_id:
            task_service.set_uncompleted(self._selected_completed_task_id)

            self._update_task_view()

        else:
            return

    def _select_uncompleted_task(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            self._selected_uncompleted_task_id = self._listbox_dict_uncompleted_tasks[index][0]

    def _select_completed_task(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            self._selected_completed_task_id = self._listbox_dict_completed_tasks[index][0]

    def _validate_task_title_entry(self, entry):
        if len(entry) == 0:
            self._task_error = True
            self._task_error_message = "Please enter a task"
            self._task_error_label_var.set(self._task_error_message)
            return

        elif len(entry) > 100:
            self._task_error = True
            self._task_error_message = "Maximum length is 100 character"
            self._date_error_label_var.set(self._date_error_message)
            return

        self._task_error = False
        self._task_error_message = ""
        self._task_error_label_var.set(self._task_error_message)
        return

    def _validate_task_date_entry(self, entry):
        try:
            validated_date_entry = datetime.strptime(entry,  "%d.%m.%Y")
        except:
            self._date_error = True
            self._date_error_message="The date not in form dd.mm.yyyy"
            return

        if validated_date_entry < datetime.now() - timedelta(days=1):
            self._date_error = True
            self._date_error_message = "The date has already passed"
            return

        self._date_error = False
        self._date_error_message = ""
        self._date_error_label_var.set(self._date_error_message)
        return
