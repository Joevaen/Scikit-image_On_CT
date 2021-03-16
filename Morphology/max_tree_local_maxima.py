# 确定图像的所有局部最大值。
#
# 局部最大值定义为像素连接的像素集合，这些像素集合的灰度级严格大于该组直接邻域中所有像素的灰度级。 该函数标记局部最大值。
#
# 从技术上讲，该实现基于图像的最大树表示。 如果已经计算了最大树表示，该函数将非常有效。 否则，最好使用函数local_maxima。