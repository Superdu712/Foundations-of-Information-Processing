>>> def sepiatone(imageFile):
        myImWin = ImageWin("Sepia Tone",800,250)
        oldIm = FileImage(imageFile)
        oldIm.draw(myImWin)
        width = oldIm.getWidth()
        height = oldIm.getHeight()
        newim = EmptyImage(width,height)
        for row in range(height):
                for col in range(width):
                        (r,g,b) = oldIm.getPixel(col,row)
                        newR = int(r*0.393+g*0.769+b*0.189)
                        newG = int(r*0.349+g*0.686+b*0.168)
                        newB = int(r*0.272+g*0.534+b*0.131)
                        if newR > 255:
                                newR = 255
                        if newG > 255:
                                newG = 255
                        if newB > 255:
                                newB = 255
                        newim.setPixel(col,row,Pixel(newR,newG,newB))
        newim.setPosition(width+1,0)
        newim.draw(myImWin)
        myImWin.exitOnClick()

>>> sepiatone("LutherBell.jpg")
>>> 
