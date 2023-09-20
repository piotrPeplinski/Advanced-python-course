import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from chart_class import Chart
import pickle



root = tk.Tk()
root.title('Books prices')
root.geometry('800x500')

chart_frame = tk.Frame(root, background='#ffffff')
chart_frame.pack(side=tk.LEFT, padx=10, pady=10)

with open('data_frame.pickle', 'rb') as file:
    df = pickle.load(file)

chart = Chart(df['Rating'], df['Price'], 'hello', 'Rating')

canvas = FigureCanvasTkAgg(chart.get_figure(), chart_frame)
canvas.get_tk_widget().pack()
canvas.draw()

root.mainloop()
