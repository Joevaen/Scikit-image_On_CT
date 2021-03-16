# 将实数和虚数响应返回给Gabor滤波器。
#
# 将Gabor滤波器内核的实部和虚部应用于图像，并将响应作为一对数组返回。
#
# Gabor滤波器是具有高斯核的线性滤波器，它由正弦平面波调制。 Gabor滤波器的频率和方向表示类似于人类视觉系统。
# Gabor滤波器组通常用于计算机视觉和图像处理。 它们特别适合于边缘检测和纹理分类。


from skimage.filters import gabor
from skimage import io, img_as_float

image = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg')

filtered_image, _ = gabor(image, 0.6)

io.imshow(filtered_image)
io.show()