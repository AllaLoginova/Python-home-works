class Programmer:
    grade_pay = {'Junior': 10, 'Middle': 15, 'Senior': 20}

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.work_hours = 0
        self.salary = 0
        self.counter = 0

    def work(self, time):
        self.work_hours += time
        self.salary += time * self.grade_pay[self.grade]
        
        if self.grade == 'Senior':
            self.salary += time * self.counter
 
    def rise(self):
        if self.grade == 'Senior':
           self.counter += 1

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
programmer.rise()
programmer.work(100)
print(programmer.info())

# Васильев Иван 750ч. 7500тгр.
# Васильев Иван 1250ч. 15000тгр.
# Васильев Иван 1500ч. 20000тгр.
# Васильев Иван 1750ч. 25250тгр.
# Васильев Иван 1850ч. 27450тгр.
