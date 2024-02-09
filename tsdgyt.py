import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_graph():
    # Create some sample data
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 6]

    # Create a Matplotlib figure and axis
    fig, ax = plt.subplots()

    # Plot the data
    ax.plot(x, y, marker='o', color='b')

    # Set labels and title
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_title('Sample Plot')

    # Create a canvas widget
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=1, column=0, columnspan=2, pady=10, padx=10)


# Create the main Tkinter window
root = tk.Tk()
root.title("Matplotlib Plot in Tkinter")

# Create a button to plot the graph
plot_button = ttk.Button(root, text="Plot Graph", command=plot_graph)
plot_button.grid(row=0, column=0, pady=10, padx=10)

# Create a button to quit the application
quit_button = ttk.Button(root, text="Quit", command=root.quit)
quit_button.grid(row=0, column=1, pady=10, padx=10)

# Run the Tkinter event loop
root.mainloop()
