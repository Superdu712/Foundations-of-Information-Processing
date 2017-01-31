            ############################################
              ##  Author:        Danning Du         ##
              ##  Date:       3rd October 2016      ##
              ##       Activity 4.5 rebellion       ##
            ############################################

>>> monthDict={1:'January', 2:'Feburary', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10: 'October', 11: 'November', 12: 'December'} # create a dictionary for 12 months
>>> def timestamp(year): # define a function called timestamp with the parameter year as a string
	print("Generating start and stop timestamps for each month in year", year) # message that tells us what the function does
	for x in range(1,13): # for loops on x (which is the month number) from 1 to 13
		month = monthDict[x] # set the value of the key x in monthDict as month name
		print("For", month)
		start = str(x).zfill(2) # set the width of the str(x) to 2, so that the width after filling zeros is 2. assigns it to the start month.
		stop = str(x+1).zfill(2) # set the width of the str(x+1) to 2, so that the width after filling zeros is 2. assigns it to the stop month.
		YY = year[2:4] # since we only want the last two digits of the parameter year, index year at position [2:4] to get YY.
		startDate = YY + start + '01000000' # use addition operator to concatenate strings; The start date DD is always '01 and time hhmmss is always six zeros '000000'.
		while x != 12: # while x is not equal to 12 (except the last month)
			endDate = YY + stop + '01000000' 
			print("Start is:", startDate, "Stop is:", endDate)
			break # break the while loop so that it does not loop infinitely.
		else: # if it is the last month
			endDate = str(int(YY)+1) + '0101000000' # the stop month of the last month is always the January of the next year, so '01'. Since we want the next year YY,
                                                                # we first convert YY to number using int(YY), then increase int(YY) by 1, then convert it back to string.
			print("Start is:", startDate, "Stop is:", endDate)
>>> year = '2016'
>>> timestamp(year) # test the function
Generating start and stop timestamps for each month in year 2016
For January
Start is: 160101000000 Stop is: 160201000000
For Feburary
Start is: 160201000000 Stop is: 160301000000
For March
Start is: 160301000000 Stop is: 160401000000
For April
Start is: 160401000000 Stop is: 160501000000
For May
Start is: 160501000000 Stop is: 160601000000
For June
Start is: 160601000000 Stop is: 160701000000
For July
Start is: 160701000000 Stop is: 160801000000
For August
Start is: 160801000000 Stop is: 160901000000
For September
Start is: 160901000000 Stop is: 161001000000
For October
Start is: 161001000000 Stop is: 161101000000
For November
Start is: 161101000000 Stop is: 161201000000
For December
Start is: 161201000000 Stop is: 170101000000
>>> 

