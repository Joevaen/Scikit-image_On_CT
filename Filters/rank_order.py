# 用于生成一个数组的对应的索引数组
from skimage.filters import rank_order
from skimage import io, img_as_float
from skimage.morphology import disk
from skimage.color import rgb2gray

image = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg')
image = rgb2gray(image)
io.imshow(image)
io.show()

md = rank_order(image)
print(md)


