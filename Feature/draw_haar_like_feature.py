# 哈尔特征 https://zh.wikipedia.org/wiki/%E5%93%88%E5%B0%94%E7%89%B9%E5%BE%81
import numpy as np
from skimage.feature import haar_like_feature_coord
from skimage.feature import draw_haar_like_feature
feature_coord, _ = haar_like_feature_coord(2, 2, 'type-4')
image = draw_haar_like_feature(np.zeros((2, 2)),
                               0, 0, 2, 2,
                               feature_coord,
                               max_n_features=1)
print(image)




