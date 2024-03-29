import os
import PIL
import numpy as np

def fig2im(fig):
    """Convert a Matplotlib figure to a PIL Image and return it"""
    import io
    buf = io.BytesIO()
    fig.savefig(buf, bbox_inches = 'tight')
    buf.seek(0)
    im = PIL.Image.open(buf)
    return im

def adjustBorders(im, border = 0, color = (255, 255, 255)):
    t = np.array(im)
    u, d, l, r  = 0, im.height - 1, 0, im.width - 1
    while (t[u,:,:3] == color).all(): u += 1
    while (t[d,:,:3] == color).all(): d -= 1
    while (t[:,l,:3] == color).all(): l += 1
    while (t[:,r,:3] == color).all(): r -= 1
    return PIL.ImageOps.expand(im.crop((l, u, r + 1, d + 1)), border, color)

def concat(ims, nbColonnes = 10, reduceFactor = 1., border = 10): 
    """
    ims est une liste d'images PIL (par ex. obtenues avec PIL.Image.open(file)))
    nbColonnes = 0 (horizontal) ou -1 (vertical) ou le nombre d'images par ligne
    """
    horizontal = 0
    vertical = -1
    ims = [im.reduce(reduceFactor) for im in ims]
    if border is not None:
        ims = [adjustBorders(im, border = border) for im in ims]
    widths, heights = list(zip(*[im.size for im in ims]))
    if nbColonnes == horizontal:
        width = sum(widths)
        height = max(heights)
        im = PIL.Image.new("RGB", (width, height), color = 'white')
        w = 0
        for i, image in enumerate(ims):
            im.paste(image, (w, 0))
            w += widths[i]
    elif nbColonnes == vertical:
        width = max(widths)
        height = sum(heights)
        im = PIL.Image.new("RGB", (width, height), color = 'white')
        h = 0
        for i, image in enumerate(ims):
            im.paste(image, (0, h))
            h += heights[i]
    else:
        n = int(nbColonnes)
        L = [ims[k *n:(k+1)*n] for k in range(len(ims) // n + 1 if len(ims) % n else len(ims) // n)]
        return concat([concat(l, nbColonnes = horizontal, reduceFactor=reduceFactor, border = border) for l in L],nbColonnes=vertical, border = border)
    return im

def _max(prefix):
    i = 0
    while os.path.isfile(f'{prefix}{i}.png'):
        i += 1
    return i - 1

def cv(prefix, dpi = 90): # dpi inutilisé
# Cette méthode ne fonctionne pas dans Google Colab

    #! pip install opencv-python
    #! pip install opencv-contrib-python

    import cv2

    for i in range(_max(prefix) + 1):
        img = cv2.imread(f'{prefix}{i}.png', cv2.IMREAD_COLOR)
        cv2.imshow('', img)
        cv2.waitKey(0)
    cv2.destroyAllWindows()
 

def mpl(prefix, dpi = 90):

    import matplotlib.animation
    import matplotlib.pyplot as plt
    import matplotlib.cbook as cbook

    plt.rcParams["animation.html"] = "jshtml"
    plt.rcParams['figure.dpi'] = dpi
    plt.ioff()
    fig, ax = plt.subplots()

    def animate(t):
        plt.cla()
        plt.axis('off')
        with cbook.get_sample_data(f'{prefix}{t}.png') as image_file:
            image = plt.imread(image_file)
        #return image
        plt.imshow(image)
    
    anim = matplotlib.animation.FuncAnimation(fig, animate, frames = _max(prefix) + 1)
    return anim
    

def widgets(prefix, dpi = 90):

    import ipywidgets
    from IPython.display import display
    import matplotlib.pyplot as plt
    import matplotlib.cbook as cbook

    plt.rcParams['figure.dpi'] = dpi

    def animate(t = 0):
        plt.cla()
        plt.axis('off')
        with cbook.get_sample_data(f'{prefix}{t}.png') as image_file:
            image = plt.imread(image_file)
        plt.imshow(image)

    slider = ipywidgets.IntSlider(min=0, max=_max(prefix), step=1, value=0)
    button = ipywidgets.Button(description="▷")

    def on_button_clicked(b):
        t = slider.value
        if t < slider.max: slider.value = t + 1

    button.on_click(on_button_clicked)

    anim = ipywidgets.interact(animate, t = slider)
    display(button)


