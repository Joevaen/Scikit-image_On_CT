# CENSURE关键点检测器。
from skimage.data import astronaut
from skimage.color import rgb2gray
from skimage.feature import CENSURE
from skimage import io, img_as_float
im = io.imread('/home/qiao/PythonProjects/Scikit-image_On_CT/Test_Img/4.jpg')
img = rgb2gray(im)
censure = CENSURE()
censure.detect(img)
print(censure.keypoints)

print(censure.scales)

