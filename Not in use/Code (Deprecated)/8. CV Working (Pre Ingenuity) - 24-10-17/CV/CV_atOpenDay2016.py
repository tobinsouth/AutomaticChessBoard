#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 20:29:38 2017

@author: tobin.south
"""

import numpy as np
import cv2

camera = 0

def click(event, x, y, flags, param):
    	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv_points.append((x, y))
        cv2.circle(cv_frame, (x, y), 3, (0, 255, 0), -1)
        cv2.imshow("Image", cv_frame)

        
def setup(): 
#     video_capture = cv2.VideoCapture(camera)
     global cv_points, cv_frame
     
     cv_points =[]
     cv2.namedWindow('Image')
     
     cv2.setMouseCallback("Image", click)
     
#     video_capture.set(3,640)
#     video_capture.set(4,480)
#     ret, cv_frame = video_capture.read()
#         
#     
#     for i in range(1,25):
#         ret, cv_frame = video_capture.read()
     
     cv_frame = cv2.imread('1.png')
         

     cv2.imshow("Image", cv_frame) 
     
     
     if cv2.waitKey(0) & 0xFF == ord('\x1b'):
#         video_capture.release()
         cv2.destroyAllWindows()
         return cv_points
           

# =============================================================================
# def setup():
#     video_capture = cv2.VideoCapture(camera)
#     
#     cv2.namedWindow('Image')
#     
#     video_capture.set(3,640)
#     video_capture.set(4,480)
#     ret, frame = video_capture.read()
#     
#     green_edge_lower = np.array([81,30,20],np.uint8)
#     green_edge_upper = np.array([125,255,255],np.uint8)
#      
#     finder_bool = True
#     while finder_bool:        
#         ret, frame = video_capture.read()        
#         frame = frame[50:420,150:500]       
#         hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         frame_board= cv2.inRange(hsv_img, green_edge_lower, green_edge_upper)
#         save = frame_board.copy()
#         
# 
#         kernel = np.ones((5,5), np.uint8)
#         frame_board = cv2.erode(frame_board, kernel, iterations=3)
#     
#         frame_board = cv2.dilate(frame_board, kernel, iterations=2)
#         
#         _,contours, hierarchy = cv2.findContours(frame_board,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#         if len(contours)>0:
#              		# Find the index of the largest contour
#             areas = [cv2.contourArea(c) for c in contours]
#             max_index = np.argmax(areas)
#             cnt=contours[max_index]
#             x,y,w,h = cv2.boundingRect(cnt)
#             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
#             corners= [[x+w,y],[x,y],[x+w,y+h],[x,y+h]]
#           
#         cv2.imshow("Image", frame) 
#     
#         if cv2.waitKey(1) & 0xFF == ord('S'):
#             video_capture.release()
#             cv2.destroyAllWindows()
#             return [x,y,w,h]
# =============================================================================

   
###################  Find Move ###############################

def openCV(x,y,w,h):
    
#    video_capture = cv2.VideoCapture(camera)
#    video_capture.set(3,640)
#    video_capture.set(4,480)
#    counter =0

    white_lower=np.array([0,34,87],np.uint8)
    white_upper=np.array([47,172,156],np.uint8)
    
    cv2.namedWindow('Image')
    

    
    while True:
#        ret, frame = video_capture.read()
        
        save = frame.copy()
        subframe = frame[50:420,150:520].copy()

        hsv_img_sub = cv2.cvtColor(subframe, cv2.COLOR_BGR2HSV)
        
#        frame_board= cv2.inRange(hsv_img_sub, green_edge_lower, green_edge_upper)
#        
#        
#        kernel = np.ones((10,10), np.uint8)
#        frame_board = cv2.dilate(frame_board, kernel, iterations=10)
#        
#        kernel = np.ones((5,5), np.uint8)
#        frame_board = cv2.erode(frame_board, kernel, iterations=5)
        
        frame_white = cv2.inRange(hsv_img_sub, white_lower, white_upper)
        

        Pieces = np.zeros((8,8))
        cv2.rectangle(subframe,(x,y),(x+w,y+h),(0,255,0),2)
    
        percent_arry = []
        for xpos in range(x,x+w-w/8,w/8):
            for ypos in range(y,y+h-h/8,h/8):
                cv2.rectangle(subframe,(xpos,ypos),(xpos+w/8,ypos+h/8),(0,255,0),2)
                square = frame_white[ypos:ypos+h/8,xpos:xpos+w/8]           
                percent = sum(sum(square))
                
                percent_arry.append(percent)
               
        # percent_arry = heapq.nlargest(16,percent_arry)
        percent_arry = [ z for z in percent_arry if z > 1000]
        i =0 
        for xpos in range(x,x+w-w/8,w/8):
            
            j =0
            for ypos in range(y,y+h-h/8,h/8): 
                square = frame_white[ypos:ypos+h/8,xpos:xpos+w/8]
                percent = sum(sum(square))  
                if percent in percent_arry:
                    Pieces[7-j,7-i] = 1
                    cv2.rectangle(subframe,(xpos,ypos),(xpos+w/8,ypos+h/8),(255,0,0),-1)
                j=j+1
            i=i+1
            
       
#        cv2.imshow("Image", frame_white) 

        
        if cv2.waitKey(1) & 0xFF == ord('\x1b'):                 
            video_capture.release()
            cv2.destroyAllWindows()
            print("Found Pieces")
            return Pieces
            	
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            video_capture.release()
            cv2.destroyAllWindows()
            print(' Aborted. \n')
            return -1
            
        cv2.imshow("Image", subframe)
            
 
# [x, y, w, h] = setup()

#Out = openCV(60, 37, 257, 305)
# print Out


    


