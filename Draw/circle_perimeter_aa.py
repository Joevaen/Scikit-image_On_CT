# 生成抗锯齿圆周长坐标。
import numpy as np
from skimage.draw import circle_perimeter_aa
img = np.zeros((10, 10), dtype=np.uint8)
rr, cc, val = circle_perimeter_aa(4, 4, 3)
img[rr, cc] = val * 255
print(img)









