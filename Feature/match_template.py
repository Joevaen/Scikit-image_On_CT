# 适用于2d和3d的模板匹配方法
# 输出是一个值在-1.0到1.0之间的数组。 给定位置的值对应于图像和模板之间的相关系数。
# 对于pad_input = True，匹配项对应于模板的中心，否则对应于模板的左上角。 为了找到最佳匹配，您必须在响应（输出）图像中搜索峰值。

import numpy as np
from skimage.feature import match_template
template = np.zeros((3, 3))
template[1, 1] = 1
print(template)



image = np.zeros((6, 6))
image[1, 1] = 1
image[4, 4] = -1
print(image)






result = match_template(image, template)
np.round(result, 3)
print(result)




result = match_template(image, template, pad_input=True)
np.round(result, 3)
print(result)




