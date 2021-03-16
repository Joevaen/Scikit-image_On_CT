# 使用Laplace运算符查找图像的边缘。
# 使用Hybrid Hessian filter过滤图像。
#
# 此过滤器可用于检测连续边缘，例如 血管，皱纹，河流。 它可用于计算包含此类对象的整个图像的比例。

# 多维高斯滤波器。
from skimage.filters import laplace
from skimage import io, img_as_float

image = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg')

io.imshow(image)
io.show()

filtered_image = laplace(image)

io.imshow(filtered_image)
io.show()

