# 直方图均衡化
from skimage import data, exposure, img_as_float, io
image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))
gamma_corrected = exposure.equalize_hist(image)
io.imshow(image)
io.show()

io.imshow(gamma_corrected)
io.show()

