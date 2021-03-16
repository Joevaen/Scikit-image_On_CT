# 返回复杂的二维Gabor滤波器内核。
#
# Gabor核是由复谐波函数调制的高斯核。 谐波函数由虚数正弦函数和实余弦函数组成。 空间频率与谐波的波长以及高斯核的标准偏差成反比。 带宽也与标准偏差成反比。

from skimage.filters import gabor_kernel
from skimage import io
from matplotlib import pyplot as plt

gk = gabor_kernel(frequency=0.2)
plt.figure()
io.imshow(gk.real)
io.show()

# more ripples (equivalent to increasing the size of the
# Gaussian spread)
gk = gabor_kernel(frequency=0.2, bandwidth=0.1)
plt.figure()
io.imshow(gk.real)
io.show()