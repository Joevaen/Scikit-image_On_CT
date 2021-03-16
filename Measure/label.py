import numpy as np
from skimage.measure import label
x = np.eye(3).astype(int)
print(x)



print(label(x, connectivity=1))



print(label(x, connectivity=2))



print(label(x, background=1))



x = np.array([[1, 0, 0],
              [1, 1, 5],
              [0, 0, 0]])
print(label(x))


