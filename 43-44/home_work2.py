class Programmer:
    grade_pay = {'Junior': 10, 'Middle': 15, 'Senior': 20}

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.work_hours = 0
        self.salary = 0
        self.flag = False

    def work(self, time):
        self.work_hours += time
        self.salary += time * self.grade_pay[self.grade]
        
        if self.grade == 'Senior' and self.flag:
            self.salary += time

    def rise(self):
        if self.grade == 'Senior':
           self.flag = True 

        elif self.grade == 'Junior':
            self.grade = 'Middle'

        elif self.grade == 'Middle':
            self.grade = 'Senior'

    def info(self):
        return f"{self.name} {self.work_hours}ч. {self.salary}тгр."
    

programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())