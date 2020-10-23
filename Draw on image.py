from PIL import Image, ImageFilter,ImageDraw
im = Image.open("images/cat2.jpg")
# Conture
draw = ImageDraw.Draw(im)
draw.line((0,0)+im.size, fill= (255,255,255))
draw.line((0,im.size[1], im.size[0],0), fill= (255,255,255))
draw.text((im.size[0]/2 - 50, im.size[1]/2), "Mohamed", fill= (0,0,0))
im.show()