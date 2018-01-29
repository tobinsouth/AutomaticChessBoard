 
# http://support.stockfishchess.org/kb/advanced-topics/compiling-stockfish-on-mac-os-x
# https://github.com/zhelyabuzhsky/stockfish
# https://pypi.python.org/pypi/pystockfish/0.1.3
# http://support.stockfishchess.org/kb/advanced-topics/engine-parameters

import chess.uci

import Chess_Movement as movement
import Chess_Serial as serial
import Chess_InputDetect as detect
import Computer_Vision as cv
from time import sleep
from IPython.display import display, SVG

restart = False
move_notation = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7}


def get_start_pos(x):
	return int(move_notation[list(x)[0]] + int(list(x)[1])*8-8)


def get_user_input(fen1,arena):
    for i in range(1,5):
        try:
            m = detect.detectMove(fen1,arena)
            print(m)
            if m == -1:
                return -1
            sleep(1)
            return m
            break
        except FileNotFoundError:
            print("Serial Error, plug it in")
        # except ValueError:
        #     print("get_user_input failed")


###### Establish AI #########
Black = chess.uci.popen_engine('./stockfish') #setup black side chess AI
Black.uci()
options2 = {"Skill Level" : 20}
Black.setoption(options2)
score = [0,0] 
count = 0
ncount = 0


################    Game    ################
inProgress = True

if restart:
    file = open('out.txt', 'r')
    board_txt = file.readlines()[-1]
    board = chess.Board(board_txt)  # "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    file.close()
else:
    open('out.txt', 'w').close() 
    
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1") # "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    # board = chess.Board("r3kbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
file = open('out.txt', 'a')

fen2=board.fen()
arena = cv.setup()

global Graves
Graves = {
    'Black': [('e',(1,0)),('e',(2,0)),('e',(3,0)),('e',(4,0)),('e',(5,0)),('e',(6,0)),('e',(7,0)),('e',(8,0)),('e',(1,1)),('e',(2,1)),('e',(3,1)),('e',(4,1)),('e',(5,1)),('e',(6,1)),('e',(7,1)),('e',(8,1))],
    'White': [('e',(8,11)),('e',(7,11)),('e',(6,11)),('e',(5,11)),('e',(4,11)),('e',(3,11)),('e',(2,11)),('e',(1,11)),('e',(8,10)),('e',(7,10)),('e',(6,10)),('e',(5,10)),('e',(4,10)),('e',(3,10)),('e',(2,10)),('e',(1,10))]
    } # Note White peices are interred in the 'Black' Graves


while inProgress:	
	################ White Turn/User Input ################

    fen1=board.fen()

    for i in range(1,20):
        try:
            # print("detect")
            m = get_user_input(fen1,arena)
            # print('final' + str(m))
            if m == 'end' or m == 'End':
                break
            if m == -1:
                print("Game Finish")
                break
            piece=str(board.piece_at(get_start_pos(m)))
            board.push_uci(m)
            break
        except ValueError:
            print('Failed to find a legal move')
    if m == -1:
        break



    fen2=board.fen()
    
    file.write(fen2+'\n')
        
    if board.is_game_over() == True:
        inProgress = False  
        print("White Won")
        score[0] = score[0] + 1
#        movement.move(fen1,fen2,m[0:2], m[2:4],piece,'White')
        serial.splitMove([[(0, 0),(0, 0)]])
        break
    else:
        print('White Move Made: ', m)
#        movement.move(fen1,fen2,m[0:2], m[2:4],piece,'White')

    # byte = 'x'
    # counter = 0
    # while counter < 10:
    #     byte = serial.ser.read(size=1)
    #     print byte
    #     if byte  == 'x':
    #         counter = counter + 1

    sleep(2)
        
    ################ Black Turn ################
    Black.position(board)
    fen1=board.fen()
    n = str(Black.go(movetime=1)[0])
    piece=str(board.piece_at(get_start_pos(n)))
    chess.Move.from_uci(n)
    board.push_uci(n)
    count = count + 1
        
    fen2=board.fen()
        
    file.write(fen2+'\n')
        
        
    if board.is_game_over() == True:
        inProgress = False
        print("Black Won")
        score[1] = score[1] + 1
        movement.move(fen1,fen2,n[0:2], n[2:4],piece,'Black',Graves)
        serial.splitMove([[(0, 0),(0, 0)]])
        break
    else:
        print('Black Move Made: ', n)
        movement.move(fen1,fen2,n[0:2], n[2:4],piece,'Black',Graves)
        
    # print "\n"
        
#    var = chess.svg.board(board=board)
#    print var
#    display(SVG(var))
    
#White.ucinewgame()
#Black.ucinewgame()
#file.write(str(serial.servoList)+'\n'+'\n') 
#file.write(str(len(serial.servoList)))
#print len(serial.servoList)
#serial.servoList=[]




