from skimage.data import coins
from skimage.filters import threshold_multiotsu
from skimage.color import label2rgb
from skimage import data, io
import numpy as np
image = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg')
thresholds = threshold_multiotsu(image)
regions = np.digitize(image, bins=thresholds)
regions_colorized = label2rgb(regions)
io.imshow(regions)
io.show()