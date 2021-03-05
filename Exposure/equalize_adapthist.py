# 对比度受限的自适应直方图均衡化（CLAHE）。
from skimage import data, exposure, img_as_float, io
image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))
gamma_corrected = exposure.equalize_adapthist(image)
io.imshow(image)
io.show()

io.imshow(gamma_corrected)
io.show()

