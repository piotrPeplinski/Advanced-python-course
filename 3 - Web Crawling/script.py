import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pickle


root = tk.Tk()
root.title('Books prices')
root.geometry('800x500')

chart_frame = tk.Frame(root, background='#ffffff')
chart_frame.pack(side=tk.LEFT, padx=10, pady=10)

# load charts
with open('rating.pickle', 'rb') as file:
    ratings_chart = pickle.load(file)

with open('stocks.pickle', 'rb') as file:
    stocks_chart = pickle.load(file)

def show_ratings():
    canvas = FigureCanvasTkAgg(ratings_chart.get_figure(), chart_frame)
    canvas.get_tk_widget().pack()
    canvas.draw()

ratings_btn = ttk.Button(root, text='Show ratings chart', command=show_ratings)
ratings_btn.pack(side=tk.TOP, padx=5, pady=5)

root.mainloop()
