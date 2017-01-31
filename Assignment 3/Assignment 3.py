Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> ## Author: Danning Du
>>> ## Date: September 15th, 2016
>>> ## ASSIGNMENT 3
>>> ## PPiC 3.1 Create a string variable that is initialized to your entire name––first, middle, and last.
>>> myname = "Danning Du" # Assign a string consists of my first name "Danning" and my last name "Du" to a variable called myname. (I don't have a middle name)
>>> 
>>> ## PPiC 3.4 Using the slice and concatenation operators, print your name in the form “Lastname, Firstname.”
>>> # Using concatenation operators: addition operator (+)
>>> lname = "Du" # assign last name "Du" to a variable called lname
>>> fname = "Danning" # assign first name "Danning" to a variable called fname
>>> fullname = lname + ", " + fname + "." # use addition operator (+) to concatenate strings. Since the concatenation operator does not automatically add a space between strings, we have to add a space after ","
>>> fullname
'Du, Danning.'
>>> print(fullname)
Du, Danning.
>>> # Using slice operator [:]
>>> fullname = "Du, Danning." # assign my full name as a string to fullname
>>> len(fullname) # length of the string fullname
12
>>> fullname[0:12] # since we want the print the full name as the substring, 0 after the [ is the starting index of the first character in the substring, and 12after : is the last character.
'Du, Danning.'
>>> print(fullname[0:12])
Du, Danning.
>>> # Combine the addition operator and slice operator
>>> lname = "Du"
>>> fname = "Danning"
>>> len(lname)
2
>>> len(fname)
7
>>> fullname = lname[0:2] + ", " + fname[0:7] + "."
>>> print(fullname)
Du, Danning.
>>> 
>>> ## PPiC 3.6 Assume you have two variables: s='s', and p='p'. Using concatenation and repetition, write an expression that produces the string mississippi.
>>> s='s'
>>> p='p'
>>> 'mi' + s*2 + 'i' + s*2 + 'i' + p*2 + 'i' # repeat string s and p by using repetition operator * 
'mississippi'
>>> 
>>> ## PPiC 3.8 Using the count method, ﬁnd the number of occurrences of the character ‘s’ in the string 'mississippi'.
>>> 'mississippi'.count('s') # astring.count(item) returns the number of occurrences of 's' in 'mississippi'
4
>>> 
>>> ## PPiC 3.9 Replace all occurrences of the substring 'iss' with 'ox'.
>>> 'mississippi'.replace('iss','ox') # replaces all occurances of old substring 'iss' with new substring 'ox' in 'mississippi'
'moxoxippi'
>>> 
>>> ## PPiC 3.11 Make the word 'python' centered and all capital letters in a string of length 20.
>>> 'python'.center(20) # first, use center method to return the string 'python' surrounded by spaces to make 'python' 20 characters long.
'       python       '
>>> ('python'.center(20)).upper() # then use upper method to return it in all uppercase.
'       PYTHON       '
>>> 
>>> ## PPiC 3.15 Write the indexToLetter function using ord and chr.
>>> def indexToLetter(index): # defines function indexToLetter that takes parameter index
	if index in range(ord('a'), ord('z')+1): # As defined by the ASCII, ord('a') converts character 'a' to number 97, and ord('z') converts character 'z' to number 122. Checks if index is in the range(97, 123)
		letter = chr(index) # letter is converted from number to character by using chr(index)
	else:
		letter = "" # if index is not in the range(97, 123), there is no corresponding character to convert according to the ASCII.
	return letter # returns the converted letter

>>> indexToLetter(103) # checks if the function indexToLetter(index) works
'g'
>>> indexToLetter(123)
''
>>> indexToLetter(96)
''
>>> 
>>> ## PPiC 3.18 Write a python function stripSpaces(myString) that takes a string representing a phrase as a parameter and returns the paragraph with the order of the letters intact but the spaces between each word removed.
>>> def stripSpaces(myString): # defines function stripSpaces that takes parameter myString
	newString = myString.replace(" ","") # use the replace method to replace all occurrences of space " " with no space "" in myString, and assign it to a variable called newString.
	return newString # returns newString with the order of the letters in myString intact but no spaces between each word

>>> stripSpaces("be right back")
'berightback'
>>> 
>>> ## PPiC 3.21 Write the substitutionDecrypt method.
>>> def substitutionDecrypt(cipherText ,key): # defines function substitutionDecrypt that takes parameters cipherText and key
	alphabet = "abcdefghijklmnopqrstuvwxyz " # creates an alphabet string
	cipherText = cipherText.lower() # converts cipherText to all lowercases using lower method
	plainText = ""
	for ch in cipherText: # for loops on each character ch in cipherText
		idx = key.find(ch) # using find method to return the index of the first occurrence of chracter in string key, assign the index to variable idx
		plainText = plainText + alphabet[idx] # alphabet[idx] returns the character at position idx and assign it to plainText for all the characters in cipherText
	return plainText # return the decrypted cipherText as plainText

>>> testKey1 = "zyxwvutsrqponmlkjihgfedcba "
>>> testKey2 = "ouwckbjmpzyexavrltsfgdqihn "
>>> substitutionDecrypt("gsv jfrxp yildm ulc",testKey1) # decrypt string "gsv jfrxp yildm ulc" with testKey1
'the quick brown fox'
>>> substitutionDecrypt("fmk lgpwy utvqa bvi",testKey2) # decrypt string "fmk lgpwy utvqa bvi" with testKey2
'the quick brown fox'
>>> 
>>> ## PPiC 3.23 Write the removeChar function using for loops rather than slice operators.
>>> def removeChar(string,idx): # define function removeChar that takes parameter string and idx
	newStr = ""
	for i in range(0,len(string)): # for loops on i from 0 to the length of the string
		if i != idx: # checks if i is not equal to the parameter idx
			newStr = newStr + string[i] # for every i not equal to idx, newStr added up the character at position i in string.
	return newStr # returns the newStr after remove string[idx] from string

>>> removeChar("Hello world",5) # checks if the removeChar(string,idx) function works
'Helloworld'
>>> removeChar("Pineapple",7)
'Pineappe'
>>> 

