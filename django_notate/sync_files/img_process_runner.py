from Image_Diff_Detection_After import after_image, before_image
from contrast import darken
from coordinates_new import coordinates
import argparse
import sys

def getAfterCoordinates(img1,img2, new_order=-1):
	# this saves as AfterImageMove.jpg
	print "after"
	after_image(img1,img2)


	# This saves as DarkImageMove.jpg
	darken("../AfterImageMove.jpg")

	# After coordinate function
	coords = coordinates(new_order)
	# first axis
	print coords.flatten()[0] 
	# second axis
	print coords.flatten()[1] 

def getBeforeCoordinates(img1,img2, new_order=-1):
	# this saves as BeforeImageMove.jpg
	print "before"
	before_image(img1,img2)
	
	# This saves as DarkImageMove.jpg
	darken("../BeforeImageMove.jpg")
	
	# Before coordinate function
	coords = coordinates(new_order)
	# first axis
	print coords.flatten()[0] 
	# second axis
	print coords.flatten()[1] 



if __name__ == "__main__":
	ap = argparse.ArgumentParser()
	ap.add_argument("-n", "--new", type=int, default=-1,
		help="whether or not the new order points should should be used")
	args = vars(ap.parse_args())
	print args
	# These two images break the before coordinates call
	getBeforeCoordinates('../../IMG_0261.jpg','../../IMG_0262.jpg', args['new'])
	getAfterCoordinates('../../IMG_0261.jpg','../../IMG_0262.jpg', args['new'])

	# Now we need to remove the images created by OpenCV
	# os.remove('AfterImageMove.jpg')
	# os.remove('BeforeImageMove.jpg')
	# os.remove('DarkImageMove.jpg')
	
