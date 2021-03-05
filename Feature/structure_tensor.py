# 使用平方差之和计算结构张量。
from skimage.feature import structure_tensor
import numpy as np
square = np.zeros((5, 5))
square[2, 2] = 1
Arr, Arc, Acc = structure_tensor(square, sigma=0.1, order='rc')
print(Acc)




