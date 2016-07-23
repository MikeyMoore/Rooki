import cv2
import numpy as np 

image1 = cv2.imread("../IMG_0142.jpg")#second image
image2 = cv2.imread("../IMG_0143.jpg")#first image

difference2 = cv2.subtract(image1, image2)

result2 = not np.any(difference2)

if result2 is True:
		print "The images are the same"
else: 
	cv2.imwrite("testTwo.jpg", difference2)
	print "the images are different"