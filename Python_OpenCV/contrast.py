from PIL import Image, ImageEnhance
image = Image.open('testOne.jpg')
# contrast = ImageEnhance.Contrast(image)
image2 = image.point(lambda p: p * 0.3)
image2.show()
image2.save("testOneDarker.jpg")
# contrast.enhance().show()