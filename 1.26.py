Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> def drawRectangle(myTurtle,width,height):
	myTurtle.forward(width)
	myTurtle.right(90) #side 1
	myTurtle.forward(height)
	myTurtle.right(90) #side 2
	myTurtle.forward(width)
	myTurtle.right(90) #side 3
	myTurtle.forward(height)
	myTurtle.right(90) #side 4
