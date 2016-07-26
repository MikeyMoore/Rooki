# check if you can set a variable equal to a set 
# then once the differences and similarities are found, move the pieces in the variable at the index of the differences/similarities
# return to the user a move based upon the similarities and differences

# create two functions 
  # first function takes in two coordinates (the first is a8, the second is a3) the function will move a rook from a8 to a3
  # second function takes in two coordinates (the first is a8, the second is a1) the function will move a rook from a8 to a1 and take the rook on a1 off the board

chess1 = ["a8 R", "b8 N", "c8 B", "d8 Q", "e8 K", "f8 B", "g8 N", "h8 R",
	"a7 P", "b7 P", "c7 P", "d7 P", "e7 P", "f7 P", "g7 P", "h7 P",
	"a6 P", "b6 P", "c6 P", "d6 P", "e6 P", "f6 P", "g6 P", "h6 P",
	"a5 o", "b5 o", "c5 o", "d5 o", "e5 o", "f5 o", "g5 o", "h5 o",
	"a4 o", "b4 o", "c4 o", "d4 o", "e4 o", "f4 o", "g4 o", "h4 o",
	"a3 o", "b3 o", "c3 o", "d3 o", "e3 o", "f3 o", "g3 o", "h3 o",
	"a2 P", "b2 P", "c2 P", "d2 P", "e2 P", "f2 P", "g2 P", "h2 P",
	"a1 R", "b1 N", "c1 B", "d1 Q", "e1 K", "f1 B", "g1 N", "h1 R"]
	
chess2 = ["a8 R", "b8 N", "c8 B", "d8 Q", "e8 K", "f8 B", "g8 N", "h8 R",
	"a7 P", "b7 P", "c7 P", "d7 P", "e7 P", "f7 P", "g7 P", "h7 P",
	"a6 P", "b6 P", "c6 P", "d6 P", "e6 P", "f6 P", "g6 P", "h6 P",
	"a5 P", "b5 P", "c5 P", "d5 P", "e5 P", "f5 P", "g5 P", "h5 P",
	"a4 P", "b4 P", "c4 P", "d4 P", "e4 P", "f4 P", "g4 P", "h4 P",
	"a3 P", "b3 P", "c3 P", "d3 P", "e3 P", "f3 P", "g3 P", "h3 P",
	"a2 P", "b2 P", "c2 P", "d2 P", "e2 P", "f2 P", "g2 P", "h2 P",
	"a1 R", "b1 N", "c1 B", "d1 Q", "e1 K", "f1 B", "g1 N", "h1 R"]

zb = set(chess1)
	
zc = set(chess2)
	
# matched = zb.intersection(zc) 
# unmatched = zb.symmetric_difference(zc) 

# print(matched)
# print(unmatched)

def move_piece(start_index, end_index):
	# I added this part -Mikey
	start_index = start_index[0]
	end_index = end_index[0]

	start_square = chess1[start_index]
	piece = chess1[start_index][-1]
	# print(piece)
	# print(start_square)
	chess1[start_index] = chess1[start_index].replace(chess1[start_index][-1], "o")
	# print(chess1[start_index])
	chess1[end_index] = chess1[end_index].replace(chess1[end_index][-1], piece)
	# print(chess1[end_index])
	# print(chess1)
	notation = start_square + chess1[end_index][0:2]
	notation = notation.replace(" ", "")
	return notation
    

# move_piece(0, 40)