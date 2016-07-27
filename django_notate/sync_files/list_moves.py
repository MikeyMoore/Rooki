from notate_runner import run_opencv
import sqlite3
from sync_files.models import Document

conn = sqlite3.connect('../db.sqlite3', check_same_thread = False)
c = conn.cursor()

def listMoves():
	imageCount = c.execute('SELECT COUNT(*) FROM sync_files_document')
	# this logic saves the single move in db, 
	# need an ImageObject.length
	for x in range(1,imageCount):
   		# images should be ImageObject.first and ImageObject.second
   		# notation = run_opencv('../../IMG_0322.jpg','../../IMG_0323.jpg')
   		imageFirst = c.execute('SELECT * FROM sync_files_document WHERE ID=(?)', [x])
   		imageSecond = c.execute('SELECT * FROM sync_files_document WHERE id=(?)', [x+1])
   		notation = run_opencv(imageFirst, imageSecond)
   		c.execute('INSERT INTO sync_files_notations VALUES (?,?)', [x, notation])
    	# need logic to delete first image
   		c.execute('DELETE FROM sync_files_document WHERE ID=(?)', x)

	# grab each notation object from database => 
	# one notation object should look something like: 
	# 'f8Be8'
	# ============
	# NotationObjects.all

	indexForNotation = 1
	finalNotation = ""
	moveWhite = ""
	moveBlack = ""
	notationCount = c.execute('SELECT COUNT(*) FROM sync_files_notations')
	for y in range(1,notationCount):
		for x in range(0, 2):
			moveNumber = str(y) + ". "
			
			if(x % 2 == 0):
				# need to call NotateObject id=indexForNotation
				moveWhite = c.execute('SELECT * FROM sync_files_notations WHERE ID=(?)', [str(indexForNotation)])
				# delete NotateObject
				c.execute('DELETE FROM sync_files_notations WHERE ID=(?)', [str(indexForNotation)])
				indexForNotation += 1
			else:
				# need to call NotateObject id=indexForNotation
				moveBlack = " .. " + "black" + str(indexForNotation)
				# delete NotateObject
				c.execute('DELETE FROM sync_files_notations WHERE ID=(?)', [str(indexForNotation)])
				indexForNotation += 1
		finalNotation += moveNumber + moveWhite + moveBlack + "\n"

	return finalNotation
