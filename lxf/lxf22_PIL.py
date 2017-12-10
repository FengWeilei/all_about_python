# -*- coding: utf-8 -*-

from PIL import Image

##im = Image.open('cover.jpg')
##w, h = im.size
##print('Original image size: %s*%s' % (w, h))
##
##im.thumbnail((w//2, h//2))
##print('Resize image = %s*%s' % (w//2, h//2))
##
##im.save('thumbnail.jpg', 'jpeg')


from PIL import Image, ImageFilter

im = Image.open('cover.jpg')

im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
