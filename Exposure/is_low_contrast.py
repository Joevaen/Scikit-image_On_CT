#　判断图像对比度是不是偏低
from skimage import data, exposure, img_as_float, io
import numpy as np
image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))


img1 = exposure.is_low_contrast(image)
print(img1)

img2 = exposure.is_low_contrast(image, upper_percentile=100)
print(img2)

