# Calander for Magic_Desk - Day subClass
# Version 0.0

from Calander_Task import Task

class Day:
	def __init__(self,number,dayOfWeek):
		assert number >= 1
		assert number <= 31
		self.number = number
		self.name = str(number)
		self.nameDay = dayOfWeek
		self.tasks = []
		if number%10 == 1 and number != 11:
			self.name += "st"
		elif number%10 == 2 and number != 12:
			self.name += "nd"
		elif number%10 == 3:
			self.name += "rd"
		else:
			self.name += "th"

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.nameDay+" "+self.name

	def printTasks(self):
		for task in self.tasks:
			print(task)

			
	def getTasks(self):
		return self.tasks
		
	def insertTask(self,task):
		self.tasks.append(task)
		return

if "__name__" == "__main__":	
	mon = Day(12)
	mon.insertTask(Task("test1",None,1022))
	mon.insertTask(Task("test3",None,1))
	#print(mon)
	mon.printTasks()
