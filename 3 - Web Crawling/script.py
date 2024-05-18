import matplotlib
matplotlib.use('Agg')
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pickle
from functools import partial


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

current_chart = None

def show_chart(chart):
    global current_chart
    if current_chart:
        current_chart.get_tk_widget().destroy()
        current_chart = None

    canvas = FigureCanvasTkAgg(chart.get_figure(), chart_frame)
    canvas.get_tk_widget().pack()
    canvas.draw()
    current_chart = canvas


ratings_btn = ttk.Button(root, text='Show ratings chart',
                         command=partial(show_chart, ratings_chart))
ratings_btn.pack(side=tk.TOP, padx=5, pady=5)

stocks_btn = ttk.Button(root, text='Show stock chart',
                        command=partial(show_chart, stocks_chart))
stocks_btn.pack(side=tk.TOP, padx=5, pady=5)

root.mainloop()
