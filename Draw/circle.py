# circle()生成一个圆形的区域内的坐标，会在0.19版本中移除，用draw.disk()代替。
import numpy as np
from skimage.draw import circle
img = np.zeros((20, 20), dtype=np.uint8)
rr, cc = circle(10, 10, 5)
img[rr, cc] = 1
print(img)










