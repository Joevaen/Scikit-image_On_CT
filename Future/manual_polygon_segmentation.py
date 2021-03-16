# 根据鼠标选择的多边形返回标签图像。
from skimage import data, future, io
camera = data.camera()
mask = future.manual_polygon_segmentation(camera)
io.imshow(mask)
io.show()
