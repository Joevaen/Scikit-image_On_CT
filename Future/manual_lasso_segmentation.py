# 根据鼠标选择的自由格式返回标签图像。
from skimage import data, future, io
camera = data.camera()
mask = future.manual_lasso_segmentation(camera)
io.imshow(mask)
io.show()