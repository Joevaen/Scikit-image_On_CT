# 通过将函数func应用于局部块来对图像进行下采样。
#
# 例如，此功能对于最大池和均值池很有用。
from skimage.measure import block_reduce
import numpy as np
image = np.arange(3*3*4).reshape(3, 3, 4)
print(image)









block_reduce(image, block_size=(3, 3, 1), func=np.mean)

image_max1 = block_reduce(image, block_size=(1, 3, 4), func=np.max)
print(image_max1)



image_max2 = block_reduce(image, block_size=(3, 1, 4), func=np.max)
print(image_max2)


