# 使用双边滤波器对图像进行降噪。
from skimage import data, img_as_float, io
import numpy as np
from skimage.restoration import denoise_bilateral
astro = img_as_float(data.astronaut())
astro = astro[220:300, 220:320]
noisy = astro + 0.6 * astro.std() * np.random.random(astro.shape)
noisy = np.clip(noisy, 0, 1)
denoise = denoise_bilateral(noisy, sigma_color=0.05, sigma_spatial=15,
                             multichannel=True)
# io.imshow(astro)
# io.show()
io.imshow(denoise)
io.show()