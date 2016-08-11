import cv2
import numpy as np

def after_image(firstImage,secondImage):
	imageOne = cv2.imread(firstImage)#first image
	imageTwo = cv2.imread(secondImage)#second image

	changeDetected = cv2.subtract(imageOne, imageTwo)

	movementFound = not np.any(changeDetected)

	if movementFound is True:
			print "The images are the same in after"
	else:
		cv2.imwrite("AfterImageMove.jpg", changeDetected)
		print "the images are different in after"

def before_image(firstImage,secondImage):
	imageOne = cv2.imread(secondImage)#second image
	imageTwo = cv2.imread(firstImage)#first image

	changeDetected = cv2.subtract(imageOne, imageTwo)

	movementFound = not np.any(changeDetected)

	if movementFound is True:
			print "The images are the same in before"
	else:
		cv2.imwrite("BeforeImageMove.jpg", changeDetected)
		print "the images are different in before"
