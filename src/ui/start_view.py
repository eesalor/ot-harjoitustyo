from tkinter import ttk, constants

class StartView:
    """Luokka, joka vastaa sovelluksen aloitusnäkymästä."""

    def __init__(self, root, handle_start):
        """Luokan konstruktori, joka luo uuden aloitusnäkymän.

        Args:
            root:
                TKinterin Tk-luokasta muodostettu käyttöliittymän juurikomponentti, johon
                käyttöliittymän komponentit alustetaan.
            handle_start:
                Kutsuttava-arvo, jota kutsutaan käyttäjän painaessa käyttöliittymän
                aloituspainiketta.
        """

        self._root = root
        self._handle_start = handle_start
        self._frame = None
    
        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa kaikki näkymän komponentit."""
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        welcome_label = ttk.Label(master=self._frame,
                                  text="Welcome to Manage Your Tasks app!",
                                  font=("Arial", 16,"bold"))

        welcome_label.grid(row=0, column=0, sticky=(constants.E, constants.W), padx=700, pady=100)

        button = ttk.Button(
            master=self._frame,
            text="Start",
            command=self._handle_start
            )

        button.grid(row=1, column=0, sticky=(constants.E, constants.W), padx=700, pady=5)

        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)
