# Name: Inthat # Student ID: 68010545999
class Student():
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.credits = 0
    def get_info(self):
        return f"ID: [{self.student_id}], Name: [{self.name}], Major: [{self.major}], Credits: [{self.credits}]"

id = int(input("Enter student ID: "))
n = (input("Enter name: "))
m = input("Enter major: ")
student = Student(id, n, m)
print(Student.get_info(student))