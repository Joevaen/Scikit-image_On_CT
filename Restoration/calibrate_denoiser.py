# 校准降噪功能并返回最佳J不变版本。
#
# 返回的函数将通过设置最佳参数值（用于对输入图像进行降噪）进行部分评估。
from skimage import color, data, io
from skimage.restoration import denoise_wavelet, calibrate_denoiser
import numpy as np
img = color.rgb2gray(data.astronaut()[:50, :50])
noisy = img + 0.5 * img.std() * np.random.randn(*img.shape)
parameters = {'sigma': np.arange(0.1, 0.4, 0.02)}
denoising_function = calibrate_denoiser(noisy, denoise_wavelet,
                                        denoise_parameters=parameters)
denoised_img = denoising_function(img)
io.imshow(img)
io.show()
io.imshow(denoised_img)
io.show()
