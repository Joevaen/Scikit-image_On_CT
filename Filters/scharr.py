# 使用Scharr变换找到边缘幅度。相比其他方法有更好的旋转不变性

from skimage.filters import scharr, scharr_h, scharr_v
from skimage import io, img_as_float
from skimage.morphology import disk
from skimage.color import rgb2gray

image = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg')
# image = rgb2gray(image)
io.imshow(image)
io.show()

md = scharr(image)
io.imshow(md)
io.show()

md = scharr_h(image)
io.imshow(md)
io.show()

md = scharr_v(image)
io.imshow(md)
io.show()
