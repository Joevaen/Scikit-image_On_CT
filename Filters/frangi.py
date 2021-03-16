# 使用Frangi容器过滤器过滤图像。
#
# 该过滤器可用于检测连续的脊，例如 血管，皱纹，河流。 它可用于计算包含此类对象的整个图像的比例。
#
# 仅针对2D和3D图像定义。 根据[1]中所述的方法，计算Hessian的特征向量，以计算图像区域与血管的相似度。

from skimage.filters import frangi
from skimage import io, img_as_float

image = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg')

filtered_image = frangi(image)

io.imshow(filtered_image)
io.show()