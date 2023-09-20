import matplotlib.pyplot as plt


class Chart:
    def __init__(self, x: list, y: list, title: str, x_label: str, y_label: str = 'Price'):
        self.__x = x
        self.__y = y
        self.__x_label = x_label
        self.__y_label = y_label
        self.__title = title
        self.generate_chart()

    def generate_chart(self):
        self.__fig, ax = plt.subplots(figsize=(6, 5))
        ax.scatter(self.__x, self.__y)
        ax.set_title(self.__title, fontsize=14)
        ax.set_xlabel(self.__x_label)
        ax.set_ylabel(self.__y_label)
        ax.grid(True)

    def get_figure(self):
        return self.__fig
