import pickle
import matplotlib.pyplot as plt

with open('data_frame.pickle', 'rb') as file:
    df = pickle.load(file)


class Chart:
    def __init__(self, x: list, y: list, title: str, x_label: str, y_label: str = 'Price'):
        self.__x = x
        self.__y = y
        self.__x_label = x_label
        self.__y_label = y_label
        self.__title = title
        self.generate_chart()

    def generate_chart(self):
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(self.__x, self.__y)
        ax.set_title(self.__title, fontsize=14)
        ax.set_xlabel(self.__x_label)
        ax.set_ylabel(self.__y_label)
        ax.grid(True)


chart = Chart(df['Rating'], df['Price'], 'Rating relation to price', 'Rating')

plt.show()
