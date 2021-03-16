# 在输入图像上执行Gamma校正。
from skimage import data, exposure, img_as_float, io
image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/41.jpg'))
gamma_corrected = exposure.adjust_gamma(image, 2)
io.imshow(image)
io.show()

io.imshow(gamma_corrected)
io.show()

