# 对输入图像执行对数校正。
from skimage import data, exposure, img_as_float, io
image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))
gamma_corrected = exposure.adjust_log(image, 1)
io.imshow(image)
io.show()

io.imshow(gamma_corrected)
io.show()

