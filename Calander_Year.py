# Calender for Magic_Desk - Year subClass
# Year files
# Current Version 0.0

from Calander_Month import Month

class Year:
	def __init__(self,number):
		self.number = number
		# Assuming wont be running until 2100
		leap = False
		if number%4 == 0:
			leap = True
		self.months = []
		for i in range(12):
			self.months.append(Month(i,leap))

	def printAll(self):
		print("Year: "+str(self.number))
		for m in self.months:
			print(m)

	def printTasks(self,date):
		# date inputted in from of [DD,MM,YYYY]
		self.month[date[1]-1]

		
	def insertTask(self,task):
		# Checking if month is valid
		if task.date[1] <= 0 or task.date[1] >= 13:
			assert ValueError("Month Incorrect")
		self.months[task.date[1]-self.months[0].number].insertTask(task)
		
		
if "__name__" == "__main__":
	test = Year(2018)
	test.printAll()
