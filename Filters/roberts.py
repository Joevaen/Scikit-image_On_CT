# 使用罗伯茨的交叉算子找到边缘
from skimage.filters import roberts
from skimage import io, img_as_float
from skimage.morphology import disk
from skimage.color import rgb2gray

image = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg')
# image = rgb2gray(image)
io.imshow(image)
io.show()

md = roberts(image)
io.imshow(md)
io.show()


