# 中值滤波
from skimage.filters import median
from skimage import io, img_as_float
from skimage.morphology import disk

image = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg')

io.imshow(image)
io.show()

md = median(image, disk(5))
io.imshow(md)
io.show()



