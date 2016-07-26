from img_process_runner import getAfterCoordinates, getBeforeCoordinates
from grid import grid_translate
from return_notation import move_piece

after_coords = getBeforeCoordinates('../../IMG_0322.jpg','../../IMG_0323.jpg', args['new'])
before_coords = getAfterCoordinates('../../IMG_0322.jpg','../../IMG_0323.jpg', args['new'])

xAxisBefore = before_coords[0]
yAxisBefore = before_coords[1]
xAxisAfter = after_coords[0]
yAxisAfter = after_coords[1]

beforeIndex = grid_translate(xAxisBefore, yAxisBefore)
afterIndex = grid_translate(xAxisAfter, yAxisAfter)

moveNotation = move_piece(beforeIndex, afterIndex) 


