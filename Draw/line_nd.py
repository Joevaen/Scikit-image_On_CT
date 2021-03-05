# 用于在n维空间中画直线，返回这条直线上的所有点坐标
from skimage.draw import line_nd
import numpy as np
lin = line_nd((1, 1), (5, 2.5), endpoint=False)
print(lin)

im = np.zeros((6, 5), dtype=int)
im[lin] = 1
print(im)


lin2 = line_nd([2, 1, 1], [5, 5, 2.5], endpoint=True)
print(lin2)
