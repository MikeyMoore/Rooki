# Notate
- World's first iOS app aiming to automically notate chess notation. Iteration 1 relies on the iPhone being in a fixed position for consistent image positioning.

## Members
- Q: Mikey Moore 
- N: Abid Ramay 
- R: Sam Heinz
- B: Justin Wong

## Stack
- MySQL/Firebase
- Django
- React Native
- Python (+ OpenCV)

## Feature Goals / MVP for Iteration 1
- User can take pictures using phone camera of chess board from within app
- User is prompted with an alert to take a picture of board at starting position
- Camera notifies user of picture taken success
- Camera is squared to only fit the chess board in it's view
- Each image of board is stored in Firebase (Firestack)
- User can press endgame button to request entire game notation
- Each image goes through OpenCV, which returns the pixel coordinates of each move (comparing two photos at a time)
- Those coordinates are translated into notation (see notation format at bottom)
- User can view the notated output inside app

## Stretch Goals / Goals for future iterations
- Notate edge cases: castling, en passant, check or checkmate.
- User can download a text file of the finished notation
- Notation returned after every move

## Notation Format
- K: King, Q: Queen, B: Bishop, N: Knight, R: Rook
- With rooks, knights, bishops, queens, and kings we always start with the square they came from followed by their letter and then the square they moved to - for example, if the rook starts on a3 and moves to a5, that is notated as: a3Ra5
- With pawns, we only say where they moved to.  So, if a pawn starts on a3 and moves to a5, that is notated as: a5
- If a K, Q, B, N, or R take another piece (move to a square that was already occupied by another piece), we add an 'x' as well as the letter of the taken piece in between the letter of the moving piece and the square they move to.  So, if a rook starts on a3 and moves to the already occupied square a5 (occupied by a knight), we notate that as: a3RxNa5.  If the square was occupied by a bishop, we notate that as: a3RxBa5.
- If a pawn moves to an already occupied square, let's say the a3 pawn moves to the occupied square b4 (occupied by a knight), we would notate that as: axNb4.  If a pawn on c5 moves to the occupied square d6 (occupied by a pawn), we would notate that as: cxd6.
- Each move would begin with a number, followed by white's move, two dots, then black's move: 11.a2Ra3 .. g6Bh7
- Our app currently cannot notate for castling, en passant, getting put in check, or checkmating.




