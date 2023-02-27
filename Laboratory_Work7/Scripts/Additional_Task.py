import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = np.arange(0, 4*np.pi, 0.001)
y = np.sin(x)
line = plt.plot(x, y)
ax.set_title('y = sin(x)')
ax = plt.axis([0, 4 * np.pi, -1.1, 1.1])
dot, = plt.plot([0], [np.sin(0)], 'go')

def func(i):
    dot.set_data(i, np.sin(i))
    return dot,

animation = FuncAnimation(fig, func, frames=np.arange(0, 4 * np.pi, 0.1), interval=100, repeat=True)
plt.show()