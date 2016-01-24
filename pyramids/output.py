import pyramids as pyr
from PIL import Image
from urllib.request import urlopen
from io import BytesIO 

URL = 'https://41.media.tumblr.com/5303218fa7840af56d79ed2d0927d0e6/tumblr_nudw3yYb8e1smba53o1_500.jpg'
file = BytesIO(urlopen(URL).read())
image = Image.open(file)

minsize = 100
pyramid = pyr.MakePyramid(image, minsize)
canvas = pyr.CompilePyramid(pyramid)
canvas.save('pyramid.png', 'PNG')