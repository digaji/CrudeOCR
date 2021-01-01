import tkinter as tk
from components import windows


def main():
    # Initialize main window
    root = tk.Tk()
    root.title("Crude OCR")
    root.geometry("1280x800")
    root.config(bg="white")

    windows.initialize(root)

    # Starts the window
    root.mainloop()


if __name__ == "__main__":
    main()
