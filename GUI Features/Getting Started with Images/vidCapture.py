import numpy as np
import cv2

# create default VideoCapture
cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
	cap.open()

print('[INFO] Camera On.')

# define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame core
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	

	# write frame to file
	out.write(frame)

	# Display the resulting frame
	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
out.release()

print('[INFO] Camera Off.')
cv2.destroyAllWindows()	
