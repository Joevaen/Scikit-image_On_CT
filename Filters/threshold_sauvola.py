# 将Sauvola局部阈值应用于阵列。 Sauvola是Niblack技术的改良版。
from skimage import data,io
from skimage.filters import threshold_sauvola
image = data.page()
threshold_image = threshold_sauvola(image, window_size=7, k=0.1)
io.imshow(threshold_image)
io.show()