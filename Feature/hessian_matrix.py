# 黑塞矩阵:通过将图像与高斯核的二阶导数在相应的r方向和c方向上进行卷积来计算。
from skimage.feature import hessian_matrix
import numpy as np
square = np.zeros((5, 5))
square[2, 2] = 4
Hrr, Hrc, Hcc = hessian_matrix(square, sigma=0.1, order='rc')
print(Hrc)




