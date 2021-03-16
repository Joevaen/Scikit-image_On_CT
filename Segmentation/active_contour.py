# 活动轮廓模型。
#
# 通过使蛇适合图像特征来激活轮廓。 支持单通道和多通道2D图像。 蛇可以是周期性的（用于分段），也可以具有固定和/或自由端。 输出蛇的长度与输入边界的长度相同。 由于点的数量是恒定的，因此请确保初始蛇具有足够的点以捕获最终轮廓的细节。
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour


# img = data.astronaut()
from skimage import data, morphology, img_as_float, io
img = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))
img = rgb2gray(img)

s = np.linspace(0, 2*np.pi, 400)
r = 315 + 50*np.sin(s)
c = 70 + 50*np.cos(s)
init = np.array([r, c]).T

snake = active_contour(gaussian(img, 3),
                       init, alpha=0.001, beta=10, gamma=0.001)

fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(img, cmap=plt.cm.gray)
ax.plot(init[:, 1], init[:, 0], '--r', lw=3)
ax.plot(snake[:, 1], snake[:, 0], '-b', lw=3)
ax.set_xticks([]), ax.set_yticks([])
ax.axis([0, img.shape[1], img.shape[0], 0])

plt.show()