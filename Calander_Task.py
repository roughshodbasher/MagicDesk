# Calander for Magic_Desk - Task subClass
# Version 1.0

class Task:
    def __init__(self,name,date,time):
        assert time >= 0
        assert time <= 2359
        self.name = name
        self.date = date
        self.time = time
        self.showtime = str(time%1200)
        if self.showtime == "0":
            self.showtime = "12"
        while len(self.showtime) < 4:
            self.showtime = "0" + self.showtime
        self.showtime = self.showtime[:2]+":"+self.showtime[2:]
        if time >= 1200:
            self.showtime += " PM"
        else:
            self.showtime += " AM"

    def __str__(self):
        return self.showtime + ", "+ self.name

    def getTime(self):
        return self.time
    


if "__name__" == "__main__":
	A = Task("testing",123,1200)
	print(A)
	x = input()
