# 计算Hessian矩阵的特征值

from skimage.feature import hessian_matrix, hessian_matrix_eigvals
import numpy as np
square = np.zeros((5, 5))
square[2, 2] = 4
H_elems = hessian_matrix(square, sigma=0.1, order='rc')
print(hessian_matrix_eigvals(H_elems)[0])




