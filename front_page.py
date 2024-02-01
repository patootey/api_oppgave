import tkinter as tk
import general as ge
import result_page as rp


r = tk.Tk()  # Oppretter et hovedvindu (root) for GUI-en
r.title("currency")  # Setter tittelen på vinduet
r.geometry("400x300")  # Setter størrelsen på vinduet til 400x300 piksler


def default(buttonA, buttonB, label1, label2):
    buttonA.button.config(buttonA.settings if buttonA.clicked == True else buttonA.command_config)
    buttonA.clicked = True if buttonA.clicked == False else False
    label1.config(text=str(buttonB.settings["text"])+" A")
    label2.config(text=str(buttonB.settings["text"])+" B")

def main(root):
    ge.clear_window(root)  # Kaller en funksjon for å fjerne alle widgets fra vinduet
    label1 = tk.Label(root, text="Søk med Land A")
    label1.grid(row=2, column=1)

    label2 = tk.Label(root, text="Søk med Land B")
    label2.grid(row=2, column=2)

    button1 = ge.Button(root, {"text":"Søk med Land" , "bg":"white"}, command_config=({"bg":"green"}))
    button1.button.grid(row=1, column=1)
    button2 = ge.Button(root, {"text":"Søk med valuta" , "bg":"white"}, command_config=({"bg":"green"}), command=lambda: default(button1,button2,label1,label2))
    button2.button.grid(row=1, column=2)
    button1.click()
    button1.command = lambda: default(button2,button1,label1,label2)
    
    name1_entry = tk.Entry(root)
    name1_entry.grid(row=3, column=1)
    name2_entry = tk.Entry(root)
    name2_entry.grid(row=3, column=2)

    search = ge.Button(root, {"text":"Start Søk"}, command=lambda: rp.results(root,name1_entry.get(), name2_entry.get(), button1.clicked))
    search.button.grid(row=4,column=1)
    root.mainloop()  # Starter GUI-hovedløkka for å vise vinduet


main(r)
r.mainloop()