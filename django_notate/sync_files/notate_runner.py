from img_process_runner import getAfterCoordinates, getBeforeCoordinates
from grid import grid_translate
from return_notation import move_piece

def run_opencv(img1,img2):
	before_coords = getBeforeCoordinates(img1,img2)
	after_coords = getAfterCoordinates(img1,img2)

	xAxisBefore = before_coords[0]
	yAxisBefore = before_coords[1]
	xAxisAfter = after_coords[0]
	yAxisAfter = after_coords[1]

	beforeIndex = grid_translate(xAxisBefore, yAxisBefore)
	afterIndex = grid_translate(xAxisAfter, yAxisAfter)

	# print "before coords"
	# print before_coords
	# print "after coords"
	# print after_coords

	# print "before index"
	# print beforeIndex
	# print "after index"
	# print afterIndex

	moveNotation = move_piece(beforeIndex, afterIndex) 
	return moveNotation


