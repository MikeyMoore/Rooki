# import the necessary packages
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import cv2
import argparse
import imutils

def coordinates():

	# load our input image, convert it to grayscale, and blur it slightly
	image = cv2.imread("DarkImageMove.jpg")
	print "Finding coordinates of move"
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (7, 7), 0)

	# perform edge detection, then perform a dilation + erosion to
	# close gaps in between object edges
	edged = cv2.Canny(gray, 50, 100)

	# find contours in the edge map, only need the corner points
	cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]

	# sort the contours from left-to-right and initialize the bounding box
	# point colors
	(cnts, _) = contours.sort_contours(cnts)
	colors = ((0, 0, 255), (240, 0, 159), (255, 0, 0), (255, 255, 0))

	# loop over the contours individually
	for (i, c) in enumerate(cnts):
		# if the contour is not sufficiently large, ignore it
		if cv2.contourArea(c) < 100:
			continue

		# compute the rotated bounding box of the contour, then
		# draw the contours
		box = cv2.minAreaRect(c)
		box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
		box = np.array(box, dtype="int")
		cv2.drawContours(image, [box], -1, (0, 255, 0), 2)

		# show the original coordinates
		# print("Object #{}:".format(i + 1))

		return box
		
