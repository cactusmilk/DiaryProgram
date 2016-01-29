import sys, os, datetime, re


#checks the state of the year file
def checkFileYear(year):
	if not os.path.exists(str(year)):
		os.mkdir(str(year))
		return print("Created folder %s" % (year))
	elif os.path.exists(str(year)) :
		return None

#checks the state of the month file
def checkFileMonth(month):
	if not os.path.exists(str(month)):
		os.mkdir(str(month))
		return print("Created folder %s" % (month))
	elif os.path.exists(str(month)):
		return None

#adds the entry to the file
def addingEntry(fileMonth,dayNow,text):
	path = "%s/%s" % (fileMonth, dayNow)
	textFile = open(str(path), "a")
	textFile.write(str(text))
	textFile.close()



#Dates used for the input
dateCurrent = datetime.datetime.now()
yearNow = dateCurrent.year
monthNow = dateCurrent.strftime("%B")
dayNow = dateCurrent.day
fileMonth = "%s/%s" % (yearNow, monthNow)


#Running the program
diaryEntry = input("Write here: ")

checkFileYear(yearNow)
checkFileMonth(fileMonth)
addingEntry(fileMonth, dayNow, diaryEntry)	
	
