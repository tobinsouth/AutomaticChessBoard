
import numpy as np
import cv2
import heapq

# video_capture = cv2.VideoCapture(1)
video_capture = cv2.VideoCapture(500)
h=50

video_capture.set(3,640)
video_capture.set(4,480)
ret, frame = video_capture.read()
cv2.imshow("Image", frame)
saved = np.zeros((8,8))

while True:
    ret, frame = video_capture.read()
    save  =  frame;
    BlueMat = np.zeros((8,8))
    GreenMat = np.zeros((8,8))
    RedMat = np.zeros((8,8))

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    all_lower=np.array([0,100,0],np.uint8)
    all_upper=np.array([40,255,150],np.uint8)
    white_lower=np.array([0,100,75],np.uint8)
    white_upper=np.array([40,255,250],np.uint8)
    stickers_lower=np.array([100,0,0],np.uint8)
    stickers_upper=np.array([140,255,255],np.uint8)
    frame_all = cv2.inRange(hsv_img, all_lower, all_upper)
    frame_white = cv2.inRange(hsv_img, white_lower, white_upper)
    frame_stickers = cv2.inRange(hsv_img, stickers_lower, stickers_upper)
    #ret,thresh = cv2.threshold(frame_threshed,127,255,cv2.THRESH_TOZERO)
    #ret,thresh = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)
    
    # contours, hierarchy = cv2.findContours(frame_stickers,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#     if len(contours)>0:
# 		# Find the index of the largest contour
#         areas = [cv2.contourArea(c) for c in contours]
# #		[a b c d] = np.argmax(areas)
# #		cnt=contours[max_index]
#         list_large =  heapq.nlargest(4,areas)
#         for each in list_large:
#             cnt=contours[areas==each]
#             x,y,w,h = cv2.boundingRect(cnt)
#             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
#    i = 0;
            

    
		
		
#    
#    for x in range(80,480,50):
#        j=0
#        for y in range(30,420,50):     
#            cv2.rectangle(frame, (x, y), (x+h, y+h), (0, 255, 0), 2)
#            BlueMat[i,j] = sum(sum(frame[x:x+h,y:y+h][1]))
#            GreenMat[i,j] = sum(sum(frame[x:x+h,y:y+h][2]))
#            RedMat[i,j] = sum(sum(frame[x:x+h,y:y+h][3]))
#            j=j+1
#        i=i+1
         
    
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        diff = abs(saved - GreenMat)
        print GreenMat/BlueMat, '\n'
        saved = GreenMat
        
    cv2.imshow("Image", frame_all)
        


    if cv2.waitKey(1) & 0xFF == ord('q'):
		break
    
video_capture.release()
cv2.destroyAllWindows()

