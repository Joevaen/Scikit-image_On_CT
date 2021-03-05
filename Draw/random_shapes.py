# 生成具有随机形状的图像，并用边框标记。
import skimage.draw
image, labels = skimage.draw.random_shapes((32, 32), max_shapes=3)
print(image)
print(labels)

