#Main Calander class for Tasks

from Calander_Year import Year

#Temp task add
import Calander_Task

class Calander:
	def __init__(self):
		#Hard coded current year to 2017 b.c 1st of Jan is a Sunday
		#	TODO check for the current time (year)
		self.years = [Year(2017)]
	
	def addTask(self,task):
		#Task formatting
		""" self.name
			self.time
			self.date	"""
		#Date formatting
		""" [DD,MM,YYYY] """
		
		#Checks if in the past
		"""" currently only checking from creation date TODO get todays date """
		if task.date[-1] < self.years[0].number:
			raise ValueError("Year Incorrect")
		
		#Checking if year is in the current array
		
			#if not (task.date is within self.years)
			#Adds years until added
		while not (task.date[-1] - self.years[-1].number < 1):
			self.years.append(Year(self.years[-1].number+1))
		# Adding Task to correct date
			# Adding to year, then calling each sub date
		print(task.date[-1]-self.years[0].number,len(self.years))
		self.years[task.date[-1]-self.years[0].number].insertTask(task)
		
		return True
		
	def printWeeksTasks(today=False):
		# Prints off this Weeks Tasks
		# if today Saturday (new week on Sunday prints Sat - next Sat)
		# TODO get todays date, today input in form of [DD,MM,YYYY]
		
		#Saturday check
		
test = Calander()
testTask = Calander_Task.Task("Name",[1,1,2020],2130)
test.addTask(testTask)
for y in test.years:
	print(y.printAll())
print(len(test.years))
input()
