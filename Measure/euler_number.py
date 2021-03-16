# 计算二值图像中的欧拉特性。可以计算3d
# https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_euler_number.html#sphx-glr-auto-examples-segmentation-plot-euler-number-py
# 对于2D对象，欧拉数是对象数减去孔数。 对于3D对象，欧拉数是对象的数量加上孔的数量减去隧道或循环的数量而获得的。
import numpy as np
from skimage.measure import euler_number
SAMPLE = np.zeros((100,100,100))
SAMPLE[40:60, 40:60, 40:60]=1
print(euler_number(SAMPLE))

SAMPLE[45:55,45:55,45:55] = 0
print(euler_number(SAMPLE))

SAMPLE = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                   [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                   [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0],
                   [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
                   [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]])
print(euler_number(SAMPLE))  # doctest:

print(euler_number(SAMPLE, connectivity=1))  # doctest:
