from PIL import Image
import numpy as np
import math
from scipy import signal
import urllib2, cStringIO

def boxfilter(n):
    "returns an n by n averaging box filter in the form of a Numpy array. Requires n to be odd."
    assert(n%2 != 0), "dimensions must be odd!"
    return np.ones((n, n))/(n*n)
    
def gauss1dalt(sigma):
    #Smoothing with a Gaussian is effective at suppressing noise and reducing detail
    #exp(- x^2 / (2*sigma^2))
    "returns a 1D Gaussian filter for a given value of sigma."    
    halfLen = np.ceil(3*(sigma))
    x = np.arange(-halfLen, halfLen+1, 1)
    filter = np.exp((-np.square(x))/(2*(np.square(sigma))))
    constant = 1.0/np.sum(filter)
    #constant2 = 1.0/(np.sqrt((2*np.pi))*sigma)
    return filter*constant
    
def gauss1d(sigma):
    #Smoothing with a Gaussian is effective at suppressing noise and reducing detail
    "returns a 1D Gaussian filter for a given value of sigma."    
    len = np.ceil(6*(sigma))
    if (len%2==0):
        len=len+1
    x = np.arange(0, len, 1)
    x = x - np.mean(x)
    filter = np.exp((-np.square(x))/(2*(np.square(sigma))))
    constant = 1.0/np.sum(filter)
    #constant2 = 1.0/(np.sqrt((2*np.pi))*sigma)
    return filter*constant
    
def gauss2d(sigma):
    "returns a 2D Gaussian filter for a given value of sigma."
    gaussx = gauss1d(sigma)
    gaussx = gaussx[np.newaxis]
    gaussy = np.transpose(gaussx)
    return signal.convolve2d(gaussx, gaussy)
    
def gaussconvolve2d(array,sigma):
    "applies Gaussian convolution to a 2D array for the given value of sigma."
    filter = gauss2d(sigma)
    return signal.convolve2d(array,filter,'same')
    
def nye():
    #load image
    URL = 'https://raw.githubusercontent.com/lulock/Vision/master/images/bill-nye.png'
    file = cStringIO.StringIO(urllib2.urlopen(URL).read())
    im = Image.open(file)
    im = im.convert('L')
    #convert to grayscale
    im = im.convert('L')
    #resize image
    dims = (im.size[0], im.size[1]/2)
    im = im.resize((im.size[0]/2, im.size[1]/2))
    #represent image as an array
    im_array = np.asarray(im)
    nye_array = im_array.copy()
    #use 2d gaussian filter to blur image
    nye_convolved = gaussconvolve2d(nye_array, 3)
    bill = Image.fromarray(nye_convolved)
    bill = bill.convert('RGB')
    #place images side by side
    compare = Image.new('RGB', dims)
    compare.paste(im, (0,0))
    compare.paste(bill, (im.size[0], 0))
    return compare
    
def nyeTwo():
    URL = 'https://raw.githubusercontent.com/lulock/Vision/master/images/bill-nye.png'
    file = cStringIO.StringIO(urllib2.urlopen(URL).read())
    im = Image.open(file)
    im = im.convert('L')
    #im.show()
    dims = (im.size[0], im.size[1]/2)
    im = im.resize((im.size[0]/2, im.size[1]/2))
    im_array = np.asarray(im)
    nye_array = im_array.copy()
    #use box filter to blur image
    nye_convolved = signal.convolve2d(nye_array,boxfilter(19),'same')
    bill = Image.fromarray(nye_convolved)
    bill = bill.convert('RGB')
    #place images side by side
    compare = Image.new('RGB', dims)
    compare.paste(im, (0,0))
    compare.paste(bill, (im.size[0], 0))
    return compare

def fresh():
    URL = 'http://img2.timeinc.net/people/i/2014/sandbox/news/140630/1994/will-smith-600x450.jpg'
    file = cStringIO.StringIO(urllib2.urlopen(URL).read())
    firstIm = Image.open(file)
    im = firstIm.convert('L')
    #im.show()
    im_array = np.asarray(im)
    im = im.convert('RGB')
    fresh_array = im_array.copy()
    #using 2d gaussian filter
    prince_convolved = gaussconvolve2d(fresh_array, 3)
    prince = Image.fromarray(prince_convolved)
    prince = prince.convert('RGB')
    #prince.show()
    #using box filter
    princebox = signal.convolve2d(fresh_array,boxfilter(19),'same')
    princebox = Image.fromarray(princebox)
    princebox = princebox.convert('RGB')
    #sharpening box filter
    princesharp = signal.convolve2d(fresh_array,sharpen(19),'same')
    princesharp = Image.fromarray(princesharp)
    princesharp = princesharp.convert('RGB')
    #display images side by side comparing gaussian and box filter at the bottom
    dims = (im.size[0]*2, im.size[1]*2)
    compare = Image.new('RGB', dims)
    compare.paste(im, (0,0))
    compare.paste(princesharp, (im.size[0],0))
    compare.paste(prince, (0, im.size[1]))
    compare.paste(princebox, (im.size[0], im.size[1]))
    return compare
    
def sharpen(n):
    "returns an n by n box filter in the form of a Numpy array. Requires n to be odd."
    assert(n%2 != 0), "dimensions must be odd!"
    filter = np.zeros((n, n))
    filter[n/2,n/2] = 2
    filter = filter - boxfilter(n)
    return filter