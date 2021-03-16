# 使用Sato分辨率过滤器过滤图像。
#
# 该过滤器可用于检测连续的脊，例如 管，皱纹，河流。 它可用于计算包含此类对象的整个图像的比例。

from skimage.filters import sato
from skimage import io, img_as_float
from skimage.morphology import disk
from skimage.color import rgb2gray

image = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg')
# image = rgb2gray(image)
io.imshow(image)
io.show()

md = sato(image)
io.imshow(md)
io.show()


