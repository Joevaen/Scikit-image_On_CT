# bezier_curve()生成贝塞尔曲线坐标。
import numpy as np
from skimage.draw import bezier_curve
img = np.zeros((10, 10), dtype=np.uint8)
print(img[1, 5])
rr, cc = bezier_curve(1, 5, 5, -2, 8, 8, 2)
img[rr, cc] = 1
print(img)
print(img[1, 5])
print(img[5, -2])
print(img[8, 8])









