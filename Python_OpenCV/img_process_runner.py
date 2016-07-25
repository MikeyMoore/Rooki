from Image_Diff_Detection_After import after_image, before_image
from contrast import darken
from coordinates_new import coordinates
import sys

# f1=sys.argv[1]
# f2=sys.argv[2]
# print\
# 	('\n',f1,'\n',f2,'\n')

def getCoordinates(img1,img2):
	# this saves as AfterImageMove.jpg
	#Image_Diff_Detection_After function call
	after_image(img1,img2)


	# This saves as DarkImageMove.jpg
	#contrast.py function call
	darken("AfterImageMove.jpg")
	print "boo"
	# coordinate function
	# coordinates()
	#coordinates_new.py - call
	coorAfter = coordinates()
	# coordinates()
	# return coor
	# print "hey there"
	print coorAfter

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

getCoordinates('../IMG_0141.jpg','../IMG_0142.jpg')
