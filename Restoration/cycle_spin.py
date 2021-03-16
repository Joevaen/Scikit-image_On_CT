# 循环旋转（将func反复应用于x的移位版本）
import skimage.data
from skimage import img_as_float, io
import numpy as np
from skimage.restoration import denoise_wavelet, cycle_spin
img = img_as_float(skimage.data.camera())
sigma = 0.1
img = img + sigma * np.random.standard_normal(img.shape)
denoised = cycle_spin(img, func=denoise_wavelet,
                      max_shifts=3)
io.imshow(img)
io.show()
io.imshow(denoised)