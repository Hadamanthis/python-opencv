import cv2
import numpy as np

drawing = False    # True if mouse is pressed
size = 1 	   # Size of paint brush
r, g, b = 0, 0, 0  # Color of the paint

def nothing(x):
	pass

# mouse callback function
def draw(event, x, y, flags, param):
	global drawing

	if (event == cv2.EVENT_LBUTTONDOWN):
		drawing = True
	
	elif (event == cv2.EVENT_MOUSEMOVE):
		if (drawing == True):
			cv2.circle(img, (x, y), size, (b, g, r), -1)

	elif (event == cv2.EVENT_LBUTTONUP):
		drawing = False
	

# create black image
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Paint')

# create trackbars for color and size
cv2.createTrackbar('R', 'Paint', 0, 255, nothing)
cv2.createTrackbar('G', 'Paint', 0, 255, nothing)
cv2.createTrackbar('B', 'Paint', 0, 255, nothing)
cv2.createTrackbar('Size', 'Paint', 0, 10, nothing)

# put a listener on the mouse event
cv2.setMouseCallback('Paint', draw)

while (True):
	cv2.imshow('Paint', img)

	# updating size and color
	r = cv2.getTrackbarPos('R', 'Paint')
	g = cv2.getTrackbarPos('G', 'Paint')
	b = cv2.getTrackbarPos('B', 'Paint')
	size = cv2.getTrackbarPos('Size', 'Paint')

	k = cv2.waitKey(1) & 0xFF
	if (k == 27):
		break

cv2.destroyAllWindows()
