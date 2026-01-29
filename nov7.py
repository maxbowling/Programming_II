import matplotlib.pyplot as plt

fig,ax = plt.subplots()
fig.set_facecolor('lightblue')
fig.suptitle('Cool Graph')
ax.grid()
graph = ax.scatter([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,2,7,8,5,9,10,],color='green')

plt.savefig("Example4.png")
plt.show()