import tkinter as tk
from tkinter import messagebox
import sqlite3


root = tk.Tk()
root.title('Employees registry')

frame = tk.Frame(root)
frame.pack(pady=20)

name_label = tk.Label(frame, text='Name')
name_entry = tk.Entry(frame)

salary_label = tk.Label(frame, text='Salary')
salary_entry = tk.Entry(frame)

position_label = tk.Label(frame, text='Position')
position_entry = tk.Entry(frame)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

salary_label.grid(row=1, column=0)
salary_entry.grid(row=1, column=1)

position_label.grid(row=2, column=0)
position_entry.grid(row=2, column=1)

register_btn = tk.Button(frame, text='Register employee')
register_btn.grid(row=3,column=1)


root.mainloop()