# Calender for Magic_Desk - Month subClass
# Month files
# Current Version 0.1

# Version 0.2 ToDo
#   debug print

from Calander_Day import Day

class Month:
	def __init__(self,number,isLeap=False,dayCounter=[0]):
		# Assertions to make sure that the number is within 0 and 11, i.e is a month
		# January == 0 (i.e number 0 -> January, number 11 -> December
		assert number >= 0
		assert number <= 11
		
		weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
		
		self.number = number
		self.days = []

		# Broke up setting days into sections for "simplicity"
		#    Only adds day in once, in simple terms the following block adds 28 "days"
		#    which is the minimum number of days in a month, the checks for feb's unique property
		#    and adds if true, adds upto and including day 30, then checks if a days has thirty days from the daysThirty array
		#    if not thirty days adds last day (31)

		for i in range(28):
				self.days.append(Day(i+1,weekdays[dayCounter[0]]))
				dayCounter[0] = (dayCounter[0]+1)%7
		 
		daysThirty = [8,3,5,10]
		if number == 1:
			# February
			if isLeap:
				self.days.append(Day(29,weekdays[dayCounter[0]]))
				dayCounter[0] = (dayCounter[0]+1)%7
		else:
			for i in range(29,31):
				self.days.append(Day(i,weekdays[dayCounter[0]]))
				dayCounter[0] = (dayCounter[0]+1)%7
			if not (number in daysThirty):
				self.days.append(Day(31,weekdays[dayCounter[0]]))
				dayCounter[0] = (dayCounter[0]+1)%7
				
		# Setting Month name
		# Array of the month names, uses number to call name in O(1) time - its a constant array always O(1)...
		names = ["January","February","March","April","May","June","July","August","September","October","November","December"]
		self.name = names[number]

  
	def __repr__(self):
		return self.name

	def __str__(self):
		RS = self.name+":\t"
		if len(self.name) <= 6:
			RS += "\t"
		for day in self.days:
			RS += str(day)
			if day != self.days[-1]:
				RS += ","
		return RS
		
	def insertTask(self,task):
	#Adds task to correct day
	#checks if day valid
		if task.date[0] <= 0 or task.date[0] >= len(self.days):
			assert ValueError("Day Incorrect: "+task.date[0])
		self.days[task.date[0]-self.days[0].number].insertTask(task)
		return True

	def getWeeksTasksMonth(self,date,counterRemaining=0):

		#Generating an Array for the tasks
		#Formatting [ [Day="Sunday",Date="1st",Task="Do Nothing"], ... ]
		#Returns false as last element if doesn't add enough days to the array,
		#		i.e if the month ends this week
		print(self.name)
		counterMax = 7 - counterRemaining
		if date[0]+counterMax > len(self.days):
			return self.getDays(date[0],date[0]+counterMax) + [False]
		return self.getDays(date[0],date[0]+counterMax)
		
	def getDay(self,number):
		return self.days[number-1]
		
	def getDays(self,start,end):
		return self.days[start-1:end-1]
if "__name__" == "__main__":    
	A = Month(11)
	A
	print(A)

