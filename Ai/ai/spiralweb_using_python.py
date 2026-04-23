import matplotlib.pyplot as plt
import numpy as np

nl = 50
n_p = 1000

fig, ax = plt.subplots(figsize=(6, 6))

# Make theta same size as r
theta = np.linspace(0, 20*np.pi, n_p)
r = np.linspace(0, 1, n_p)

x = r * np.cos(theta)
y = r * np.sin(theta)

ax.plot(x, y, color='black')

# radial lines
for i in range(nl):
    angle = 2 * np.pi * i / nl
    xl = [0, np.cos(angle)]
    yl = [0, np.sin(angle)]
    ax.plot(xl, yl, color='black', linewidth=0.8)

ax.axis('off')
plt.show()