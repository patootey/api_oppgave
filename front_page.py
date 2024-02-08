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
    frame = tk.Frame(root, width=root.winfo_width(), height=root.winfo_height())  # Set a background color and dimensions for visibility
    frame.place(y=50)
    arrow = ge.Photo(root, image_path="./images/arrow.png", size=(40,40),command=lambda: ge.load_page(root,ge.prevpage))
    arrow.label.place(y=0,x=0)

    label1 = tk.Label(frame, text="Søk med Land A")
    label1.grid(row=2, column=1)

    label2 = tk.Label(frame, text="Søk med Land B")
    label2.grid(row=2, column=2)

    label3 = tk.Label(frame, text="Default ting")
    label3.grid(row=2, column=3)

    button1 = ge.Button(frame, {"text":"Søk med Land" , "bg":"white"}, command_config=({"bg":"green"}))
    button1.button.grid(row=1, column=1)
    button2 = ge.Button(frame, {"text":"Søk med valuta" , "bg":"white"}, command_config=({"bg":"green"}), command=lambda: default(button1,button2,label1,label2))
    button2.button.grid(row=1, column=2)
    button1.click()
    button1.command = lambda: default(button2,button1,label1,label2)
    
    name1_entry = tk.Entry(frame)
    name1_entry.grid(row=3, column=1)
    name2_entry = tk.Entry(frame)
    name2_entry.grid(row=3, column=2)
    name3_entry = tk.Entry(frame)
    name3_entry.grid(row=3, column=3)


    search = ge.Button(frame, {"text":"Start Søk"}, command=lambda: rp.results(root,name1_entry.get(), name2_entry.get(), name3_entry.get(), button1.clicked))
    search.button.grid(row=4,column=1)


    error_message = tk.Label(root, fg="red")
    error_message.place(x=70,y=0)
    ge.save_widget(error_message)
    root.mainloop()  # Starter GUI-hovedløkka for å vise vinduet


main(r)
r.mainloop()