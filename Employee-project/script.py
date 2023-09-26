import tkinter as tk
from tkinter import messagebox
import sqlite3
import pandas as pd


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

def register_employee():
    name = name_entry.get()
    salary = salary_entry.get()
    position = position_entry.get()

    df = pd.DataFrame({
        'Name':[name],
        'Salary':[float(salary)],
        'Position':[position]
    })

    connection = sqlite3.connect('groszek-firma.sqlite')
    cursor = connection.cursor()
    #check if empty
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()
    df.to_sql('employees',connection,if_exists='append',index=False)
    if not data:
        cursor.execute('CREATE UNIQUE INDEX unique_name ON employees (Name)')
        connection.commit()
        
    
    connection.close()

    name_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)
    position_entry.delete(0, tk.END)



name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

salary_label.grid(row=1, column=0)
salary_entry.grid(row=1, column=1)

position_label.grid(row=2, column=0)
position_entry.grid(row=2, column=1)

register_btn = tk.Button(frame, text='Register employee',command=register_employee)
register_btn.grid(row=3,column=1)


root.mainloop()