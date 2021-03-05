# 调整图像，使其累积直方图与另一幅图像相匹配，各个通道独立匹配。
import matplotlib.pyplot as plt

from skimage import data, img_as_float, io
from skimage import exposure
from skimage.exposure import match_histograms

reference = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/9.jpg')

image = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg')


matched = match_histograms(image, reference, multichannel=True)

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
                                    sharex=True, sharey=True)
for aa in (ax1, ax2, ax3):
    aa.set_axis_off()

ax1.imshow(image)
ax1.set_title('Source')
ax2.imshow(reference)
ax2.set_title('Reference')
ax3.imshow(matched)
ax3.set_title('Matched')

plt.tight_layout()
plt.show()