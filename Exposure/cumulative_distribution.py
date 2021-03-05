# 返回给定图像的累积分布函数（cdf）。
from skimage import data, exposure, img_as_float, io
import numpy as np
image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))
hi = exposure.histogram(image)
cdf = exposure.cumulative_distribution(image)
print(np.alltrue(cdf[0] == np.cumsum(hi[0])/float(image.size)))
