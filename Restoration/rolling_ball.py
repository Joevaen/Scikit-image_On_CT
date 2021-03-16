# 通过滚动/移动内核来估计背景强度。
#
# 在不均匀曝光的情况下，此滚球算法可估算ndimage的背景强度。 它是常用滚动球算法的概括[1]。
import imageio
import matplotlib.pyplot as plt
import numpy as np

from skimage import (
    data, restoration, util
)


def plot_result(image, background):
    fig, ax = plt.subplots(nrows=1, ncols=3)

    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('Original image')
    ax[0].axis('off')

    ax[1].imshow(background, cmap='gray')
    ax[1].set_title('Background')
    ax[1].axis('off')

    ax[2].imshow(image - background, cmap='gray')
    ax[2].set_title('Result')
    ax[2].axis('off')

    fig.tight_layout()


image = data.coins()
from skimage import data, morphology, img_as_float, io
image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))
# gamma_corrected = morphology.area_closing(image)


background = restoration.rolling_ball(image)

plot_result(image, background)
plt.show()

image = data.page()
image_inverted = util.invert(image)

background_inverted = restoration.rolling_ball(image_inverted, radius=45)
filtered_image_inverted = image_inverted - background_inverted
filtered_image = util.invert(filtered_image_inverted)
background = util.invert(background_inverted)

fig, ax = plt.subplots(nrows=1, ncols=3)

ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original image')
ax[0].axis('off')

ax[1].imshow(background, cmap='gray')
ax[1].set_title('Background')
ax[1].axis('off')

ax[2].imshow(filtered_image, cmap='gray')
ax[2].set_title('Result')
ax[2].axis('off')

fig.tight_layout()

plt.show()