import numpy as np
import cv2

# load an color image in grayscale
img = cv2.imread('index.jpeg', cv2.IMREAD_GRAYSCALE)

# show the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

