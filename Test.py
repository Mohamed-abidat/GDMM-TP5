from PIL  import Image
im = Image.open("images/test1.jpg")
# print attributes
print(im.size, im.format, im.mode)
im.show()

from PIL import ImageFilter
original = Image.open("images/test2.jpg")
blured = original.filter(ImageFilter.BLUR)
original.show()
blured.show()
blured.save("images/blured.jpeg")