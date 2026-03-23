from ui.start_view import StartView
from ui.task_view import TaskView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = StartView(self._root, self._handle_start)

        self._current_view.pack()

    def _handle_start(self):
        self._show_task_view()

    def _show_task_view(self):
        self._hide_current_view()

        self._current_view = TaskView(self._root, self._update_task_view)

        self._current_view.pack()

    def _update_task_view(self):
        self._show_task_view()
