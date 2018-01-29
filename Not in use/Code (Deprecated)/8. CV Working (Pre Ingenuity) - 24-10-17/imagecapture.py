# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 22:25:32 2017

@author: Tobin South
"""

import cv2
video_capture = cv2.VideoCapture(0)

video_capture.set(3,640)
video_capture.set(4,480)
ret, frame = video_capture.read()
cv2.imshow("Image", frame)

while True:
    ret, frame = video_capture.read()
    save  =  frame
    
    #if cv2.waitKey(1) & 0xFF == ord('s'):
    cv2.imshow("Image", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()

