class Student:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.average = 0

    def avg(self, score, lectures):
        self.average = score/lectures
        return self.average

student_1 = Student(first_name="Dmytro", second_name="Vyshnevetsky", age=19)
student_2 = Student(first_name="Ivan", second_name="Sirko", age=20)
student_3 = Student(first_name="Pylyp", second_name="Orlyk", age=19)

print(f"Dmytro Vyshnevetsky - {student_1.avg(80, 20)}")
print(f"Ivan Sirko - {student_2.avg(100, 25)}")
print(f"Pylyp Orlyk - {student_3.avg(90, 30)}")