# 确定高度> = h的图像的所有最大值。(先把局部的所有点用直面坐标系体现出来，然后再确定这个峰值高度)
#
# 局部最大值定义为具有相等灰度级的像素连接集，这些灰度级严格大于该集的直接邻域中所有像素的灰度级。
#
# 高度为h的局部最大值M是局部最大值，对于该局部最大值，至少有一条路径将M连接到具有相等或更高局部最大值的M上，其最小值为f（M）-h（即，沿路径的值不递减） 相对于最大值大于h），并且没有到达最小值更大或更大的相等或更高局部最大值的路径。
#
# 通过此功能还可以找到图像的全局最大值。
from skimage import data, morphology, img_as_float, io
image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))
gamma_corrected = morphology.h_maxima(image, 100)
io.imshow(image)
io.show()

io.imshow(gamma_corrected)
io.show()