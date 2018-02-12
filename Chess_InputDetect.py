import Chess_Serial as serial
# import Chess_Reset as reseter

import numpy
import re
import cv2
from torch.autograd import Variable
import torch
from torchvision import transforms
import torch.nn as nn
import torch.nn.functional as F
import chess.uci
import chess


camera = 0


def click(event, x, y, flags, param):
    """ Detects when a click happens and draws on image"""

    if event == cv2.EVENT_LBUTTONDOWN:
        cv_points.append((x, y))
        cv2.circle(cv_frame, (x, y), 3, (0, 255, 0), -1)
        cv2.imshow("Image", cv_frame)


def setup():
    """ Finds the four corner points on board """

    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.conv1 = nn.Conv2d(3, 6, 5)
            self.pool = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(6, 16, 5)
            self.fc1 = nn.Linear(16 * 9 * 9, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 1)

        def forward(self, x):
            x = x.unsqueeze(0)
            x = self.conv1(x)
            x = self.pool(F.relu(x))
            x = self.pool(F.relu(self.conv2(x)))
            x = x.view(-1, 16 * 9 * 9)
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x

    net = torch.load('TrainedNetworkWithMoarData.rip')

    this_transform = transforms.Compose(
            [transforms.ToPILImage(), transforms.ToTensor(),
             transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    # Non neural network stuff

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
        return cv_points , net, this_transform


def find_move(board,image):
    """ Returns the move made, returns -1 if move is illegal or no move is made """

    board = board.split(' ', 1)[0]  # Converts fen board to pathable matrix

    def r(o):
        return (''.join(['0' * int(h) if h.isdigit()else'\n' if h == '/' else h for h in o]))  # Converts fen to a map

    board = r(board)
    board = re.sub('([a-z]{1})', '0', board)
    board = re.sub('([A-Z]{1})', '1', board)
    board = numpy.array([list(i) for i in board.splitlines()])
    board = numpy.array([[int(x) for x in i] for i in board])
    change = board - image

    nonzero = numpy.nonzero(change)

    if len(nonzero[1]) > 2:
        startSquare = 'e1'
        if nonzero[1][0] == 4:
            endSquare = 'g1'
            print('Castle - Kingside')
        else:
            endSquare = 'c1'
            print('Castle - Queenside')
    else:
        start = numpy.argmax(change)
        start = [start // 8, start % 8]
        startSquare = str(chr(start[1] + 97)) + str(7 - start[0] + 1)

        end = numpy.argmin(change)
        end = [end // 8, end % 8]
        endSquare = str(chr(end[1] + 97)) + str(7 - end[0] + 1)

    move = startSquare + endSquare

    if chess.Move.from_uci(move) in board.legal_moves: ###### Need to deal with game ending
        return move
    elif move == 'end' or move == 'End':
        print("This is legacy please fix")
        return -1
    else:
        return -1


def get_board_from_camera(frame):
    """ Uses Neural Network to detect what squares are white or not white """

    board_guess = np.zeros((8, 8))

    for i in range(0, 8):
        for j in range(0, 8):
            xpos_1 = i * 50
            xpos_2 = (i + 1) * 50
            ypos_1 = j * 50
            ypos_2 = (j + 1) * 50

            subframe = save_warp[ypos_1:ypos_2, xpos_1:xpos_2]
            subframe = cv2.cvtColor(subframe, cv2.COLOR_BGR2RGB)

            output = net(Variable(this_transform(subframe)))

            if output.data[0].cpu().numpy()[0] > 0.5:
                board_guess[7 - i, 7 - j] = 1
            else:
                board_guess[7 - i, 7 - j] = 0

    return board_guess


def prettify_frame(board_guess, frame):
    """ Make the frame pretty by drawing sub squares and colours the white peices"""
    for i in range(0, 8):
        for j in range(0, 8):
            xpos_1 = i * 50
            xpos_2 = (i + 1) * 50
            ypos_1 = j * 50
            ypos_2 = (j + 1) * 50

            if board_guess[7 - i, 7 - j] == 1:
                cv2.rectangle(frame, (xpos_1, ypos_1), (xpos_2, ypos_2), (0, 0, 255), 2)
            elif board_guess[7 - i, 7 - j] == 0:
                cv2.rectangle(frame, (xpos_1, ypos_1), (xpos_2, ypos_2), (0, 200, 0), 2)

    return frame


def get_user_input(board,arena, net, this_transform):
    """ Uses camera to detect current state of board every 1 second, if legal new board, returns move"""

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

    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Image', 1000, 1000)

    counter = 0
    while True:
        ret, frame = video_capture.read()

        frame = cv2.warpPerspective(frame, M, (400, 400))  # Warp frame to board

        counter+=1
        if counter % 20 == 1:  # Only do the hard work every 20 cycles

            board_guess = get_board_from_camera(frame.copy())  # Use nn to guess the state of the board

            move = find_move(board,board_guess)  # Finds move and checks if legal

            if not move == -1:  # Return move if it was legal
                return move

        frame = prettify_frame(board_guess, frame)  # Colour frame by what piece is where

        cv2.imshow("Image", frame)  # Display frame

        # Control Calls Based on Key Press
        # Hit esc to return piece
        if cv2.waitKey(1) & 0xFF == ord(' '):
            video_capture.release()
            cv2.destroyAllWindows()
            return np.transpose(Pieces)

        # Hit q to quit and reset
        if cv2.waitKey(1) & 0xFF == ord('\x1b'):
            video_capture.release()
            cv2.destroyAllWindows()
            print(' Aborted. \n')
            try:
                serial.splitMove([[(0, 0), (0, 0)]])
            except:
                print('Failed to reset')
            return -1

