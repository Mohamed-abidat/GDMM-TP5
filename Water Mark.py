from PIL import Image, ImageFilter,ImageDraw
im = Image.open("images/cat2.jpg")
logo = Image.open("images/puppy1.jpg")
cp = im.copy()
position = (im.width-logo.width, im.height-logo.height)
cp.paste( logo, position)
cp.show()