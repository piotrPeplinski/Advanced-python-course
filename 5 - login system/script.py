import tkinter as tk
from tkinter import messagebox

credentials = {}

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


def register():
    username = username_entry.get()
    password = password_entry.get()

    if username in credentials:
        messagebox.showerror('Registration Failed', 'Username already exists.')
    else:
        credentials[username] = password
        messagebox.showinfo('Registration Successful', 'Account created successfully!')

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in credentials:
        if credentials[username] == password:
            messagebox.showinfo('Login successful','Login successful')
        else:
            messagebox.showerror('Login Failed', 'Incorrect password.')
    else:
        messagebox.showerror('Login Failed', 'No such user.')

register_btn = tk.Button(frame, text='Register', command=register)
login_btn = tk.Button(frame, text='Login', command=login)

register_btn.grid(row=2, column=0)
login_btn.grid(row=2, column=1)




root.mainloop()
