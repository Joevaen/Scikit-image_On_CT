# 开操作会把白色的点像素值去掉
from skimage import data, morphology, img_as_float, io
image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))
gamma_corrected = morphology.area_opening(image)
io.imshow(image)
io.show()

io.imshow(gamma_corrected)
io.show()