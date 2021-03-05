# circle()生成一个圆形的周长内的坐标。
import numpy as np
from skimage.draw import circle_perimeter
img = np.zeros((20, 20), dtype=np.uint8)
rr, cc = circle_perimeter(10, 10, 5)
img[rr, cc] = 1
print(img)










