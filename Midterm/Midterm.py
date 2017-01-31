Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> #Programming Task 1:
Part 1. – Python commands of two different references point to the same collection-type object in memory:
>>> a = ["dog","cat","bird"] #a as a list of three elements
>>> b = a #assign the value of a to b
>>> b
['dog', 'cat', 'bird']
>>> 
>>> #Part 2. – It is not possible to have a single reference point to two or more distinct objects at the same time.  
>>> m = "fish" #assign a string to m
>>> m = [2,3,4] #assign a list to m
>>> m #the string goes away, leaves m as a list
[2, 3, 4]
>>> 
>>> #readline() vs. readlines()
>>> f = open("hihi.txt","r")
>>> a = f.readlines()
>>> a
['This is 1st line\n', '\n', 'This is 2nd line\n', 'This is 3rd line\n', '\n', '\n', 'This is 4th line\n', 'This is 5th line']
>>> f = open("hi.txt","r") 
>>> for a in f.readlines(): #readlines() in a for loop, for each line a 
	print(a) #prine line a
	f.close()

	
This is 1st line

This is 2nd line

This is 3rd line

This is 4th line

This is 5th line
>>> f = open("hi.txt","r")
>>> b = f.readline()
>>> while b: #readline() in a while loop, while each line b
	print(b) #print line b
	b = f.readline()

	
This is 1st line

This is 2nd line

This is 3rd line

This is 4th line

This is 5th line
>>> f.close()
>>> f = open("hi.txt","r")
>>> for line in f.readline(): #readline() in a for loop, for each line in f
	print(line) #print the line character by character
	f.close()

	
T
h
i
s
 
i
s
 
1
s
t
 
l
i
n
e


>>> #returns the next line of the file with all text up to and includeing the newline character \n.
>>> f = open("hi.txt","r")
>>> a = f.readline()
>>> a
'This is 1st line\n'
>>> a = f.readline()
>>> a
'This is 2nd line\n'
>>> a = f.readline()
>>> a
'This is 3rd line\n'
>>> a = f.readline()
>>> a
'This is 4th line\n'
>>> a = f.readline()
>>> a
'This is 5th line'
>>> a = f.readline()
>>> a
''
>>> f.close()
>>> 
>>> #readline(n) n is provided as a parameter, only n character will be returned if the line is longer than n.
>>> f = open("hi.txt","r")
>>> a = f.readline()
>>> a
'This is 1st line\n'
>>> a = f.readline(10)
>>> a
'This is 2n'
>>> a = f.readline(20)
>>> a
'd line\n'
>>> a = f.readline(100)
>>> a
'This is 3rd line\n'
>>> a = f.readline(4)
>>> a
'This'
>>> a = f.readline(5)
>>> a
' is 4'
>>> 
>>> #Returns a lost of n strings, each represting a single line of the file.
>>> #readlines(n)
>>> f = open("hi.txt","r")
>>> a = f.readlines(1)
>>> a
['This is 1st line\n']
>>> a = f.readlines(2)
>>> a
['This is 2nd line\n']
>>> a = f.readlines(3)
>>> a
['This is 3rd line\n']
>>> a = f.readlines(4)
>>> a
['This is 4th line\n']
>>> a = f.readlines(5)
>>> a
['This is 5th line']
>>> a = f.readlines(6)
>>> a
[]
>>> 
