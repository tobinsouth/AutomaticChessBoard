import numpy as np
import cv2


# Initialise video
video_capture = cv2.VideoCapture(1)
video_capture.set(3,640)
video_capture.set(4,480)

while True:
	# Gets frames
    ret, frame = video_capture.read()
#    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#    blue_lower=np.array([100,200,100],np.uint8)
#    blue_upper=np.array([140,255,255],np.uint8)
#    frame_threshed = cv2.inRange(hsv_img, blue_lower, blue_upper)
#    imgray = frame_threshed
#    ret,thresh = cv2.threshold(frame_threshed,127,255,0)
#    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#    if len(contours)>0:
#		# Find the index of the largest contour
#        areas = [cv2.contourArea(c) for c in contours]
#        max_index = np.argmax(areas)
#        cnt=contours[max_index]
#
#        x,y,w,h = cv2.boundingRect(cnt)
#        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
#	# cv2.imshow("Show",frame)	
##	 crop_img = frame[y:y+h, x:x+w]
##	 cv2.imshow("Image", crop_img)
    cv2.imshow('Video', frame)

#	Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()