# DAISY局部图像描述符基于梯度方向直方图
# http://cvlab.epfl.ch/software/daisy
# 没怎么看懂这个算法干什么的

from skimage.feature import daisy
from skimage import data, img_as_float, io
import matplotlib.pyplot as plt


img = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))

descs, descs_img = daisy(img, step=180, radius=58, rings=2, histograms=6,
                         orientations=8, visualize=True)

fig, ax = plt.subplots()
ax.axis('off')
ax.imshow(descs_img)
descs_num = descs.shape[0] * descs.shape[1]
ax.set_title('%i DAISY descriptors extracted:' % descs_num)
plt.show()