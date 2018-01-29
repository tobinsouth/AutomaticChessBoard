# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 02:21:15 2017

@author: Tobin South
"""


import numpy as np
import cv2
import heapq
from collections import Counter

video_capture = cv2.VideoCapture(1)
h=50

cv2.namedWindow('Image')

video_capture.set(3,640)
video_capture.set(4,480)
ret, frame = video_capture.read()
#cv2.imshow("Image", frame)


green_edge_lower = np.array([81,30,20],np.uint8)
green_edge_upper = np.array([125,255,255],np.uint8)

white_lower=np.array([0,34,87],np.uint8)
white_upper=np.array([47,172,156],np.uint8)
    
    
    

array_corners = [];
finder_bool = True
while finder_bool:
    
    ret, frame = video_capture.read()
    
       

    
    frame = frame[100:420,150:500]
    
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    

    

    frame_board= cv2.inRange(hsv_img, green_edge_lower, green_edge_upper)
    save = frame_board.copy()
    
    
    
    kernel = np.ones((5,5), np.uint8)
    frame_board = cv2.erode(frame_board, kernel, iterations=3)


    frame_board = cv2.dilate(frame_board, kernel, iterations=2)
    save_frame = frame_board.copy()
    
    contours, hierarchy = cv2.findContours(frame_board,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours)>0:
         		# Find the index of the largest contour
        areas = [cv2.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        cnt=contours[max_index]
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        corners= [[x+w,y],[x,y],[x+w,y+h],[x,y+h]]
        print w, " ", h, "\n"
#        rc = cv2.minAreaRect(contours[0])
#        box = cv2.boxPoints(rc)
#        for p in box:
#            pt = (p[0],p[1])
#            print pt
#            cv2.circle(frame,pt,5,(200,0,0),2)
#        array_corners.append(corners)
      
    cv2.imshow("Image", frame) 

    if cv2.waitKey(1) & 0xFF == ord('S'):
        video_capture.release()
        cv2.destroyAllWindows()
        break
  


while True:
    ret, frame = video_capture.read()
    
    
    save = frame.copy()
    subframe = frame[100:420,150:520].copy()

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv_img_sub = cv2.cvtColor(subframe, cv2.COLOR_BGR2HSV)
    
    
    frame_board= cv2.inRange(hsv_img_sub, green_edge_lower, green_edge_upper)
    
    
    kernel = np.ones((10,10), np.uint8)

    frame_board = cv2.dilate(frame_board, kernel, iterations=10)
    
    kernel = np.ones((5,5), np.uint8)
    
    frame_board = cv2.erode(frame_board, kernel, iterations=5)
    

    
    frame_white = cv2.inRange(hsv_img_sub, white_lower, white_upper)
    
    all_lower=np.array([0,100,0],np.uint8)
    all_upper=np.array([40,255,150],np.uint8)
    
    stickers_lower=np.array([140,200,255],np.uint8)
    stickers_upper=np.array([140,200,255],np.uint8)
    
    frame_all = cv2.inRange(hsv_img_sub, all_lower, all_upper)

    frame_stickers = cv2.inRange(hsv_img_sub, stickers_lower, stickers_upper)

#    kernel = np.ones((2,2),np.uint8)
#    frame_white = cv2.erode(frame_white,kernel,iterations = 2)
#    
#    contours, hierarchy = cv2.findContours(frame_board,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#    if len(contours)>0:
#         		# Find the index of the largest contour
#        areas = [cv2.contourArea(c) for c in contours]
#        max_index = np.argmax(areas)
#        cnt=contours[max_index]
#        x,y,w,h = cv2.boundingRect(cnt)
#        cv2.rectangle(subframe,(x,y),(x+w,y+h),(0,255,0),2)
#        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
#
#        corners= [[x+w,y],[x,y],[x+w,y+h],[x,y+h]]
##        rc = cv2.minAreaRect(contours[0])
##        box = cv2.boxPoints(rc)
    Pieces = np.zeros((8,8))
    cv2.rectangle(subframe,(x,y),(x+w,y+h),(0,255,0),2)

    percent_arry = []
    total = sum(sum(frame_white))
    for xpos in range(x,x+w-w/8,w/8):
        for ypos in range(y,y+h-h/8,h/8):
            cv2.rectangle(subframe,(xpos,ypos),(xpos+w/8,ypos+h/8),(0,255,0),2)
            square = frame_white[ypos:ypos+h/8,xpos:xpos+w/8]
#            hsv_square = cv2.cvtColor(square, cv2.COLOR_BGR2HSV)
#            square_white = cv2.inRange(hsv_square, white_lower, white_upper)            
            percent = sum(sum(square))
            
            percent_arry.append(percent)
           
#    percent_arry = heapq.nlargest(14,percent_arry)
    percent_arry = [ z for z in percent_arry if z > 1000]
    i =0 
    for xpos in range(x,x+w-w/8,w/8):
        
        j =0
        for ypos in range(y,y+h-h/8,h/8): 
            square = frame_white[ypos:ypos+h/8,xpos:xpos+w/8]
            percent = sum(sum(square))  
            print percent               
            if percent in percent_arry:
                Pieces[j,i] = 1
                cv2.rectangle(subframe,(xpos,ypos),(xpos+w/8,ypos+h/8),(255,0,0),-1)
                print "draw"
            j=j+1
        i=i+1
   
    
    

    
    
    
    #ret,thresh = cv2.threshold(frame_threshed,127,255,cv2.THRESH_TOZERO)
    #ret,thresh = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)
#    corners = []
#    contours, hierarchy = cv2.findContours(frame_board,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#    if len(contours)>0:
# 		# Find the index of the largest contour
#        areas = [cv2.contourArea(c) for c in contours]
# #		[a b c d] = np.argmax(areas)
# #		cnt=contours[max_index]
#        list_large =  heapq.nlargest(4,areas)
#        for each in list_large:
#            cnt=contours[areas.index(each)]
#            x,y,w,h = cv2.boundingRect(cnt)
#            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
##            corners.append([x+h/2,y+h/2])
#    else:
#        print "No green dots found"
#            
#    corners=  [[177, 103], [215, 375], [554, 87], [510, 382]]
    
    
#    contours, hierarchy = cv2.findContours(frame_board,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#    if len(contours)>0:
#         		# Find the index of the largest contour
#        areas = [cv2.contourArea(c) for c in contours]
#        max_index = np.argmax(areas)
#        cnt=contours[max_index]
#        x,y,w,h = cv2.boundingRect(cnt)
#        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
#        corners= [[x+w,y],[x,y],[x+w,y+h],[x,y+h]]
##        rc = cv2.minAreaRect(contours[0])
##        box = cv2.boxPoints(rc)
##        for p in box:
##            pt = (p[0],p[1])
##            print pt
##            cv2.circle(frame,pt,5,(200,0,0),2)


    cv2.imshow("Image", subframe)      
            
#    a = 600
#    b = 600
#    newcorn = np.float32(corners)
#    oldcorn = np.float32([[0,0],[a,0],[0,b],[a,b]])
#    M = cv2.getPerspectiveTransform(newcorn,oldcorn)
#    dst = cv2.warpPerspective(frame_all,M,(a,b)) 
#    cv2.imshow("Image", frame_board)

		
#    
#    for x in range(80,480,50):
#        j=0
#        for y in range(30,420,50):     
#            cv2.rectangle(frame, (x, y), (x+h, y+h), (0, 255, 0),
#            GreenMat[i,j] = sum(sum(frame[x:x+h,y:y+h][2]))
#            RedMat[i,j] = sum(sum(frame[x:x+h,y:y+h][3]))
#            j=j+1
#        i=i+1
         
    
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        diff = abs(saved - GreenMat)
        print GreenMat/BlueMat, '\n'
        saved = GreenMat
        
#    cv2.imshow("Image", frame)
        


    if cv2.waitKey(1) & 0xFF == ord('\x1b'):
		break
    
video_capture.release()
cv2.destroyAllWindows()

