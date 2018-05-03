# Calender for Magic_Desk - Month subClass
# Month files
# Current Version 0.1

# Version 0.2 ToDo
#   debug print

from Calander_Day import Day

class Month:
	def __init__(self,number,isLeap=False):
		# Assertions to make sure that the number is within 0 and 11, i.e is a month
		# January == 0 (i.e number 0 -> January, number 11 -> December
		assert number >= 0
		assert number <= 11

		
		self.number = number
		self.days = []

		# Broke up setting days into sections for "simplicity"
		#   Only adds day in once, in simple terms the following block adds 28 "days"
		#    which is the minimum number of days in a month, the checks for feb's unique property
		#    and adds if true, adds upto and including day 30, then checks if a days has thirty days from the daysThirty array
		#    if not thirty days adds last day (31)

		for i in range(28):
				self.days.append(Day(i+1))
		 
		daysThirty = [8,3,5,10]
		if number == 1:
			# February
			if isLeap:
				self.days.append(Day(29))
		else:
			for i in range(29,31):
				self.days.append(Day(i))
			if not (number in daysThirty):
				self.days.append(Day(31))
				
		# Setting Month name
		# Array of the month names, uses number to call name in O(1) time - its a constant array always O(1)...
		names = ["January","February","March","April","May","June","July","August","September","October","November","December"]
		self.name = names[number]

		return
  
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
	
	#checks if day correct
		if task.date[0] <= 0 or task.date[0] >= len(self.days):
			assert ValueError("Day Incorrect")
		
		self.days[task.date[1]-self.days[0].number].insertTask(task)
		return True

if "__name__" == "__main__":    
	A = Month(11)
	A
	print(A)

