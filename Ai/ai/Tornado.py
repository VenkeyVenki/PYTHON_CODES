import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,10*np.pi,1000)
r=np.linspace(0,2,1000)
x=r*np.cos(t)
y=r*np.sin(t)
plt.scatter(x,y,s=1)
plt.title("Tornado")
plt.axis('off')
plt.show()