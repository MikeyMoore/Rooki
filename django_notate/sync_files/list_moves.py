from notate_runner import run_opencv
import sqlite3

conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()

def listMoves():

	# this logic saves the single move in db, 
	# need an ImageObject.length
	for x in range(0,2):
   		# images should be ImageObject.first and ImageObject.second
   		notation = run_opencv('../../IMG_0322.jpg','../../IMG_0323.jpg')
   		# c.execute('INSERT INTO notations VALUES (?)', notation)
    	# need logic to delete first image

	# grab each notation object from database => 
	# one notation object should look something like: 
	# 'f8Be8'
	# ============
	# NotationObjects.all

	indexForNotation = 0
	finalNotation = ""
	moveWhite = ""
	moveBlack = ""
	for y in range(1,30):
		for x in range(0, 2):
			moveNumber = str(y) + ". "
			
			if(x % 2 == 0):
				# need to call NotateObject id=indexForNotation
				moveWhite = "white" + str(indexForNotation)
				# delete NotateObject
				# SomeModel.objects.filter(id=id).delete()
				indexForNotation += 1
			else:
				# need to call NotateObject id=indexForNotation
				moveBlack = " .. " + "black" + str(indexForNotation)
				# delete NotateObject
				# SomeModel.objects.filter(id=id).delete()
				indexForNotation += 1
		# need to delete first two NotateObjects in database
		finalNotation += moveNumber + moveWhite + moveBlack + "\n"

	print finalNotation
