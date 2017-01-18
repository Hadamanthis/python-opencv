import numpy as np
import cv2

# load an image
img = cv2.imread("index.jpeg", cv2.IMREAD_GRAYSCALE)

# save the image with 'save.png' name
cv2.imwrite("save.png", img)
