import tkinter as tk
from widgets import CYT  # Import CustomYouTubeApp from the widgets.py file

if __name__ == "__main__":
    root = tk.Tk()
    app = CYT(root)  # Initialize the custom YouTube app
    root.mainloop()  # Start the main Tkinter event loop
