# http://support.stockfishchess.org/kb/advanced-topics/compiling-stockfish-on-mac-os-x
# https://github.com/zhelyabuzhsky/stockfish
# https://pypi.python.org/pypi/pystockfish/0.1.3
# http://support.stockfishchess.org/kb/advanced-topics/engine-parameters


import Chess_Movement as movement
import Chess_InputDetect as detect
import Chess_Serial as serial

import chess.uci
import chess
from time import sleep


# Helper Functions
move_notation = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7}

def get_start_pos(x):
    return int(move_notation[list(x)[0]] + int(list(x)[1])*8-8)

def reset():
    serial.splitMove([[(0, 0), (0, 0)]])
    return 1


# Establish AI

Black = chess.uci.popen_engine('./stockfish') #setup black side chess AI
Black.uci()
options2 = {"Skill Level" : 20}
Black.setoption(options2)
score = [0,0] 
count = 0
ncount = 0


# Setup

inProgress = True

board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

arena, net, this_transform = detect.setup()

global Graves
Graves = {
    'Black': [('e',(1,0)),('e',(2,0)),('e',(3,0)),('e',(4,0)),('e',(5,0)),('e',(6,0)),('e',(7,0)),('e',(8,0)),('e',(1,1)),('e',(2,1)),('e',(3,1)),('e',(4,1)),('e',(5,1)),('e',(6,1)),('e',(7,1)),('e',(8,1))],
    'White': [('e',(8,11)),('e',(7,11)),('e',(6,11)),('e',(5,11)),('e',(4,11)),('e',(3,11)),('e',(2,11)),('e',(1,11)),('e',(8,10)),('e',(7,10)),('e',(6,10)),('e',(5,10)),('e',(4,10)),('e',(3,10)),('e',(2,10)),('e',(1,10))]
    } # Note White peices are interred in the 'Black' Graves


while inProgress:	

    # White Turn / User Input

    fen=board.fen()

    m = detect.get_user_input(fen,arena, net, this_transform)

    board.push_uci(m)

    if board.is_game_over() == True:  # Check for win
        inProgress = False  
        print("White Won")
        reset()
        break
    else:
        print('White Move Made: ', m)

    # End White Turn

    sleep(2)

    # Black Turn / AI

    Black.position(board)

    fen1=board.fen()

    n = str(Black.go(movetime=1)[0])

    # chess.Move.from_uci(n)

    board.push_uci(n)

    fen2=board.fen()

    piece=str(board.piece_at(get_start_pos(n)))

    if board.is_game_over() == True:
        inProgress = False
        print("Black Won")
        score[1] = score[1] + 1
        movement.move(fen1, fen2, n[0:2], n[2:4],piece,'Black',Graves)
        reset()
        break
    else:
        print('Black Move Made: ', n)
        movement.move(fen1, fen2, n[0:2], n[2:4],piece,'Black',Graves)
        
    # End Black Turn

