import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as pch
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
import numpy as np
mpl.rcParams['toolbar'] = 'None'

L = 1.5

fig = plt.figure(facecolor='w', figsize = (L, L), frameon = True)
ax = fig.add_subplot(111)
ax.axis('off')
ax.axis('equal')
#ax.axis([0, L, 0, L])

kwargs = {'color' : 'lightgrey', 'linewidth' : 1.}
for i in range(8):
    ax.plot([i-.5, i-.5],[-.5, 8 - .5],**kwargs)
    ax.text(i, -.75, '$'+str(i)+'$', fontsize = 8, color = 'black', verticalalignment = 'top', horizontalalignment = 'center')
for j in range(8):
    ax.plot([-.5, 8 - .5],[j - .5, j - .5],**kwargs)
    ax.text(-.75, j, '$'+str(j)+'$' , fontsize = 8, color = 'black', verticalalignment = 'center', horizontalalignment = 'right')

def rect(i,j,color):
    ax.add_patch(plt.Rectangle((i - .5, j - .5), 1 , 1, fill = True, fc = color))

rect(0,0,'red')
plt.savefig('fig1-1.png')
for i in range(1,8):
    rect(i,0,'green')
    rect(i,i,'green')
    rect(0,i,'green')
plt.savefig('fig1-2.png')

rect(2,1,'red')
rect(1,2,'red')
plt.savefig('fig1-3.png')
for i in range(3,8):
    rect(i,1,'green')
    rect(2,i,'green')
    rect(i,i-1,'green')
    rect(1,i,'green')
    rect(i,2,'green')
    rect(i-1,i,'green')
plt.savefig('fig1-4.png')

rect(5,3,'red')
rect(3,5,'red')
plt.savefig('fig1-5.png')
for i in range(3,8):
    for i, j in [(6,3),(6,4),(7,3),(7,5)]:
        rect(i,j,'green')
        rect(j,i,'green')
plt.savefig('fig1-6.png')

rect(7,4,'red')
rect(4,7,'red')
plt.savefig('fig1-7.png')

from PIL import Image
import os

image = []
for i in range(1,8):
    image.append(Image.open(f"fig1-{i}.png"))

width, height = image[0].size

new_image = Image.new("RGB", (7 * width, height))

for i, im in enumerate(image):
    new_image.paste(im, (i * width,0))
                
new_image.save("fig1.png")
for i in range(1,8):
    os.remove(f"fig1-{i}.png")



