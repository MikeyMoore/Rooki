from Image_Diff_Detection_After import after_image, before_image
from contrast import darken
from coordinates_new import coordinates
import argparse
import sys

def getCoordinates(img1,img2, new_order=-1):
	# this saves as AfterImageMove.jpg
	#Image_Diff_Detection_After function call
	print "after"
	after_image(img1,img2)


	# This saves as DarkImageMove.jpg
	#contrast.py function call
	darken("../AfterImageMove.jpg")

	# After coordinate function
	coordinates(new_order)

	# this saves as BeforeImageMove.jpg
	print "before"
	before_image(img1,img2)
	
	# Now for the before coordinates
	darken("BeforeImageMove.jpg")
	
	# Before coordinate function
	coordinates(new_order)

	# os.remove('AfterImageMove.jpg')
	# os.remove('BeforeImageMove.jpg')
	# os.remove('DarkImageMove.jpg')
	# os.remove('ItsAlive.jpg')


if __name__ == "__main__":
	ap = argparse.ArgumentParser()
	ap.add_argument("-n", "--new", type=int, default=-1,
		help="whether or not the new order points should should be used")
	args = vars(ap.parse_args())
	print args
	getCoordinates('IMG_0141.jpg','IMG_0142.jpg', args['new'])
