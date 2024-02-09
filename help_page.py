import tkinter as tk
import general as ge

def help(root):
    ge.savedWidgets[0].config(text="")
    ge.prevpage = ge.keep_page(root)
    frame = tk.Frame(root, width=root.winfo_width(), height=root.winfo_height()) 
    frame.place(y=50)