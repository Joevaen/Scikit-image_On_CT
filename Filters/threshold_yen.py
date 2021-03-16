# 根据yen的方法返回阈值
from skimage import data,io
from skimage.filters import threshold_yen
image = data.page()
thresh = threshold_yen(image)
binary = image <= thresh
print(binary)