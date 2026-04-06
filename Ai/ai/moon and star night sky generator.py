import numpy as np
import matplotlib.pyplot as plt
plt.figure(facecolor="black")
plt.scatter(np.random.rand(200),
            np.random.rand(200),color="white",s=4)
moon=plt.Circle((0.7,0.7),0.1,color="lightgray")
plt.gca().add_patch(moon)
plt.axis("off")
plt.show()