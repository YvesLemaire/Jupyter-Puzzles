import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['toolbar'] = 'None'

#fig = plt.figure(facecolor='w', figsize = (7, 7), frameon = True)
fig = plt.figure(facecolor='w', frameon = True)
ax = fig.add_subplot(111)
ax.axis('off')
ax.axis('equal')
ax.axis([-3,3,-3,3])

for u in range(-1,3):
    ax.plot([u + .5 for _ in range(3)], [y + .5 for y in range(-1,2)], color = 'grey')
    if u < 2:
        ax.plot([x + .5 for x in range(-1,3)], [u + .5 for _ in range(4)], color = 'grey')
for i in range(3):
    for j in range(2):
        ax.plot(i,j, color = 'black', marker = 'o', markersize = '2')
        ax.text(i, j - .2, f'${i},{j}$', fontsize = 11, color = 'black', verticalalignment = 'top', horizontalalignment = 'center')

#plt.show()

plt.savefig('grille.png')