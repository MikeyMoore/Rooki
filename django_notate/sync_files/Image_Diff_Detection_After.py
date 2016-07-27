import cv2
import numpy as np

def after_image(img1,img2):
	image1 = cv2.imread(img1)#first image
	image2 = cv2.imread(img2)#second image

	difference2 = cv2.subtract(image1, image2)

	result2 = not np.any(difference2)

	if result2 is True:
			print "The images are the same in after"
	else:
		cv2.imwrite("AfterImageMove.jpg", difference2)
		print "the images are different in after"

def before_image(img1,img2):
	image1 = cv2.imread(img2)#second image
	image2 = cv2.imread(img1)#first image

	difference2 = cv2.subtract(image1, image2)

	result2 = not np.any(difference2)

	if result2 is True:
			print "The images are the same in before"
	else:
		cv2.imwrite("BeforeImageMove.jpg", difference2)
		print "the images are different in before"
