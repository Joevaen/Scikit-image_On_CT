# 查找n维数组的局部最小值。
#
# 局部极小值定义为具有相等灰度级（平稳段）的连接像素组，这些像素组严格小于邻域中所有像素的灰度级。
from skimage import data, morphology, img_as_float, io
image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))
gamma_corrected = morphology.local_minima(image)
io.imshow(image)
io.show()

io.imshow(gamma_corrected)
io.show()