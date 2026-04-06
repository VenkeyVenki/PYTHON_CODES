import matplotlib.pyplot as plt
fig, ax=plt.subplots()
steps=["Start","Input n","For i=1 to n","Print spaces",
       "Print increasing numbers",
       "Print decreasing numbers","End"]
y=0.9
for s in steps:
    ax.text(0.5,y,s,ha='center',
            bbox=dict(boxstyle="round"))
    if y>0.1:
        ax.annotate("",(0.5,y-0.1),(0.5,y),
                    arrowprops=dict(arrowstyle="->"))
    y-=0.12
ax.axis('off')
plt.show()