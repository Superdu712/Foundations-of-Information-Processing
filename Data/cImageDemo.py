#https://github.com/bnmnetp/cImage
from cImage import *
myimagewindow = ImageWin("Image Processing",1200,800)
oldimage = FileImage("lutherbell.gif")
oldimage.setPosition(0,0)
oldimage.draw(myimagewindow)

width = oldimage.getWidth()
height = oldimage.getHeight()
newim = EmptyImage(width,height)

for row in range(height):
    for col in range(width):
            oldpixel = oldimage.getPixel(col,row)
            ave=(oldpixel.getRed()+oldpixel.getGreen()+oldpixel.getBlue())/3
            newim.setPixel(col,row,Pixel(ave,ave,ave))

newim.setPosition(width+1,0)
newim.draw(myimagewindow)

myimagewindow.exitOnClick()
