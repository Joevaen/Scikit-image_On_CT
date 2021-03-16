# 返回两个输入分段的联接。
#
# S1和S2的连接点J定义为以下分割，其中且仅当两个体素在S1和S2中位于同一段中时，它们才在同一段中。
import numpy as np
from skimage.segmentation import join_segmentations
s1 = np.array([[0, 0, 1, 1],
               [0, 2, 1, 1],
               [2, 2, 2, 1]])
s2 = np.array([[0, 1, 1, 0],
               [0, 1, 1, 0],
               [0, 1, 1, 1]])
print(join_segmentations(s1, s2))


