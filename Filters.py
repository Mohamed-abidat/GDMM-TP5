from PIL import Image, ImageFilter
original = Image.open("images/cat2.jpg")
# Conture
filterd  = original.filter(ImageFilter.CONTOUR)
filterd.show()
# EDGE_ENHANCE
filterd  = original.filter(ImageFilter.EDGE_ENHANCE)
filterd.show()
# FIND_EDGES
filterd  = original.filter(ImageFilter.FIND_EDGES)
filterd.show()
# SMOOTH
filterd  = original.filter(ImageFilter.SMOOTH)
filterd.show()
# CROP
filterd  = original.crop((0,0,200,200))
filterd.show()
