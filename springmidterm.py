import matplotlib.pyplot as plt

fig,ax = plt.subplots()
fig.set_facecolor('lightblue')
fig.suptitle('Blue Graph')
ax.grid()
graph = ax.scatter([1,2,3,4,5,],[1,2,3,4,2],color='blue')

plt.savefig("Example4.png")
plt.show()
print("I am just messing around on this file until I start my project")