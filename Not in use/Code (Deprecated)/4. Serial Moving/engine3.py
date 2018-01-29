import chess.uci

board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

for x in xrange(0,63):
	print board.piece_at(x)

print board

move_notation = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7}

def get_start_pos(move):
	return int(move_notation[list(move)[0]] + int(list(move)[1])*8-8)




x = '8'



print board.piece_at(get_start_pos(x))