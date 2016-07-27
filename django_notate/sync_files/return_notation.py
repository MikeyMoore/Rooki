# Important: need to take resetting the chessboard into consideration

chessboard = ["a8 R", "b8 N", "c8 B", "d8 Q", "e8 K", "f8 B", "g8 N", "h8 R",
	"a7 P", "b7 P", "c7 P", "d7 P", "e7 P", "f7 P", "g7 P", "h7 P",
	"a6 o", "b6 o", "c6 o", "d6 o", "e6 o", "f6 o", "g6 o", "h6 o",
	"a5 o", "b5 o", "c5 o", "d5 o", "e5 o", "f5 o", "g5 o", "h5 o",
	"a4 o", "b4 o", "c4 o", "d4 o", "e4 o", "f4 o", "g4 o", "h4 o",
	"a3 o", "b3 o", "c3 o", "d3 o", "e3 o", "f3 o", "g3 o", "h3 o",
	"a2 P", "b2 P", "c2 P", "d2 P", "e2 P", "f2 P", "g2 P", "h2 P",
	"a1 R", "b1 N", "c1 B", "d1 Q", "e1 K", "f1 B", "g1 N", "h1 R"]

def move_piece(start_index, end_index):
	start_square = chessboard[start_index]
	end_square = chessboard[end_index]
	piece = chessboard[start_index][-1]
	print(piece)
	print(start_square)
	chessboard[start_index] = chessboard[start_index].replace(chessboard[start_index][-1], "o")
	print(chessboard[start_index])
	chessboard[end_index] = chessboard[end_index].replace(chessboard[end_index][-1], piece)
	print(chessboard[end_index])
	print(chessboard)

	if(piece != "P" and end_square[-1] == "o"):
		# non-pawn from start to empty spot
		notation = start_square + end_square[0:2]
		notation = notation.replace(" ", "")
		print notation
	elif(piece != "P" and end_square[-1] == "P"):
	    # non-pawn from start to take pawn
	    notation = start_square + "x" + end_square[0:2]
	    notation = notation.replace(" ", "")
	    print notation
	elif(piece != "P" and end_square[-1] != "o" and end_square[-1] != "P"):
		# non-pawn from start to take another piece
		notation = start_square + "x" + end_square[-1] + end_square[0:2]
		notation = notation.replace(" ", "")
		print notation
	elif(piece == "P" and end_square[-1] == "o"):
		# pawn go from start to empty spot
		notation = end_square[0:2]
		print notation
	elif(piece == "P" and end_square[-1] == "P"):
		# pawn go from start to take pawn
		notation = start_square[0] + "x" + end_square[0:2]
		print notation
	elif(piece == "P" and end_square[-1] != "P" and end_square[-1] != "o"):
		# pawn go from start to take another piece
		notation = start_square[0] + "x" + end_square[-1] + end_square[0:2]
		print notation
	else:print "Oops"
	
# move_piece(2, 9)
