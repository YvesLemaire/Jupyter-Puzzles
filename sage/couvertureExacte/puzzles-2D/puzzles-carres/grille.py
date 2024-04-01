import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['toolbar'] = 'None'

#fig = plt.figure(facecolor='w', figsize = (7, 7), frameon = True)
fig = plt.figure(facecolor='w', frameon = True)
ax = fig.add_subplot(111)
ax.axis('off')
ax.axis('equal')
ax.axis([-3,3,-3,3])

for u in range(-3,3):
    ax.plot([u + .5 for _ in range(6)], [y + .5 for y in range(-3,3)], color = 'grey')
    ax.plot([x + .5 for x in range(-3,3)], [u + .5 for _ in range(6)], color = 'grey')
for i in range(-2,3):
    for j in range(-2,3):
        ax.plot(i,j, color = 'black', marker = 'o', markersize = '2')
        ax.text(i, j - .2, f'${i},{j}$', fontsize = 11, color = 'black', verticalalignment = 'top', horizontalalignment = 'center')


plt.savefig('grille.png')