
# Resizing Images and Building Pyramids!


```python
import pyramids as pyr
from PIL import Image
import numpy as np
import math
from scipy import signal
import urllib2, cStringIO
```


```python
URL = 'https://41.media.tumblr.com/5303218fa7840af56d79ed2d0927d0e6/tumblr_nudw3yYb8e1smba53o1_500.jpg'
file = cStringIO.StringIO(urllib2.urlopen(URL).read())
image = Image.open(file)
```


```python
minsize = 100
pyramid = pyr.MakePyramid(image, minsize)
```


```python
pyr.CompilePyramid(pyramid)
```




![png](output_4_0.png)




