# import the necessary packages
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import cv2
import argparse
import imutils

def coordinates():

	# load image, convert it to grayscale, and blur it to remove noise
	image = cv2.imread("DarkImageMove.jpg")
	print "Finding coordinates of move"
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (7, 7), 0)

	# perform edge detection
	edged = cv2.Canny(gray, 50, 100)

	# find contours in the edge map, only need the corner points
	cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]

	# sort the contours from left-to-right 
	(cnts, _) = contours.sort_contours(cnts)

	# loop over the contours individually
	for (i, c) in enumerate(cnts):

		# compute the rotated bounding box of the contour, then
		# draw the contours
		box = cv2.minAreaRect(c)
		box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
		# box = np.array(box, dtype="int")

		# show the original coordinates
		# print("Object #{}:".format(i + 1))

		return box
		
