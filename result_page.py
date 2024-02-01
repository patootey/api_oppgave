import tkinter as tk
import general as ge
import landAPI as la

def results(root, key1, key2, country):
    ge.prevpage = ge.keep_page(root)
    frame = tk.Frame(root, bg='red', width=root.winfo_width(), height=root.winfo_height())  # Set a background color and dimensions for visibility
    frame.place(y=50)  # Adjust coordinates as needed
    try:
        if country:
            image_url1 = la.search(key1)[3]
            image_url2 = la.search(key2)[3]

            flag1 = ge.Photo(frame, image_path=image_url1)
            flag1.label.place(x=0, y=0)

            flag2 = ge.Photo(frame, image_path=image_url2)
            flag2.label.place(x=100, y=0)
            print("HABSAD")

    except Exception as e:
        ge.load_page(root, ge.prevpage)
        print("Error occurred:", str(e))
        print(la.search(key1))
        print(la.search(key2))
