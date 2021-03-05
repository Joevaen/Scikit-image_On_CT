# 生成两点间直线上抗锯齿线像素坐标。
from skimage.draw import line_aa
import numpy as np
img = np.zeros((10, 10), dtype=np.uint8)
rr, cc, val = line_aa(1, 1, 8, 8)
img[rr, cc] = val * 255
print(img)









