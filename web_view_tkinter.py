import tkinterweb
import tkinter as tk
root = tk.Tk()
frame = tkinterweb.HtmlFrame(root)
frame.load_website('https://www.google.com/')
frame.pack(fill="both", expand=True)
root.mainloop()
