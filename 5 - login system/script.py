import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Authentication system')

frame = tk.Frame(root)
frame.pack(pady=20)

username_label = tk.Label(frame, text='Username')
username_entry = tk.Entry(frame)

password_label = tk.Label(frame, text='Password')
password_entry = tk.Entry(frame, show='*')

username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)

password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)

register_btn = tk.Button(frame, text='Register')
login_btn = tk.Button(frame, text='Login')

register_btn.grid(row=2, column=0)
login_btn.grid(row=2, column=1)


root.mainloop()
