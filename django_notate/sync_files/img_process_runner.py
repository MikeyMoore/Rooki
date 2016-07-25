from Image_Diff_Detection_After import after_image, before_image
from contrast import darken
from coordinates_new import coordinates
import argparse
import sys

# f1=sys.argv[1]
# f2=sys.argv[2]
# print\
# 	('\n',f1,'\n',f2,'\n')

def getCoordinates(img1,img2, new_order=-1):
	# this saves as AfterImageMove.jpg
	#Image_Diff_Detection_After function call
	after_image(img1,img2)


	# This saves as DarkImageMove.jpg
	#contrast.py function call
	darken("../AfterImageMove.jpg")

	# coordinate function
	# coordinates()
	#coordinates_new.py - call
	# coorAfter = coordinates()
	coordinates(new_order)
	# print coordinates
	# return coor
	print "hey there"
	# print coorAfter

	# this saves as BeforeImageMove.jpg
	# before_image(img1,img2)
	#
	# # Now for the before coordinates
	# darken("BeforeImageMove.jpg")
	#
	# coorBefore = coordinates()
	# print coorBefore

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
