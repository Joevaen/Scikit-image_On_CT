# 返回给定大小和尺寸的n维窗口。
from skimage.filters import window
w = window('hann', (512, 512))
w = window(16, (256, 256, 35))
w = window(('tukey', 0.8), (100, 300))