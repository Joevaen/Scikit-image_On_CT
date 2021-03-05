# 对给定的图像中的坐标赋予颜色
from skimage.draw import line, set_color
import numpy as np
img = np.zeros((10, 10), dtype=np.uint8)
rr, cc = line(1, 1, 20, 20)
set_color(img, (rr, cc), 1)
print(img)









