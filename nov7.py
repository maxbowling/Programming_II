import matplotlib.pyplot as plt

fig,ax = plt.subplots()
fig.set_facecolor('lightblue')
fig.suptitle('Cool Graph')
ax.grid()
graph = ax.scatter([1,2,3,4,6],[1,2,3,4,8],color='red')
plt.show()
plt.savefig("Example2.png")