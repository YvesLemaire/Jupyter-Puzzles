def cv(prefix, max, dpi = 90): # dpi inutilisé
# Cette méthode ne fonctionne pas dans Google Colab

    #! pip install opencv-python
    #! pip install opencv-contrib-python

    import cv2

    for i in range(max + 1):
        img = cv2.imread(f'{prefix}{i}.png', cv2.IMREAD_COLOR)
        cv2.imshow('', img)
        cv2.waitKey(0)
    cv2.destroyAllWindows()
 

def mpl(prefix, max, dpi = 90):

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
    
    anim = matplotlib.animation.FuncAnimation(fig, animate, frames = max + 1)
    return anim
    

def widgets(prefix, max, dpi = 90):

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

    slider = ipywidgets.IntSlider(min=0, max=max, step=1, value=0)
    button = ipywidgets.Button(description="▷")

    def on_button_clicked(b):
        t = slider.value
        if t < slider.max: slider.value = t + 1

    button.on_click(on_button_clicked)

    anim = ipywidgets.interact(animate, t = slider)
    display(button)
