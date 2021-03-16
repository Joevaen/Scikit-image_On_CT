# 使用Farid变换找到边缘大小。
from skimage.filters import farid, farid_h, farid_v
from skimage import io, img_as_float

image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg'))

filtered_image = farid(image)

io.imshow(filtered_image)
io.show()

# farid_h找到图像的水平边缘
filtered_image = farid_h(image)

io.imshow(filtered_image)
io.show()

#farid_v找到图像的竖直边缘
filtered_image = farid_v(image)

io.imshow(filtered_image)
io.show()