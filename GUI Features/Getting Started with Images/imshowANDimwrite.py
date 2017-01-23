import numpy as np
import cv2

# load an image
img = cv2.imread("index.jpeg", cv2.IMREAD_GRAYSCALE)

# display the image
cv2.imshow("image", img)

k = cv2.waitKey(0)
if k == 27:	# wait for ESC key to exit
	cv2.destroyAllWindows()
elif k == ord('s'):	# wait for 's' key to save and exit
	print("[INFO] Saving the image")
	cv2.imwrite('save.png', img)
	cv2.destroyAllWindows()
