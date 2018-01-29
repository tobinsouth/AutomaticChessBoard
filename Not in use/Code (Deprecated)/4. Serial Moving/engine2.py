# http://support.stockfishchess.org/discussions/problems/6080-mac-python-stockfish-engine-integration

import subprocess
import chess

board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")


stockfish = subprocess.Popen(["./stockfish"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

def get_best_move(moves_list, move_time, skill_level):
	"""
	>>> get_best_move([], '500', '20')
	(u'e2e4', '')
	"""
	moves_as_str = str(moves_list)
	stockfish.stdin.write(('setoption name Threads value 4\n').encode('utf-8'))
	stockfish.stdin.flush()
	stockfish.stdin.write(('setoption name Hash value 512\n').encode('utf-8'))
	stockfish.stdin.flush()
	stockfish.stdin.write(('setoption name OwnBook value true\n').encode('utf-8'))
	stockfish.stdin.flush()
	stockfish.stdin.write(('setoption name Skill Level value ' + skill_level + '\n').encode('utf-8'))
	stockfish.stdin.flush()
	stockfish.stdin.write(('position startpos moves ' + moves_as_str + '\n').encode('utf-8'))
	stockfish.stdin.flush()
	stockfish.stdin.write(('go wtime ' + move_time + ' btime ' + move_time + '\n').encode('utf-8'))
	stockfish.stdin.flush()

	bestmove = "";
	analysis = "";

	while True:
		line = stockfish.stdout.readline().decode().rstrip()
		if "score cp" in line or "score mate" in line:
			analysis = line.split('multipv')[0]
		if "bestmove" in line:
			bestmove = line
			break
	
	return bestmove.split()[1], analysis




# print get_best_move([], '500', '20')[0]


x = True
count = 0

while x:
	# engine.position(board)
	# engine.go(movetime=2000)
	m = get_best_move(board, '500', '20')[0]
	print m, count, board.fen()
	chess.Move.from_uci(str(m))
	board.push_uci(str(m))
	
	print(board)

	if board.is_game_over() == True:
		x = False
		break

	# engine.position(board)
	# engine.go(movetime=2000)
	m = get_best_move(board, '500', '20')[0]
	print m, count, board.fen()
	chess.Move.from_uci(str(m))
	board.push_uci(str(m))

	print(board)

	if board.is_game_over() == True:
		x = False
	count = count + 1



