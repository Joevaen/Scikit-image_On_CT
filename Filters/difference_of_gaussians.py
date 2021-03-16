# 高斯差算子，DoG算子
# https://zh.wikipedia.org/wiki/%E9%AB%98%E6%96%AF%E5%B7%AE
from skimage.data import astronaut
from skimage.filters import difference_of_gaussians
from skimage import io, img_as_float

image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg'))

filtered_image = difference_of_gaussians(image, 2, 10,
                                         multichannel=True)
io.imshow(filtered_image)
io.show()

filtered_image = difference_of_gaussians(image, 2,
                                         multichannel=True)
io.imshow(filtered_image)
io.show()

filtered_image = difference_of_gaussians(image, (2,5), (3,20))
io.imshow(filtered_image)
io.show()
