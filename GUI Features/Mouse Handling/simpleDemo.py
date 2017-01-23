import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
	if (event == cv2.EVENT_LBUTTONDOWN):
		cv2.circle(img, (x, y), 100, (255, 0, 0), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Draw')
cv2.setMouseCallback('Draw', draw_circle)

while (True):
	cv2.imshow('Draw', img)
	if (cv2.waitKey(20) & 0xFF == 27):
		break

cv2.destroyAllWindows()
