from PIL import Image, ImageFilter,ImageDraw
im = Image.open("images/cat2.jpg")
im_rotated = im.rotate(270)
im_rotated.show()