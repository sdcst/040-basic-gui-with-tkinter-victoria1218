import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title("T-Town Veterniary Clinic Database")
dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image= dogphoto)
label2 = tk.Label(window, text= "Client Database")


window.mainloop()



