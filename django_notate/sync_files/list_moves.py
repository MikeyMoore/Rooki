def listMoves():

	# grab each notation object from database => 
	# one notation object should look something like: 
	# 'f8Be8'
	# ============
	# Notation.all

	finalNotation = ""
	moveWhite = ""
	moveBlack = ""
	for y in range(1,30):
		for x in range(0, 2):
			moveNumber = str(y) + ". "
			indexForNotation = x
			
			if(x % 2 == 0):
				# need to call NotateObject.first
				moveWhite = "white" + str(x)
			else:
				# need to call NotateObject.second
				moveBlack = " .. " + "black" + str(x)
		# need to delete first two NotateObjects in database
		finalNotation += moveNumber + moveWhite + moveBlack + "\n"

	print finalNotation
