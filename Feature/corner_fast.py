# FAST拐点检测，拐点检测Opencv有七种，且比skimage的方法快的多
from skimage import data, feature, img_as_float, io
import numpy as np
image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))
gamma_corrected = feature.corner_fast(image)
points = feature.corner_peaks(gamma_corrected)
print(points)
io.imshow(image)
io.show()

