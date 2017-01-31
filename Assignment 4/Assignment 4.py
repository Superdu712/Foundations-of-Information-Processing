Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> ## Author: Danning Du
>>> ## Date: September 23th, 2016
>>> ## ASSIGNMENT 4

>>> ## PPiC 4.1 Create a list with the following five items: 7, 9, 'a', 'cat', False. Assign this list to the variable myList.
>>> myList = [7,9,'a','cat',False] # use square brackets to include those comma-delimited values in the list.
>>> myList                         # return myList
[7, 9, 'a', 'cat', False]

>>> ## PPiC 4.2  Write Python statements to do the following:
>>> ## (a) Append 3.14 and 7 to the list.
>>> myList.append(3.14) # use append method to add 3.14 to the end of myList.
>>> myList.append(7)    # then add 7 to the end of myList
>>> myList              # return myList, it now has 3.14 and 7.
[7, 9, 'a', 'cat', False, 3.14, 7]

>>> ## (b) Insert the value 'dog' at position 3.
>>> myList.insert(3,'dog') # use insert method to insert 'dog' at the 3rd position in myList
>>> myList                 # return myList
[7, 9, 'a', 'dog', 'cat', False, 3.14, 7]

>>> ## (c) Find the index of 'cat'
>>> myList.index('cat') # use index method to return the index of the first occurrence of 'cat', which is at 4th position.
4

>>> ## (d) Count the number of 7’s in the list.
>>> myList.count(7) # use count method to return the number of occurence of 7, which is 2.
2

>>> ## (e) Remove the first 7 from the list.
>>> myList.remove(7) # use remove method to remove the first occurence of 7
>>> myList           # 7 at postion 0 is removed.
[9, 'a', 'dog', 'cat', False, 3.14, 7]

>>> ## (f) Remove 'dog' from the list using pop and index.
>>> myList.index('dog') # first, use index method to find the position of 'dog' in myList, which is 2.
2
>>> myList.pop(myList.index('dog')) # then, use pop method to remove and return the 2nd item in myList.
'dog'
>>> myList # return myList with 'dog' removed from myList
[9, 'a', 'cat', False, 3.14, 7]

>>> ## PPiC 4.3  Split the string “the quick brown fox” into a list of words.
>>> phrase = "the quick brown fox" # assign the string to a variable called phrase
>>> phrase.split() # use split method which takes the string as a parameter that indicates the places to break the string into substring.
['the', 'quick', 'brown', 'fox'] # In this case we want to break the string into a lost of words, so we assign no parameter to split, so Python will break the string using the space between words as the delimiter.

>>> ## PPiC 4.10 Suppose you initialize the following list: mylist = [[]]*3. Evaluate this expression.
>>> A = [] # assign an empty list to variable A
>>> mylist = [A]*3 # initialize the list, which is same as mylist = [[]]*3, the empty list is repeated 3 times, and assign the result to mylist
>>> mylist # the result is also a list consist of three empty lists.
[[], [], []]

>>> ## PPiC 4.11 Evaluate the expression mylist[1].append(2). Explain the result.
>>> mylist[1] # as we just did in the previous exercise, mylist = [[], [], []]
[] # index the position 1 in mylist, which returns an empty list
>>> mylist[1].append(2) # use append method to add 2 to the end of mylist[1], which returns [2]
>>> mylist # since a change to one element in mylist shows up in all three occurences, the repetition result is actually a list of three references to the same list.
[[2], [2], [2]]

>>> ## PPiC 4.12 Draw a reference diagram to illustrate what is happening in the previous two exercises.

>>> ## PPiC 4.18 Replace the call to the sum function with an iteration that computes the total of the values in alist.
>>> def sum(alist): # define function sum with the parameter alist
	sum = alist[0] # set the initial value of sum as the value in the 0 position of alist
	for i in alist[1:]: # for each i in alist start from position 1 to the end
		sum = sum + i # increase sum by i
	return sum # return sum that computes the total of the values in alist.

>>> sum([1,2,3,4,5,6]) # To test how the function works
21

>>> ## PPiC 4.24 You have been given the following lists of students and their test scores:
>>> ## names=['joe','tom','barb','sue','sally'] scores=[10,23,13,18,12] Write a function, makeDictionary, that takes the two lists and returns a dictionary with the names as the key and the scores as the values.
## Assign the result of makeDictionary to scoreDict, which will be used in the exercises that follow.
>>> def makeDictionary(names,scores): # define function makeDictionary with two parameters: names, scores, both are lists
	scoreDict={} # assign an empty dictionary as the initial value to scoreDict
	v = 0 # set the initial of value v to 0
	for k in names: # for each key k in list names
		scoreDict[k] = scores[v] # the value of the key in scoreDict equals the value in list scores
		v = v + 1 # increase the value of v by 1 to the next v
	return scoreDict # return the dictionary scoreDict

>>> names=['joe','tom','barb','sue','sally'] # to test the function, use the two lists provided in the question
>>> scores=[10,23,13,18,12]
>>> makeDictionary(names,scores) # we get dictionary scoreDict with the values in names and its scores
{'sally': 12, 'barb': 13, 'joe': 10, 'sue': 18, 'tom': 23}

>>> ## PPiC 4.31 Print out a table of students and their scores with the students listed in alphabetical order.
>>> def order(dictionary): # define function order with parameter dictionary
	names = list(dictionary.keys()) # first, make a list of names from the keys of dictionary
	names.sort() # modifies names to be sorted, list names is sorted in alphabetical order
	for k in names: # for each key k in names
		if k in dictionary: # check if k is in dictionary
			print(k,dictionary[k]) # if it is, print the student name and the corresponding value in dictioanry

			
>>> order({'sally': 12, 'barb': 13, 'joe': 10, 'sue': 18, 'tom': 23}) # test the function with the dictionary created in 4.24
barb 13 # as we can see, students names are listed in alphabetical order.
joe 10
sally 12
sue 18
tom 23

>>> ## Bonus PPiC 4.7 Write a function shuffle that takes a list and returns a new list with the elements shuffled into a random order.
>>> import random # first, import random module into Python
>>> def shuffle(list): # define function shuffle with parameter list
	a = len(list) - 1 # decrease the length of list by 1 to get the index of the last element in the list
	Newlist = [] # assign an empty list as the initial value to Newlist
	for i in range(len(list)): # for each number i in range 0 to the length of list
		idx = random.randint(0,a-i) # generate a random integer in the range 0 to a-i, assign it to the idx
		Newlist.insert(idx,list[idx]) # list[idx] gives the element in the idx position in list; use insert method to insert list[idx] at the idx position in the Newlist.
		list.remove(list[idx]) # remove the first occurrence of list[idx] in the list, so the list does not include the list[idx] that we have just put into the Newlist
	return Newlist # return Newlist with the elements shuffled in list

>>> shuffle([1,'dog',4,6]) # to test the function, take list [1,'dog',4,6] as the parameter 
[6, 'dog', 1, 4]
>>> shuffle([1,'dog',4,6])
[4, 'dog', 1, 6]
>>> shuffle([1,'dog',4,6])
[4, 'dog', 1, 6]
>>> shuffle([1,'dog',4,6])
[1, 4, 6, 'dog']
>>> shuffle([1,'dog',4,6])
[6, 4, 'dog', 1]
>>> shuffle([1,'dog',4,6])
[6, 4, 'dog', 1]
>>> shuffle([1,'dog',4,6])
[4, 1, 6, 'dog']
>>> shuffle([1,'dog',4,6])
[1, 'dog', 4, 6]
>>> 
