import tkinter as tk
from components import frames

# * -- Starting Resolution -- * #
WIDTH = 1280
HEIGHT = 800


def main():
    # Initialize main window
    root = tk.Tk()
    root.title("Crude OCR")
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.config(bg="white")

    frames.initialize(root)

    # Starts the window
    root.mainloop()


if __name__ == "__main__":
    main()
