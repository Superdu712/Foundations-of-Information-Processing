Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> #2.5
>>> help("random.randrange")
Help on method randrange in random:

random.randrange = randrange(start, stop=None, step=1, _int=<class 'int'>) method of random.Random instance
    Choose a random item from range(start, stop[, step]).
    
    This fixes the problem with randint() which includes the
    endpoint; in Python this is usually not what you want.

>>> help("random.randint")
Help on method randint in random:

random.randint = randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

>>> #2.11
>>> def average(N):
	Acc=0
	for x in range(1,N+1):
		Acc = Acc + x
		averageAcc = Acc/N
	return averageAcc

>>> average(1)
1.0
>>> average(2)
1.5
>>> average(3)
2.0
>>> #2.23
>>> not 7 > 3
False
>>> #2.27
>>> import random
>>> count = random.randint(1,10)
>>> count <= 10 and count >= 1
True
>>> #2.29
>>> if result==100:
	answer=1
else:
	answer=2

	
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    if result==100:
NameError: name 'result' is not defined
>>> def random(result):
	if result==100:
		answer=1
	else:
		answer=2
	return answer

>>> random(80)
2
>>> random(100)
1
>>> #2.35
>>> def salary(rate, hours):
	if hours > 40:
		pay = rate*40 + 1.5*rate*(hours-40)
	else:
		pay = rate*hours
	return pay

>>> #Bonus EOC 2.8
>>> def function(n,i):
	x = 1
	for k in range(i):
		nextterm = (x+n/x)/2
		x = nextterm
	return nextterm

>>> function(4,4)
2.0000000929222947
>>> function(4,5)
2.000000000000002
>>> function(4,6)
2.0
>>> 
