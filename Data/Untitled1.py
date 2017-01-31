Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> def createWordlist(dname):
	wordList = []
	myFile = open(dname, 'r')
	line = myFile.readline()
	punctuation = ['(',')','?','!',':',';',',','.','/','"',",","_","#","@","^","&","*","%","+","=","|",'<','>']
	number = [0,1,2,3,4,5,6,7,8,9]
	while line is not '':
		mylist = line.split()
		for aword in mylist:
			word = ""
			for char in aword:
				if (char in punctuation) or (char in number):
					char = ""
				word = word + char
			wordList.append(word.lower())
		line = myFile.readline()
	return wordList

>>> createWordlist("wordlist1.txt")
['disqus', 'aarhus', 'aaron', 'ababa', 'aback-abaft-abandon', 'abandoned', 'abandoning', 'abandonment', 'abandons', 'abase', 'wer', 'abased', 'abasement', 'abasements', 'abases', 'abash', 'abashed']
>>> 
