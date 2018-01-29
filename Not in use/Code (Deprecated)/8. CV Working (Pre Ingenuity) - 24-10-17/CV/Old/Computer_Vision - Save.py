
import numpy as np
import cv2
video_capture = cv2.VideoCapture(1)
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
    
    
    
    i = 0;
    
    for x in range(80,480,50):
        j=0
        for y in range(30,420,50):     
            cv2.rectangle(frame, (x, y), (x+h, y+h), (0, 255, 0), 2)
            BlueMat[i,j] = sum(sum(frame[x:x+h,y:y+h][1]))
            GreenMat[i,j] = sum(sum(frame[x:x+h,y:y+h][2]))
            RedMat[i,j] = sum(sum(frame[x:x+h,y:y+h][3]))
            j=j+1
        i=i+1
            
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        diff = abs(saved - GreenMat)
        print GreenMat/BlueMat, '\n'
        saved = GreenMat
        
    cv2.imshow("Image", frame)
        


    if cv2.waitKey(1) & 0xFF == ord('q'):
		break
    
video_capture.release()
cv2.destroyAllWindows()

