#Main Calander class for Tasks

from Calander_Year import Year

#Temp task add
import Calander_Task

class Calander:
	def __init__(self):
		#Hard coded first year to 2017 b.c 1st of Jan is a Sunday
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
		#print(task.date[-1]-self.years[0].number,len(self.years))
		self.years[task.date[-1]-self.years[0].number].insertTask(task)
		
		return True
		
	def printWeeksTasks(self,today=False):
		# Prints off this Weeks Tasks
		# if today Saturday (new week on Sunday prints Sat - next Sat)
		# TODO get todays date, today input in form of [DD,MM,YYYY]
		if not today:
			#add call to get current date
			#then format in [DD,MM,YYYY]
			x = 1
		
		#Realized can be done when printing not calling
		#Saturday check
		#if self.years[today[2]-2017].months[today[1]-1].days[today[0]-1].nameDay == "Saturday":
			#Want to Display today and Next week (Sun - Sat)
		
		#Sunday\tMonday\tTuesday\tWednesday\tThursday\tFriday\tSaturday
		#Date Tasks
		print("\tSunday\t\tMonday\t\tTuesday\t\tWednesday\tThursday\tFriday\t\tSaturday\n")
		days = self.years[today[2]-2017].getWeeksTasks(today)
		count = 0
		isSaturday = False
		dayArray = []
		if days[0].nameDay == "Saturday":
			count = 1
			isSaturday = True
		for i in range(0,len(days)):
			dayArray.append(days[i])
		#if today is saturday prints in corresponding position
		print(dayArray)
		if isSaturday:
			print("\t"*13+str(dayArray[0].name))
			for t in dayArray[0].tasks:
				print("\t"*13+str(t))
			del days[0]
			del dayArray[0]
		# Getting dates for the week
		print(dayArray[0].nameDay,dayArray[0].name)
		dateArray = []
		taskArray = []
		for d in days:
			dateArray.append(d.name)
			taskArray.append(d.tasks)
		temp = "\t\t".join(dateArray)
		print("\n\t"+temp+"\n")
		maxTasks = 1
		counter = 0
		printArray = []
		while counter < maxTasks:
			printArray.append([])
			for i in range(6):
				if len(dayArray[i].tasks) < counter+1:
					printArray[-1].append("\t")
				else:
					printArray[-1].append(dayArray[i].tasks[counter])
				if len(dayArray[i].tasks) > maxTasks:
					maxTasks = len(dayArray[i])
			counter += 1
		
		for p in printArray:
			PS = "\t"
			for t in p:
				PS += str(t)
				if 16-len(str(t)) > 0:
					PS += " "*(16-len(str(t)))
				
			print(PS)
		for d in days:
			print(d.tasks)
		return
		
test = Calander()
testTask = Calander_Task.Task("Name",[7,0,2017],2130)
test.addTask(testTask)
test.addTask(testTask)

#test for adding tasks
for i in range(4):
	testTask = Calander_Task.Task("Name"+str(i),[(1+i)+7,0,2017],2130)
	test.addTask(testTask)


#for y in test.years:
#	print(y.printAll())
#print(len(test.years))
test.printWeeksTasks([7,1,2017])
input()
