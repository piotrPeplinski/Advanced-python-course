import pickle
import matplotlib.pyplot as plt

with open('data_frame.pickle', 'rb') as file:
    df = pickle.load(file)

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(df['Rating'], df['Price'])
ax.set_title('Rating relation to price',fontsize=14)
ax.set_xlabel('Rating')
ax.set_ylabel('Price')
ax.grid(True)
plt.show()
