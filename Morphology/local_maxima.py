# 查找n维数组的局部最大值。
#
# 局部最大值定义为具有相等灰度级（平稳段）的像素连接集，这些像素组严格大于邻域中所有像素的灰度级。
from skimage import data, morphology, img_as_float, io
image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))
gamma_corrected = morphology.local_maxima(image, connectivity=100)
io.imshow(image)
io.show()

io.imshow(gamma_corrected)
io.show()