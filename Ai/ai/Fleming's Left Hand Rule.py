import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.quiver(0,0,0,1,0,0,color='red')
ax.quiver(0,0,0,0,1,0,color='blue')
ax.quiver(0,0,0,1,0,1,color='green')
ax.text(1,0,0,"Current (I)")
ax.text(0,1,0,"Field (B)")
ax.text(0,0,1,"Force (F)")
plt.title("Fleming's Left Hand Rule")
plt.show()