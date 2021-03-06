# :camera: Let's have some fun with Python and computer vision

Starting by importing some libraries
```python
from PIL import Image
import numpy as np
import math
from scipy import signal
import urllib2, cStringIO
```
The first couple of convolutions to discover is with the use of 
- a boxfilter that blurs by averaging
- a 2d gaussian filter
- a sharpening boxfilter

###This is our original image:
<p align="center">
  <img src="https://raw.githubusercontent.com/lulock/Vision/master/filters/images/fresh.jpg" alt="The Original Fresh Prince"/>
</p>

Now, here's the image in grayscale (top left), **sharpened** using a boxfilter (top right), **blurred** with a **2d Gaussian filter** (bottom left), and **blurred** using a boxfilter (bottom right): 
![Comparison of applied filters][prince]

###Bill Nye with Gaussian blur: 
![Gaussian blur][bill]

[bill]: https://raw.githubusercontent.com/lulock/Vision/master/filters/images/Output/billBlur.png "Bill Nye Gaussian Blur"
[prince]: https://raw.githubusercontent.com/lulock/Vision/master/filters/images/Output/prince.png "Fresh Prince Convolutions"
