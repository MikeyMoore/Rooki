from detect_change import after_image, before_image
from contrast import darken
from coordinates_new import coordinates
import argparse
import sys

def getBeforeCoordinates(img1,img2, new_order=-1):
	# This highlights change between two images 
	# and saves as BeforeImageMove.jpg
	before_image(img1,img2)
	
	# This darkens out artifacts in image 
	# and saves as DarkImageMove.jpg
	darken("BeforeImageMove.jpg")
	
	# Finds coordinates of the change in two images
	coords = coordinates(new_order)
	# This simplifies the the eight coordinates found
	# to two coordinates 
	twoCoords = [coords[0][0], coords[0][1]] 

	# Some console logs for debugging
	print "before coords"
	print coords

	return twoCoords

def getAfterCoordinates(img1,img2, new_order=-1):
	# This highlights change between two images 
	# and saves as AfterImageMove.jpg
	after_image(img1,img2)

	# This darkens out artifacts in image 
	# and saves as DarkImageMove.jpg
	darken("AfterImageMove.jpg")

	# Finds coordinates of the change in two images
	coords = coordinates(new_order)
	# This simplifies the the eight coordinates found
	# to two coordinates 
	twoCoords = [coords[0][0], coords[0][1]] 

	# Some console logs for debugging
	print "after coords"
	print coords

	return twoCoords

	
# Abid: I'm not sure why this code here is necessary?  -Mikey

# if __name__ == "__main__":
# 	ap = argparse.ArgumentParser()
# 	ap.add_argument("-n", "--new", type=int, default=-1,
# 		help="whether or not the new order points should should be used")
# 	args = vars(ap.parse_args())
	
# 	# getBeforeCoordinates('../../IMG_0322.jpg','../../IMG_0323.jpg', args['new'])
# 	getAfterCoordinates('../../IMG_0322.jpg','../../IMG_0323.jpg', args['new'])

# 	# Now we need to remove the images created by OpenCV
# 	# os.remove('AfterImageMove.jpg')
# 	# os.remove('BeforeImageMove.jpg')
# 	# os.remove('DarkImageMove.jpg')
	
