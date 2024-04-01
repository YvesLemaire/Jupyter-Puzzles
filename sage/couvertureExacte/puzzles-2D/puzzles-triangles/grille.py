import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['toolbar'] = 'None'

#fig = plt.figure(facecolor='w', figsize = (7, 7), frameon = True)
fig = plt.figure(facecolor='w', frameon = True)
ax = fig.add_subplot(111)
ax.axis('off')
ax.axis('equal')
#ax.axis([-3,3,-3,3])

c = .5 * 3. ** .5

for i in range(4):
   ax.plot([i, i + 1.],[0, c * 2], color = 'grey')
for j in range(3):
   ax.plot([.5 * j, 3. + .5 * j],[c * j, c * j], color = 'grey')
   if j: ax.plot([.5 * j, j],[c * j, 0], color = 'grey')   
ax.plot([2., 3.],[c * 2., 0.], color = 'grey')
ax.plot([3., 3.5],[c * 2., c], color = 'grey')

for i in range(3):
    for j in range(2):
        ax.text(i + .5 * j + .5, j * c + .2, f'${i},{j},2$', fontsize = 12, color = 'black', verticalalignment = 'bottom', horizontalalignment = 'center')
        ax.text(i + .5 * j + 1., (j + 1) * c - .2, f'${i},{j},1$', fontsize = 12, color = 'black', verticalalignment = 'top', horizontalalignment = 'center')


plt.savefig('grille.png')