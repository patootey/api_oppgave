import tkinter as tk  # Importerer tkinter-biblioteket for GUI
from PIL import Image, ImageTk  # Importerer moduler for bildebehandling
import requests
from io import BytesIO

class Button:
    def __init__(self, root, settings, command_config=None, command=None):
        self.clicked = False
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
    
class Photo:
    def __init__(
        self,
        root,
        image_path,
        size=(50, 50),
        command=None,
        button="<Button-1>",
    ):
        self.image_path = image_path  # Filbanen til bildet
        self.size = size  # Størrelsen på bildet
        self.command = command
        self.button = button  # Knappen som brukes til å aktivere klikk-handling
        self.image = None  # Variabel for bildet
        self.label = None  # Variabel for etiketten som viser bildet
        self.create_image(root)  # Oppretter bildet i GUI-en

    def create_image(self, root):
        try:
            photo = Image.open(self.image_path)  # Åpner bildet fra fil
            photo = photo.resize(self.size, Image.ADAPTIVE)  # Justerer størrelsen på bildet
            self.image = ImageTk.PhotoImage(
            photo
            )  # Konverterer bildet til PhotoImage-format
            self.label = tk.Label(root, image=self.image)  # Oppretter en etikett med bildet
        except:
            response = requests.get(self.image_path)
            if response.status_code == 200:
                image_data = response.content
                image = Image.open(BytesIO(image_data))
                photo_image = ImageTk.PhotoImage(image)
                label = tk.Label(root, image=photo_image)
                label.image = photo_image  # Keep a reference to prevent garbage collection
                self.label = label

        if self.command:
            # Binder klikk-handling til bildet hvis en funksjon er angitt
            self.label.bind(self.button, lambda event: self.command())
        
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
            widget.place()


savedWidgets = []  # En liste for å lagre tidligere opprettede komponenter


# Funksjon for å lagre en enkelt widget i 'savedWidgets'
def save_widget(widget):
    global savedWidgets
    savedWidgets.append(widget)
