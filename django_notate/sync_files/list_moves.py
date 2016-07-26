def listMoves():
	for x in range(1, 30):
		moveNumber = str(x) + ". "
		move = ""
		for y in range(0,2):
			if(y == 0):
				move = str(y)
			if(y == 1):
				move += " .. " + str(y)
		print moveNumber + move
