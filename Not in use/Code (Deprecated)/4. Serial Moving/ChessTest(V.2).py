
# http://support.stockfishchess.org/kb/advanced-topics/compiling-stockfish-on-mac-os-x
# https://github.com/zhelyabuzhsky/stockfish
# https://pypi.python.org/pypi/pystockfish/0.1.3

import chess.uci

def move(fen,startPos, endPos):
	    # Starting and ending positions
    startPos = (ord(startPos[0])-95,int(startPos[1]))
    endPos = (ord(endPos[0])-95,int(endPos[1]))
    print fen


move_notation = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7}
def get_start_pos(x):
	return int(move_notation[list(x)[0]] + int(list(x)[1])*8-8)

# board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")




engine1 = chess.uci.popen_engine('./stockfish')
engine1.uci()
options1 = {"Skill Level" : 5}
engine1.setoption(options1)


engine2 = chess.uci.popen_engine('./stockfish')
engine2.uci()
options2 = {"Skill Level" : 20}
engine2.setoption(options2)



# engine.setoption(options1)
# print(engine.author

# x = True

score = [0,0]
count = 0
ncount = 0



for i in range(0,1):
	# count = 0
	x = True
	board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
	while x:
		engine1.position(board)
		fen = board.fen()
		m = str(engine1.go(movetime=1)[0])
		if str(board.piece_at(get_start_pos(m))) == 'N':
			ncount = ncount + 1
		print m[0:2], m[2:4]
		chess.Move.from_uci(m)
		board.push_uci(m)
		count = count + 1

		move(fen,m[0:2], m[2:4])

		if board.is_game_over() == True:
			x = False
			# print "engine1 Won"
			score[0] = score[0] + 1
			break

		engine2.position(board)
		fen = board.fen()
		n = str(engine2.go(movetime=1)[0])
		if str(board.piece_at(get_start_pos(n))) == 'n':
			ncount = ncount + 1
		print n[0:2], n[2:4]
		chess.Move.from_uci(n)
		board.push_uci(n)
		count = count + 1

		move(fen,n[0:2], n[2:4])

		if board.is_game_over() == True:
			x = False
			# print "engine2 Won"
			score[1] = score[1] + 1
		# count = count + 1
		print "\n"
	engine1.ucinewgame()
	engine2.ucinewgame()


print score, ncount, count




