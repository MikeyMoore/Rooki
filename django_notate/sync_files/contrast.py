from PIL import Image, ImageEnhance

def darken(lightImage):
	# print "made it to contrast"
	image = Image.open(lightImage)
	# contrast = ImageEnhance.Contrast(image)
	image2 = image.point(lambda p: p * 0.3)
	# print "I'm about to show image"
	# image2.show()
	# print "I'm about to write image"
	image2.save("DarkImageMove.jpg")
	# contrast.enhance().show()
	# print "finished the contrast statement"
