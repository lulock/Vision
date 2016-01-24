from PIL import Image
import numpy as np
import math
from scipy import signal
import urllib2, cStringIO

def MakePyramid(image, minsize):
    '''returns a list including the original PIL image 
    followed by all the PIL of images of reduced size'''
    factor = 0.75
    pyramid = [image];
    while True:
        x = image.size[0];
        y = image.size[1];
        image = image.resize((int(x*factor), int(y*factor)), Image.BICUBIC)
        pyramid.append(image);
        if (x < minsize) | (y < minsize):
            break
    return pyramid
            
def CompilePyramid(pyramid):
    '''displays all images in pyramid as one horizontal image'''
    length = sum(image.size[0] for image in pyramid)
    height = int(pyramid[0].size[1])
    canvas = Image.new('RGB', (length, height), color ='white')
    offset = 0
    for im in pyramid:
        canvas.paste(im, (offset,0))
        offset = offset + im.size[0]
    return canvas