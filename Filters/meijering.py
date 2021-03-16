#　使用Meijering神经突过滤器过滤图像。

# 该过滤器可用于检测连续的脊，例如 神经突，皱纹，河流。 它可用于计算包含此类对象的整个图像的比例。

# 中值滤波
from skimage.filters import meijering
from skimage import io, img_as_float
from skimage.morphology import disk

image = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg')

io.imshow(image)
io.show()

md = meijering(image)
io.imshow(md)
io.show()



