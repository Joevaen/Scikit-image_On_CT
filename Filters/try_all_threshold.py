# 通过有一个ａｐｉ直接测试所有阈值分割的效果
from skimage.data import text
from skimage.filters import try_all_threshold
fig, ax = try_all_threshold(text(), figsize=(10, 6), verbose=False)