import cv2
import numpy as np 

image1 = cv2.imread("IMG_0130.jpg")#first image
image2 = cv2.imread("IMG_0131.jpg")#second image

difference = cv2.subtract(image1, image2)

result = not np.any(difference) #if difference is all zeroes it will return False


if result is True:
		print "The images are the same"
else: 
	cv2.imwrite("before.jpg", difference)
	print "the images are different"

