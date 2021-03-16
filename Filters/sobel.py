# 使用Sobel查找图像中的边缘。
from skimage.filters import sobel, sobel_h, sobel_v
from skimage import io, img_as_float
from skimage.morphology import disk
from skimage.color import rgb2gray

image = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg')
# image = rgb2gray(image)
io.imshow(image)
io.show()

md = sobel(image)
io.imshow(md)
io.show()

md = sobel_h(image)
io.imshow(md)
io.show()

md = sobel_v(image)
io.imshow(md)
io.show()


