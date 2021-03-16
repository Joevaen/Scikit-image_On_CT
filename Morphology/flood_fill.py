# 对图像执行洪水填充。
#
# 从特定的seed_point开始，找到等于或在种子值的公差范围内的连接点，然后将其设置为new_value。
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, filters, color, morphology, io, img_as_float
from skimage.segmentation import flood, flood_fill
cameraman = data.camera()
image = img_as_float(io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/10.jpg'))


# Change the cameraman's coat from dark to light (255).  The seed point is
# chosen as (155, 150)
light_coat = flood_fill(image, (255, 255), 255)
fig, ax = plt.subplots(ncols=2, figsize=(10, 5))

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].imshow(light_coat, cmap=plt.cm.gray)
ax[1].plot(150, 155, 'ro')  # seed point
ax[1].set_title('After flood fill')
ax[1].axis('off')

plt.show()

output = []

for i in range(8):
    tol = 5 + 20 * i
    output.append(flood_fill(image, (0, 0), 255, tolerance=tol))

# Initialize plot and place original image
fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(12, 12))
ax[0, 0].imshow(image, cmap=plt.cm.gray)
ax[0, 0].set_title('Original')
ax[0, 0].axis('off')

# Plot all eight different tolerances for comparison.
for i in range(8):
    m, n = np.unravel_index(i + 1, (3, 3))
    ax[m, n].imshow(output[i], cmap=plt.cm.gray)
    ax[m, n].set_title('Tolerance {0}'.format(str(5 + 20 * i)))
    ax[m, n].axis('off')
    ax[m, n].plot(0, 0, 'bo')  # seed point

fig.tight_layout()
plt.show()