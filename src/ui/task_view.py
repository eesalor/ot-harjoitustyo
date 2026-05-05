from datetime import datetime, timedelta
from tkinter import ttk, constants
from tkinter import *
import tkinter as tk
from services.task_service import task_service, InvalidTaskError

class TaskView:
    """Luokka, joka vastaa sovelluksen tehtävänäkymästä."""

    def __init__(self, root, update_task_view):
        """Luokan konstruktori, joka luo uuden tehtävänäkymän.

        Args:
            root:
                TKinterin Tk-luokasta muodostettu käyttöliittymän juurikomponentti, johon
                käyttöliittymän komponentit alustetaan.
            update_task_view:
                Kutsuttava-arvo, jota kutsutaan, kun käyttäjä luo uuden tehtävän, merkitsee
                tehtävän tehdyksi tai tekemättömäksi, poistaa tehtävän tai kategorian.
        """

        self._root = root
        self._frame = None
        self._update_task_view = update_task_view

        self._task_title_entry = None
        self._task_date_entry = None
        self._task_category_combobox = None

        self._all_categories = None

        self._selected_category = None
        self._selected_uncompleted_task_id = None
        self._selected_completed_task_id = None

        self._listbox_uncompleted_tasks = None
        self._listbox_completed_tasks = None

        self._listbox_dict_uncompleted_tasks = None
        self._listbox_dict_completed_tasks = None

        self._task_error = False
        self._task_error_label = None
        self._task_error_label_var = None

        self._date_error = False
        self._date_error_label = None
        self._date_error_label_var = None

        self._initialize()
    
    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa kaikki näkymän komponentit."""
        self._frame.destroy()

    def _initialize_task_field(self):
        task_title_label = ttk.Label(master=self._frame, text="Task*")

        self._task_title_entry = ttk.Entry(master=self._frame)

        task_title_label.grid(
            row=1,
            column=1,
            columnspan=2,
            padx=5,
            pady=5
            )

        self._task_title_entry.grid(
            row=2,
            column=1,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

    def _initialize_date_field(self):
        task_date_label = ttk.Label(master=self._frame, text="Date (dd.mm.yyyy)*")

        self._task_date_entry = ttk.Entry(master=self._frame)

        task_date_label.grid(
            row=1,
            column=3,
            columnspan=2,
            padx=5,
            pady=5
            )

        self._task_date_entry.grid(
            row=2,
            column=3,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

        create_button = ttk.Button(
            master=self._frame,
            text="Create task",
            command=self._handle_create_button_click
            )

        create_button.grid(
            row=2,
            column=11,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

    def _initialize_category_combobox(self):
        category_label = ttk.Label(master=self._frame, text="Enter or select category:")
        category_label.grid(row=1, column=8, padx=5, pady=5)

        self._task_category_combobox = ttk.Combobox(
            master=self._frame,
            width=20,
            )

        categories = task_service.get_categories()

        self._task_category_combobox['values'] = categories

        self._task_category_combobox.bind('<<ComboboxSelected>>', self._select_category)

        self._task_category_combobox.grid(
            row=2,
            column=8,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

        delete_category_button = ttk.Button(
            master=self._frame,
            text="Delete selected category",
            command=self._handle_delete_category_button_click
            )

        delete_category_button.grid(
            row=3,
            column=11,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
        )

    def _select_category(self, event):
        self._selected_category = event.widget.get()
        return

    def _show_errors(self):
        self._task_error_label_var = StringVar(self._frame)
        self._task_error_label = tk.Label(master=self._frame, textvariable=self._task_error_label_var, fg="red")
        self._task_error_label.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        self._date_error_label_var = StringVar(self._frame)
        self._date_error_label = tk.Label(master=self._frame, textvariable=self._date_error_label_var, fg="red")
        self._date_error_label.grid(row=3, column=3, columnspan=2, padx=5, pady=5)

    def _generate_task_title_error(self, title_entry):
        if len(title_entry) == 0:
            self._task_error = True
            self._task_error_label_var.set("Please enter a task")
            return

        elif len(title_entry) > 100:
            self._task_error = True
            self._task_error_label_var.set("Maximum length is 100 characters")
            return

        self._task_error = False
        self._task_error_label_var.set("")
        return

    def _generate_task_date_error(self, date_entry):
        try:
            validated_date_entry = datetime.strptime(date_entry,  "%d.%m.%Y")
        except:
            self._date_error = True
            self._date_error_label_var.set("The date not in form dd.mm.yyyy")
            return

        if validated_date_entry < datetime.now() - timedelta(days=1):
            self._date_error = True
            self._date_error_label_var.set("The date has already passed")
            return

        self._date_error = False
        self._date_error_label_var.set("")
        return

    def _handle_create_button_click(self):
        title = self._task_title_entry.get()
        date = self._task_date_entry.get()
        category = self._task_category_combobox.get()

        self._all_categories = task_service.get_categories()

        try:
            task_service.create_task(title, date, category)

        except InvalidTaskError:
            self._generate_task_title_error(title)
            self._generate_task_date_error(date)

            if self._task_error or self._date_error:
                return

        self._update_task_view()

    def _handle_delete_category_button_click(self):
        if not self._selected_category:
            return

        category = self._task_category_combobox.get()

        task_service.delete_category(category)

        self._update_task_view()

    def _initialize_uncompleted_task_listbox(self):
        label = ttk.Label(master=self._frame, text="Uncompleted tasks:")
        label.grid(row=7, column=1, columnspan=2, padx=5, pady=5)

        self._listbox = Listbox(master=self._frame, width=80, height=20)

        self._listbox.grid(row=8, column=1, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._uncompleted_tasks = task_service.get_tasks(completion_status=False)

        self._listbox_dict_uncompleted_tasks = {}

        n = 0
        if len(self._uncompleted_tasks) != 0:
            for row in self._uncompleted_tasks.items():
                self._listbox_dict_uncompleted_tasks[n] = row
                if row[1].category is None:
                    task = f"{row[1].date:15} {row[1].title} {5*" "} (No category)"
                else:
                    task = (f"{row[1].date:15} {row[1].title} {5*" "} {row[1].category}")
                self._listbox.insert(tk.END, task)
                n += 1

            self._listbox.bind('<<ListboxSelect>>', self._select_uncompleted_task)

        set_completed_button = ttk.Button(
            master=self._frame,
            text="Set completed",
            command=self._handle_set_completed_button_click
            )

        set_completed_button.grid(
            row=9,
            column=1,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5)

        delete_uncompleted_button = ttk.Button(
            master=self._frame,
            text="Delete selected task",
            command=self._handle_delete_uncompleted_button_click
            )

        delete_uncompleted_button.grid(
            row=10,
            column=1,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

    def _initialize_completed_task_listbox(self):
        label = ttk.Label(master=self._frame, text="Completed tasks:")
        label.grid(row=7, column=3, columnspan=2, padx=5, pady=5)

        self._listbox_completed_tasks = Listbox(master=self._frame, width=80,height=20)

        self._listbox_completed_tasks.grid(row=8, column=3, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._completed_tasks = task_service.get_tasks(completion_status=True)

        self._listbox_dict_completed_tasks = {}

        n = 0
        if len(self._completed_tasks) != 0:
            for row in self._completed_tasks.items():
                self._listbox_dict_completed_tasks[n] = row
                if row[1].category is None:
                    task = f"{row[1].date:15} {row[1].title} {5*" "} (No category)"
                else:
                    task = (f"{row[1].date:15} {row[1].title} {5*" "} {row[1].category}")
                self._listbox_completed_tasks.insert(tk.END, task)
                n += 1

            self._listbox_completed_tasks.bind('<<ListboxSelect>>', self._select_completed_task)

        set_uncompleted_button = ttk.Button(
            master=self._frame,
            text="Set uncompleted",
            command=self._handle_set_uncompleted_button_click
            )

        set_uncompleted_button.grid(
            row=9,
            column=3,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5)

        delete_completed_button = ttk.Button(
            master=self._frame,
            text="Delete selected task",
            command=self._handle_delete_completed_button_click
            )

        delete_completed_button.grid(
            row=10,
            column=3,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

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

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        create_label= ttk.Label(master=self._frame, text="Create a new task", font=("Arial", 12,"bold"))
        create_label.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

        self._initialize_task_field()

        self._initialize_date_field()

        self._initialize_category_combobox()

        self._show_errors()

        label = ttk.Label(master=self._frame, text="Your tasks", font=("Arial", 12,"bold"))
        label.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

        self._initialize_uncompleted_task_listbox()

        self._initialize_completed_task_listbox()

        self._root.grid_columnconfigure(1, weight=1)
        self._root.grid_columnconfigure(2, weight=1)
