# 使用罗伯茨的交叉算子找到边缘
#  0   1
# -1   0
from skimage.filters import roberts_neg_diag
from skimage import io, img_as_float
from skimage.morphology import disk
from skimage.color import rgb2gray

image = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg')
# image = rgb2gray(image)
io.imshow(image)
io.show()

md = roberts_neg_diag(image)
io.imshow(md)
io.show()


