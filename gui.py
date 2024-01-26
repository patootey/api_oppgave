import tkinter as tk
import general as ge


r = tk.Tk()  # Oppretter et hovedvindu (root) for GUI-en
r.title("currency")  # Setter tittelen på vinduet
r.geometry("400x300")  # Setter størrelsen på vinduet til 400x300 piksler

class Button:
    def __init__(self):
        self.clicked = False
        self.button


def main(root):
    ge.clear_window(root)  # Kaller en funksjon for å fjerne alle widgets fra vinduet
    button1 = tk.Button(root, text="Søk w/ Land", command=button_click).grid(row=1,column=1)
    root.mainloop()  # Starter GUI-hovedløkka for å vise vinduet

main(r)