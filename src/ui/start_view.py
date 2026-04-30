from tkinter import ttk, constants

class StartView:
    def __init__(self, root, handle_start):
        self._root = root
        self._handle_start = handle_start
        self._frame = None
    
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        welcome_label = ttk.Label(master=self._frame,
                                  text="Welcome to Manage Your Tasks app!",
                                  font=("Arial", 16,"bold"))

        welcome_label.grid(row=0, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        button = ttk.Button(
            master=self._frame,
            text="Start",
            command=self._handle_start
            )

        button.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
