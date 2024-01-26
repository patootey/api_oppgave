import tkinter as tk
import general as ge


r = tk.Tk()  # Oppretter et hovedvindu (root) for GUI-en
r.title("currency")  # Setter tittelen på vinduet
r.geometry("400x300")  # Setter størrelsen på vinduet til 400x300 piksler




def main(root):
    ge.clear_window(root)  # Kaller en funksjon for å fjerne alle widgets fra vinduet
    button1 = ge.Button(root, {"text":"Søk med Land" , "bg":"white"}, command_config=({"bg":"green"}))
    button1.button.grid(row=1, column=1)
    root.mainloop()  # Starter GUI-hovedløkka for å vise vinduet

main(r)