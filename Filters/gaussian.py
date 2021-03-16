# 多维高斯滤波器。
from skimage.filters import gaussian
from skimage import io, img_as_float

image = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg')

io.imshow(image)
io.show()

filtered_image = gaussian(image, 0.1)

io.imshow(filtered_image)
io.show()

filtered_image = gaussian(image, 0.6)

io.imshow(filtered_image)
io.show()