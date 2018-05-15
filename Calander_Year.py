# Calender for Magic_Desk - Year subClass
# Year files
# Current Version 0.0

from Calander_Month import Month

class Year:
	def __init__(self,number):
		self.number = number
		# Getting the first day of the year
		weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
		startDay = [(3+number-2000)%7]
		
		# Assuming wont be running until 2100
		leap = False
		if number%4 == 0:
			leap = True
		self.months = []
		for i in range(12):
			self.months.append(Month(i,leap,startDay))

	def printAll(self):
		print("Year: "+str(self.number))
		for m in self.months:
			print(m)
			print()

	def printTasks(self,date):
		# date inputted in from of [DD,MM,YYYY]
		self.month[date[1]-1]

		
	def insertTask(self,task):
		#print(task.date)
		# Checking if month is valid
		if task.date[1] <= 0 or task.date[1] >= 13:
			assert ValueError("Month Incorrect")
		self.getMonth(task.date[1]).insertTask(task)
	
	def getWeeksTasks(self,date):
		Tasks = self.getMonth(date[1]).getWeeksTasksMonth(date)
		if Tasks[-1] != False:
			print(Tasks[0].nameDay)
			return Tasks
		Tasks.pop()
		date[0] += 1
		return Tasks + self.getMonth(date[1]).getWeeksTasksMonth(date,len(Taks))
	
	def getMonth(self,number):
		return self.months[number-1]
	
if "__name__" == "__main__":
	test = Year(2018)
	test.printAll()
