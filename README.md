# The Automatic Chess Board
## Making a chessboard that you play, a project by Thomas, Chris and Tobin

### Computer Vision and Piece Detection
To detect the chess pieces, a video feed from a camera above is passed into a python script that dissects the board into the individual squares, which are then passed through a neural network that we trained to detect white chess pieces. This board state is then processed to determine the move made. This process continues until a user makes a legal move. This move is then passed back to the Chess AI.

### Convolutional Neural Network
The machine learning approach to detecting the pieces uses a neural network from PyTorch. The architecture follows: convolution, pool, convolution, pool, and two fully connected layers leading to output. This is totally overkill but creates almost perfect accuracy. Other approaches which used classical image processing techniques were also used extensively, however, the machine learning approach supersedes the need for these. 

### Chess AI
The chess AI used is known as the Stockfish Engine. This engine is open source and has programmable difficulties. One key advantage is that only the current FEN (Forsyth-Edwards Notation, an ASCII string describing the state of the game) of the chess board needs to be parsed to the AI. The AI outputs a move, and an A* search algorithm finds an optimised path for the piece(s) involved to take. When moving pieces such as the knight, if needed, another piece will be temporarily moved automatically.

### Physical System
The chess pieces are moved by a retractable magnet mounted on a carriage that can be moved around the board by two stationary stepper motors labelled A and B below. The motion is very unintuitive but is described simply with the equations below. The frame is composed of a blue chess board on top of a wooden base with acrylic top to see the working mechanics for the purpose of using this tool as an educational tool for student outreach.

## Main Contributers:
Chris Whalley (BE(Hons)(Mecht))
Thomas Walker (BE(Hons)(Mecht))
Tobin South (BMaCompSc)

## Sponsors:
Adept
Australian Center for Robotic Vision

Thanks to Rafa for being a legend
