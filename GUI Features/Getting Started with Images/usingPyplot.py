import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('index.jpeg', cv2.IMREAD_UNCHANGED)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img, cmap='gray', interpolation='bicubic')

plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis

plt.show()
