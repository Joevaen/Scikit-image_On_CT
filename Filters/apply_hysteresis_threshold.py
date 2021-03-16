# 对图像执行滞后阈值操作,在边缘检测和阈值分割之后再进行的对边缘进行细化的操作。
# 图像上的灰度值>=High分割的RegionsOut（“secure” points）直接作为结果输出；
# 相反，如果灰度值<Low分割的RegionsLow被直接舍弃；
# 灰度值介于两者之间，对于分割后的每个Region（“potential” ），如果与RegionsOut的距离小于MaxLength 值，那么这个region就被当做RegionsOut一起输出，也就是说最初分割的RegionsOut会影响最终的输出结果。
# 原文链接：https://blog.csdn.net/qq_18620653/article/details/105467210
import numpy as np
from skimage import io, img_as_float
from skimage.filters import apply_hysteresis_threshold, sobel
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

image = np.array([1, 2, 3, 2, 1, 2, 1, 3, 2])
print(apply_hysteresis_threshold(image, 1.5, 2.5).astype(int))

fig, ax = plt.subplots(nrows=2, ncols=2)

image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg'))
edges = sobel(image)

low = 0.1
high = 0.35

lowt = (edges > low).astype(int)
hight = (edges > high).astype(int)
hyst = apply_hysteresis_threshold(edges, low, high)

ax[0, 0].imshow(image, cmap='gray')
ax[0, 0].set_title('Original image')

ax[0, 1].imshow(edges, cmap='magma')
ax[0, 1].set_title('Sobel edges')

ax[1, 0].imshow(lowt, cmap='magma')
ax[1, 0].set_title('Low threshold')

ax[1, 1].imshow(hight + hyst, cmap='magma')
ax[1, 1].set_title('Hysteresis threshold')

for a in ax.ravel():
    a.axis('off')

plt.tight_layout()

plt.show()



