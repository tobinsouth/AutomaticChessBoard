import numpy as np
import cv2
# import Chess_Reset as reseter
import Chess_Serial as serial

camera = 0


def click(event, x, y, flags, param):
    """ Detects when a click happens and draws on image"""
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates

    if event == cv2.EVENT_LBUTTONDOWN:
        cv_points.append((x, y))
        cv2.circle(cv_frame, (x, y), 3, (0, 255, 0), -1)
        cv2.imshow("Image", cv_frame)


def setup():
    """ Finds the four corner points on board """
    video_capture = cv2.VideoCapture(camera)
    global cv_points, cv_frame

    cv_points = []
    cv2.namedWindow('Image')

    cv2.setMouseCallback("Image", click)

    video_capture.set(3, 640)
    video_capture.set(4, 480)
    ret, cv_frame = video_capture.read()

    for i in range(1, 10):
        ret, cv_frame = video_capture.read()

    cv2.imshow("Image", cv_frame)

    if cv2.waitKey(0) & 0xFF == ord(' '):
        video_capture.release()
        cv2.destroyAllWindows()
        return cv_points


############################ Old setup ################################
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

###################   Deceted Piece #####(The hard part) ##################

def findPeice(subframe):
    """
    :param subframe: the section of of board image
    :return: the likelyhood of being a white piece

    """
    hsv_subframe = cv2.cvtColor(subframe, cv2.COLOR_BGR2HSV)
    #    hsv_subframe = subframe
    #    cv2.imshow("Image", subframe)

    hsv_subframe_crop = hsv_subframe[12:-12, 12:-12]
    white_lower = np.array([0, 34, 87], np.uint8)
    white_upper = np.array([47, 172, 156], np.uint8)
    frame_white = cv2.inRange(hsv_subframe, white_lower, white_upper)
    whiteness = (sum(sum(frame_white)))

    #    plt.hist(hsv_subframe.ravel(),256,[0,256]); plt.show())
    #    color = ('b','g','r')
    #    for i,col in enumerate(color):
    #        histr = cv2.calcHist([hsv_subframe],[i],None,[256],[0,256])
    #        plt.plot(histr,color = col)
    #        plt.xlim([0,256])
    #    plt.show()


    #    cv2.waitKey(0) & 0xFF == ord('\x1b')

    #    if whiteness > 1700:
    #        return 1
    #    else:
    #        return 0
    return whiteness


def largest_indices(ary, n):
    """Returns the n largest indices from a numpy array."""
    flat = ary.flatten()
    indices = np.argpartition(flat, -n)[-n:]
    indices = indices[np.argsort(-flat[indices])]
    return np.unravel_index(indices, ary.shape)


def openCV(a, b, c, d, number_of_pieces, current_fen):
    [x, y] = min([a, b, c, d], key=sum)
    [x_b, y_b] = max([a, b, c, d], key=sum)
    w = x_b - x
    h = y_b - y

    [nah1, temp1, temp2, nah2] = sorted([a, b, c, d], key=sum)
    top_right = max(temp1, temp2)
    bot_left = min(temp1, temp2)
    pts_old = np.float32([[x, y], top_right, bot_left, [x_b, y_b]])
    pts_new = np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])

    M = cv2.getPerspectiveTransform(pts_old, pts_new)

    video_capture = cv2.VideoCapture(camera)
    video_capture.set(3, 640)
    video_capture.set(4, 480)
    counter = 0

    first_frame = True
    cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Image', 1000, 1000)

    while True:
        ret, frame = video_capture.read()
        # frame = cv2.imread('1.png')

        save = frame.copy()

        frame = cv2.warpPerspective(frame, M, (400, 400))

        save_warp = frame.copy()

        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        Pieces = np.zeros((8, 8))
        final = np.zeros((8, 8))

        for i in range(0, 8):
            for j in range(0, 8):
                xpos_1 = i * 50
                xpos_2 = (i + 1) * 50
                ypos_1 = j * 50
                ypos_2 = (j + 1) * 50

                cv2.rectangle(frame, (xpos_1, ypos_1), (xpos_2, ypos_2), (0, 200, 0), 2)
                subframe = save_warp[ypos_1:ypos_2, xpos_1:xpos_2]

                Pieces[7 - i, 7 - j] = findPeice(subframe.copy())
            #                print(Pieces[7-i,7-j])
            #

        if first_frame == True:
            average = Pieces
        else:
            average = (average * 0.75 + Pieces * 0.25) / 2

        Pieces = average
        bestguess = Pieces.max()

        for i in range(0, 8):
            for j in range(0, 8):
                xpos_1 = i * 50
                xpos_2 = (i + 1) * 50
                ypos_1 = j * 50
                ypos_2 = (j + 1) * 50
                if Pieces[7 - i, 7 - j] in Pieces[largest_indices(Pieces, number_of_pieces)]:
                    cv2.rectangle(frame, (xpos_1 + 15, ypos_1 + 15), (xpos_2 - 15, ypos_2 - 15),
                                  (0,0,255 * Pieces[7 - i, 7 - j] / bestguess), -1)
                    final[7 - j, 7 - i] = 1

        cv2.imshow("Image", frame)

        # Control Calls Based on Key Press

        # Hit esc to return piece
        if cv2.waitKey(1) & 0xFF == ord(' '):
            video_capture.release()
            cv2.destroyAllWindows()
            return final

        # Hit q to quit and reset
        if cv2.waitKey(1) & 0xFF == ord('\x1b'):
            video_capture.release()
            cv2.destroyAllWindows()
            print(' Aborted. \n')
            try:
                serial.splitMove([[(0,0),(0,0)]])
            except:
                print('Failed to reset')
            return -1


# [a, b, c, d] = setup()
# [a, b, c, d] =[(65, 48), (387, 47), (71, 365), (385, 366)]
# 


# Out = openCV(a, b, c, d)
# print Out
