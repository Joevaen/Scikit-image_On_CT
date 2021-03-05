# 求一个三维的椭圆体的表面积和体积
import numpy as np
from skimage.draw import ellipsoid, ellipsoid_stats
spacing = (1., 10 / 6., 16 / 6.)
ellipsoid_anisotropic = ellipsoid(6, 10, 16, spacing=spacing, levelset=True)
print(ellipsoid_anisotropic)
print(ellipsoid_anisotropic.shape)
v, s = ellipsoid_stats(6, 10, 16)
print(v)
print(s)