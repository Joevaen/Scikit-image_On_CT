from skimage import data,io
from skimage.filters import threshold_niblack
image = data.page()
threshold_image = threshold_niblack(image, window_size=7, k=0.1)
io.imshow(threshold_image)
io.show()