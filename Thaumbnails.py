from PIL import Image
size = (256, 256)
im = Image.open("images/cat2.jpg")
im.thumbnail(size)
im.show()
im.save("images/cat2.small.jpg")
gray_scale = im.convert('L')
gray_scale.show()