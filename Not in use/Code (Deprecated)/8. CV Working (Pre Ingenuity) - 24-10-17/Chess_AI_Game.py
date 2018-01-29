
import chess.uci

#import Chess_Movement as movement   


				# import Chess_Serial as serial

print('Running')
#########  Setup  ############
move_notation = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7}
def get_start_pos(x):
	return int(move_notation[list(x)[0]] + int(list(x)[1])*8-8)

def get_user_input():
    var = raw_input("Enter Move like e2e4: ")
    return var

open('out.txt', 'w').close() 
file = open('out.txt', 'a')


###### Establish AI #########
White = chess.uci.popen_engine('./stockfish') #setup black side chess AI
White.uci()
options1 = {"Skill Level" : 5}
White.setoption(options1)

Black = chess.uci.popen_engine('./stockfish') #setup black side chess AI
Black.uci()
options2 = {"Skill Level" : 20}
Black.setoption(options2)

score = [0,0]
count = 0
ncount = 0


################    Game    ################
inProgress = True
board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
fen2=board.fen()
while inProgress:	
	################ White Turn/User Input ################
    
        
    White.position(board)
    fen1=board.fen()
    m = str(White.go(movetime=1)[0])
    piece=str(board.piece_at(get_start_pos(m)))
    chess.Move.from_uci(m)
    board.push_uci(m)
    count = count + 1
        
    fen2=board.fen()
        
    file.write(str(board)+'\n'+'\n')
        
    if board.is_game_over() == True:
        inProgress = False  
        print "White Won"
        score[0] = score[0] + 1
#        movement.move(fen1,fen2,m[0:2], m[2:4],piece,'White')
        break
    else:
        print 'White Move Made: ', m
#        movement.move(fen1,fen2,m[0:2], m[2:4],piece,'White')
        
        
    ################ Black Turn ################
    Black.position(board)
    fen1=board.fen()
    n = str(Black.go(movetime=1)[0])
    piece=str(board.piece_at(get_start_pos(n)))
    chess.Move.from_uci(n)
    board.push_uci(n)
    count = count + 1
        
    fen2=board.fen()
        
    file.write(str(board)+'\n'+'\n')
        
        
    if board.is_game_over() == True:
        inProgress = False
        print "Black Won"
        score[1] = score[1] + 1
#        movement.move(fen1,fen2,n[0:2], n[2:4],piece,'Black')
        break
    else:
        print 'Black Move Made: ', n
#        movement.move(fen1,fen2,n[0:2], n[2:4],piece,'Black')
        
    # print "\n"
        
    print board

    

    
#White.ucinewgame()
#Black.ucinewgame()
#file.write(str(serial.servoList)+'\n'+'\n') 
#file.write(str(len(serial.servoList)))
# print len(serial.servoList)
#serial.servoList=[]




