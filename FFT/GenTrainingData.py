
'''
This class will be responsible for generating images and the respective clicks.
It will also generate the expected results.


Phase 1.
1. Generate the image.  The image has only one shape.
2. Generate the click.  The click should be inside the desired object.


Phase 2.
1. Generate the image.  The image has multiple non-overlapping shapes.
2.

'''


from PIL import Image, ImageDraw
from random import randint


padding = 22

def genCenter(xrange, yrange):
    x=randint(padding,xrange-padding)
    y=randint(padding,yrange-padding)
    return x, y


# Generate random number: https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
def genCircleCoordinates(xcenter, ycenter):
    translatex=randint(-padding,0)
    translatey=randint(-padding,0)
    w = xcenter+translatex-padding/3
    x = ycenter+translatey-padding/3
    a=[w,x]
    b=[w+padding*2,x+padding*2]
    c=a+b
    return c


def genClick(xstart,xend,ystart,yend):
    xclick = randint(xstart, xend)
    yclick = randint(ystart, yend)
    return xclick, yclick


xrange=128
yrange=128

xcenter, ycenter = genCenter(xrange, yrange)

xstart,ystart,xend,yend = genCircleCoordinates(xcenter, ycenter)

smallPadding = int(padding/4)
xclick, yclick = genClick(xcenter-smallPadding,xcenter+smallPadding,ycenter-smallPadding,ycenter+smallPadding)


# Draw circle: https://pythonprogs.blogspot.com/2017/01/lets-draw-circle-with-pil-in-python.html
img = Image.new("RGB",(xrange,yrange),'white')
dr = ImageDraw.Draw(img)


dr.ellipse((xstart,ystart,xend,yend),'yellow') # Draw circle
dr.point([xcenter,ycenter], 'black')



img.show()


