import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("300x140")

label1 = tk.Label(window, text = "Pochacco!")
label2 = tk.Label(window, text = "A cuddly little puppy! This is from the same\n creators who brought you Keropi and Kero Kero", bg="#00FFFF")
dogphoto = PhotoImage(file="dog.png")
label3 = tk.Label(window, image=dogphoto)

label1.place(x=165,y=45)
label2.place(x=0,y=100)
label3.place(x=100,y=0)

window.mainloop()