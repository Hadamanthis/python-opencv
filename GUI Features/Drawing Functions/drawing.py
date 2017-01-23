import numpy as np
import cv2

# create black image
img = np.zeros((512, 512,3), np.uint8)

# draw a diagonal blue line with thickness of 5 px
img = cv2.line(img, (0,0), (511, 511), (255, 0, 0), 5)

# draw a green rectangle
img = cv2.rectangle(img, (128, 64), (192, 92), (0, 255, 0), 3)

# draw a circle
img = cv2.circle(img, (447,63), 63, (0, 0, 255), -1)

# draw an ellipse
img = cv2.ellipse(img, (100, 460), (100, 50), 0, 0, 180, (180, 90, 67), -1) 

# draw a polygon
pts = np.array([[10, 5], [50, 60], [120, 70], [70, 30]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 255, 255))

# add text to image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 400), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('drawing', img)

cv2.waitKey(0)
