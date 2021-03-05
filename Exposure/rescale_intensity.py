# 图像强度归一化
from skimage import data, exposure, img_as_float, io
import numpy as np
img = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))
io.imshow(img)
io.show()
p2, p98 = np.percentile(img, (2, 98))
img_rescale = exposure.rescale_intensity(img, in_range=(p2, p98))


io.imshow(img_rescale)
io.show()