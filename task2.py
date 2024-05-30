import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")

button1 = tk.Button(window,text="Search by Name")
label1 = tk.Label(window, text="Client Database")
dogphoto = PhotoImage(file="dog.png")
label7 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window, text="Name")
label3 = tk.Label(window, text="Type")
label4 = tk.Label(window, text="Breed")
label5 = tk.Label(window, text="Owner")
label6 = tk.Label(window, text="Birthday")
entry1 = tk.Entry(window, width=15)
entry2 = tk.Entry(window, width=10)
entry3 = tk.Entry(window, width=10)
entry4 = tk.Entry(window, width=10)
entry5 = tk.Entry(window, width=10)
entry6 = tk.Entry(window, width=10)
button2 = tk.Button(window,text="< Previous")
button3 = tk.Button(window,text="Next >")
button4 = tk.Button(window,text="Save Entry", width=10, height=2)

button1.grid(row = 1, column = 4)
label7.grid(row=1, column=1, rowspan=3)
label1.grid(row = 1, column = 1)
entry1.grid(row = 1, column = 5)
label1.grid(row = 2, column = 3)
label2.grid(row = 4, column = 1)
label3.grid(row = 4, column = 2)
label4.grid(row = 4, column = 3)
label5.grid(row = 4, column = 4)
label6.grid(row = 4, column = 5)
entry2.grid(row = 5, column = 1)
entry3.grid(row = 5, column = 2)
entry4.grid(row = 5, column = 3)
entry5.grid(row = 5, column = 4)
entry6.grid(row = 5, column = 5)
button2.grid(row = 6, column = 1)
button4.grid(row=6, column=3)
button3.grid(row = 6, column = 5)

window.mainloop()



