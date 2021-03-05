# 求一个三维的椭圆体
import numpy as np
from skimage.draw import ellipsoid
spacing = (1., 10 / 6., 16 / 6.)
ellipsoid_anisotropic = ellipsoid(6, 10, 16, spacing=spacing, levelset=True)
print(ellipsoid_anisotropic)
print(ellipsoid_anisotropic.shape)