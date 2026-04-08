from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Title")
    window.minsize(400, 400)

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
