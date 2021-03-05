# 生成椭圆区域内的坐标
import numpy as np
from skimage.draw import ellipse
img = np.zeros((10, 12), dtype=np.uint8)
rr, cc = ellipse(5, 6, 3, 5, rotation=np.deg2rad(30))
img[rr, cc] = 1
print(img)









