# 基于三角算法的返回阈值。
from skimage import data,io
from skimage.filters import threshold_triangle
image = data.page()
thresh = threshold_triangle(image)
binary = image > thresh
print(binary)