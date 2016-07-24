from PIL import Image, ImageEnhance

def darken(lightImage):
	image = Image.open(lightImage)
	# contrast = ImageEnhance.Contrast(image)
	image2 = image.point(lambda p: p * 0.3)
	image2.show()
	image2.save("DarkImageMove.jpg")
	# contrast.enhance().show()