import numpy as np
from ipywidgets import interact, fixed
from PIL import Image


def imgResize(im, size):
    img = Image.fromarray(im)
    img = img.resize(size)
    return img

def imshow(X, resize=None):
    interact(imgResize, im=fixed(X), size=fixed(resize))