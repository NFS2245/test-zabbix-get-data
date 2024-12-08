from tkinter import Tk
from ui_components import build_ui

if __name__ == "__main__":
    root = Tk()
    root.title("Data Processing App")
    build_ui(root)
    root.mainloop()
