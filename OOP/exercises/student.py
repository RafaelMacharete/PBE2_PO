class Student():
    def __init__(self, id, student_name, student_grade):
        self.id = id
        self.name = student_name
        self.grade = student_grade
    
    def calc_average(self):
        self.average = 0
        for idx in self.grade:
            self.average += idx
        self.average /= len(self.grade)

    def is_student_approved(self):
        if self.average >= 5:
            return 'IS'
        return 'IS NOT'
    
    def __str__(self):
        return f'{self.name} student has {self.average} of average\nAnd {self.is_student_approved()} approved'

student1 = Student(0, 'Rafael', [10,10,0])
student1.calc_average()
print(student1)