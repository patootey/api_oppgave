import tkinter as tk
import general as ge
import landAPI as la
import requests
from PIL import Image, ImageTk
from io import BytesIO

def results(root, key):
    frame = tk.Frame(root)
    image_url = la.search(key)[3]
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        photo_image = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=photo_image)
        label.image = photo_image  # Keep a reference to prevent garbage collection
        label.place(x=0, y=0)
    frame.place(y=50)
