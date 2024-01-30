import tkinter as tk  # Importerer tkinter-biblioteket for GUI
from PIL import Image, ImageTk  # Importerer moduler for bildebehandling

class Button:
    def __init__(self, root, settings, command_config=None, command=None, clicked=False):
        self.clicked = clicked
        self.button = tk.Button(root, **settings, command=self.click)
        self.command_config = command_config
        self.settings = settings
        self.command = command
    
    def click(self):
        self.clicked = True if self.clicked == False else False
        if self.clicked and self.command_config != None:
            self.button.config(**self.command_config)
        else:
            self.button.config(**self.settings)
        if self.command:
            self.command()
    


prevpage = []  # En liste for å lagre tidligere visningskomponenter


# Funksjon for å fjerne alle komponenter unntatt de som er spesifikt angitt i 'page'
def clear_window(root, page=[]):
    for widget in root.winfo_children():
        if widget not in page and widget not in savedWidgets and widget not in prevpage:
            widget.destroy()


# Funksjon for å lagre nåværende visningskomponenter
def keep_page(root):
    page = []
    for widget in root.winfo_children():
        if widget.winfo_ismapped() and widget not in savedWidgets:
            page.append(widget)
            widget.forget()
    return page


# Funksjon for å laste inn tidligere visningskomponenter i 'page'
def load_page(root, page):
    if page is not None:
        clear_window(root, page=page)
        for widget in page:
            widget.pack()


savedWidgets = []  # En liste for å lagre tidligere opprettede komponenter


# Funksjon for å lagre en enkelt widget i 'savedWidgets'
def save_widget(widget):
    global savedWidgets
    savedWidgets.append(widget)
