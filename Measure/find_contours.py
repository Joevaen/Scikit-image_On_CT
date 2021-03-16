# 在2D数组中找到给定级别值的等值轮廓。
#
# 使用“行进平方”方法为特定级别值计算输入2D数组的等值轮廓。 线性地对数组值进行插值，以为输出轮廓提供更好的精度。
import numpy as np
from skimage.measure import find_contours
a = np.zeros((3, 3))
a[0, 0] = 1
print(a)



print(find_contours(a, 0.5))

