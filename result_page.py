import tkinter as tk
import general as ge
import landAPI as la

def results(root, key1, key2, key3, country, start_date, end_date):
    ge.savedWidgets[0].config(text="")
    ge.prevpage = ge.keep_page(root)
    frame = tk.Frame(root, width=root.winfo_width(), height=root.winfo_height()) 
    frame.place(y=50)  
    try:
        data = (la.search(key1), la.search(key2))
        if country:

            for i in range(2):
                name_label = tk.Label(frame, text=data[i-1][0], font=(ge.font, 30, "bold"))
                name_label.grid(row=1, column=1 if i == 1 else 3)
                flag = ge.Photo(frame, image_path=data[i-1][3])
                flag.label.grid(row=2, column=1 if i == 1 else 3)
            

        vs_label = tk.Label(frame, text="VS", font=(ge.font, 30, "bold"))
        vs_label.grid(row=1, column=2)

    
        for i in range(2):
            text = tk.Label(frame, text=f"Name: {data[i-1][0]}\nCode: {data[i-1][1]}\nSymbol: {data[i-1][2]}")
            text.grid(row=3, column= 1 if i == 1 else 3)
        

    except Exception as e:
        data = (la.search(key1), la.search(key2))
        ge.load_page(root, ge.prevpage)
        print("Error occurred:", str(e))
        error = data[0] if type(data[0]) == str else data[1]
        ge.savedWidgets[0].config(text=error)

