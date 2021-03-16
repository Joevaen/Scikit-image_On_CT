# 执行图像的直径打开。
#
# 直径开口会移除图像的所有明亮结构，且最大扩展范围小于直径阈值。 最大扩展定义为边界框的最大扩展。 该运算符也称为边界框打开。 在实践中，结果类似于形态学上的开口，但是长而薄的结构并没有被去除。
#
# 从技术上讲，此运算符基于图像的最大树表示。
from skimage import data, morphology, img_as_float, io
image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))
gamma_corrected = morphology.diameter_opening(image, 50)
io.imshow(image)
io.show()

io.imshow(gamma_corrected)
io.show()