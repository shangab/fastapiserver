import tkinter as tk

root = tk.Tk()

root.geometry("800x500")

root.title("MY FIRST GUI")

label = tk.Label(root,text="hello world",font=('Arial',22)) 

label.pack()
root.mainloop()