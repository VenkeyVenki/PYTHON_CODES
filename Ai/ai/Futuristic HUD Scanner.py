import matplotlib.pyplot as plt
import numpy as np
plt.ion()
theta=np.linspace(0,2*np.pi,300)
for t in np.linspace(0,10,100):
    plt.clf()
    plt.gca().set_facecolor("black")
    for r in [1,1.5,2]:
        plt.plot(r*np.cos(theta),r*np.sin(theta),
                 color='cyan',alpha=0.3)
    angle=t
    x=[0,2*np.cos(angle)]
    y=[0,2*np.sin(angle)]
    plt.plot(x,y,color='lime',lw=2)
    for a in np.linspace(0,2*np.pi,6):
        px=1.5*np.cos(a+t*0.5)
        py=1.5*np.sin(a+t*0.5)
        plt.scatter(px,py,color='red',s=50)
    plt.scatter(0,0,color='cyan',s=100),plt.xlim(-2.5,2.5)
    plt.ylim(-2.5,2.5),plt.axis('off')
    plt.title("Futuristic HUD Scanner",color='pink')
    plt.pause(0.05),plt.show()