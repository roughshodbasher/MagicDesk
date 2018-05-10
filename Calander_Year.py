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
		print(task.date)
		# Checking if month is valid
		if task.date[1] <= 0 or task.date[1] >= 13:
			assert ValueError("Month Incorrect")
		self.months[task.date[1]-self.months[0].number].insertTask(task)
	
	def getWeeksTasks(self,date):
		return self.months[date[1]-1].getWeeksTasks(date)
		
if "__name__" == "__main__":
	test = Year(2018)
	test.printAll()
