from PIL import Image, ImageEnhance

def darken(lightImage):
	image = Image.open(lightImage)
	imageDarkened = image.point(lambda p: p * 0.3)

	# Below is an attempt to brighten the found change in two images
	# after it has been darkened to destroy unwanted artifacts.  It 
	# currently does not work.

	# contrast = ImageEnhance.Contrast(imageDarkened)
	# pinpointedChange = contrast.enhance(6)
	# pinpointedChange.show()

	imageDarkened.save("DarkImageMove.jpg")
	

