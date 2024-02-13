import tkinter as tk
import general as ge
import main as la
import requests
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def results(root, key1, key2, key3, country, start_date, end_date):
    ge.savedWidgets[0].config(text="")
    ge.prevpage = ge.keep_page(root)
    frame = tk.Frame(root, width=root.winfo_width(), height=root.winfo_height()) 
    frame.place(y=50)  
    try:
        data = (la.search(key1), la.search(key2), la.search(key3))
        print(data)
        if country:

            for i in range(2):
                name_label = tk.Label(frame, text=data[i][0], font=(ge.font, 30, "bold"))
                name_label.grid(row=1, column=1 if i == 1 else 3)
                flag = ge.Photo(frame, image_path=data[i][4], height=200)
                flag.label.grid(row=2, column=1 if i == 1 else 3)
        else:
            for i in range(2):
                name_label = tk.Label(frame, text=data[i][1], font=(ge.font, 30, "bold"))
                name_label.grid(row=1, column=1 if i == 1 else 3)
            

        vs_label = tk.Label(frame, text="VS", font=(ge.font, 30, "bold"), padx=50)
        vs_label.grid(row=1, column=2)

    
        for i in range(2):
            text = tk.Label(frame, text=f"Name: {data[i][1]}\nCode: {data[i][2]}\nSymbol: {data[i][3]}")
            text.grid(row=3, column= 1 if i == 1 else 3)
        
        key = f"https://api.frankfurter.app/{start_date}..{end_date}?from={data[2][2]}&to={data[0][2]},{data[1][2]}"
        print(key)

        la.penge.toCurrency1 = data[0]
        la.penge.toCurrency2 = data[1]
        la.penge.fromCurrency = data[2]
        la.penge.startDate = start_date
        la.penge.endDate = f"..{end_date}"
        fig, error = la.penge.plotter(data=(requests.get(key)).json())
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=4, column=1, columnspan=3, pady=10, padx=10)
        canvas_widget.config(height=300, width=600)

        for i in error:
            end_date_text = "i dag" if end_date == "" else end_date
            label = tk.Label(frame, text=f"Manglende data for {data[i][2]} mellom {start_date} og {end_date if len(end_date) > 2 else end_date_text}", fg="red")
            label.grid(row=5, column=i+1)
        

    except Exception as e:
    
        keys = [key1,key2,key3]
        data = (la.search(key1), la.search(key2), la.search(key3))

        ge.load_page(root, ge.prevpage)
        print("Error occurred:", str(e))
        error = None
        for i in range(len(data)):
            if type(data[i-1]) == str:
                error = f"Fant ikke {'landet' if country else 'valutaen'} {keys[i-1]}"
        if data[0][2] == data[1][2] and data[0][2] == data[2][2]:
            error = f"Alt er jo {data[0] [1]} din idiot"
        else:
            error = f"Datoene stemmer ikke YYYY-MM-DD"
        
        ge.savedWidgets[0].config(text=error)
