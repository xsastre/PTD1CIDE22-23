import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * x*x + 3*x

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(-8, 8), xticks=np.arange(-8, 8),
       ylim=(8, 8), yticks=np.arange(-8, 8))

plt.show()