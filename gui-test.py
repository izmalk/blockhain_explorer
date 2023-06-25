import tkinter as tk
from tkinter import ttk


def button_clicked():
    print("Button clicked!")


# Create the main window
window = tk.Tk()
window.title("GUI Example")
window.geometry("400x300")

# Create a tab control
tab_control = ttk.Notebook(window)

# Create the first tab
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Tab 1")

# Create a button in the first tab
button = ttk.Button(tab1, text="Click Me", command=button_clicked)
button.pack(pady=10)

# Create the second tab
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Tab 2")

# Create a canvas in the second tab
canvas = tk.Canvas(tab2, width=300, height=200, bg="white")
canvas.pack(pady=10)

# Add items to the canvas (e.g., a rectangle)
canvas.create_rectangle(50, 50, 250, 150, fill="blue")

# Pack the tab control to make it visible
tab_control.pack(expand=1, fill="both")

# Start the GUI event loop
window.mainloop()
