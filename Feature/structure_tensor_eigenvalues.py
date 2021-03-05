# 计算结构张量的特征值。

from skimage.feature import structure_tensor
from skimage.feature import structure_tensor_eigenvalues
import numpy as np
square = np.zeros((5, 5))
square[2, 2] = 1
A_elems = structure_tensor(square, sigma=0.1, order='rc')
print(structure_tensor_eigenvalues(A_elems)[0])




