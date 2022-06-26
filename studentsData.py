class StudentsDetails:
    def __init__(self, studentID, studentName,studentClass, scienceMark, mathMark):
        self.studentID = studentID
        self.studentName = studentName
        self.studentClass = studentClass
        self.scienceMark = scienceMark
        self.mathMark = mathMark

    def average(self):
       avg = ((self.mathMark + self.scienceMark)/2)
       return avg
        

id = int(input("Enter Students id"))
name = input("enter student name")
studentCls = int(input("enter student class"))
sciencemark = int(input("enter science mark"))
mathmark = int(input("enter math mark"))

studentOne = StudentsDetails(id, name, studentCls, sciencemark, mathmark)

print(studentOne.studentID)
print(studentOne.studentName)
print(studentOne.scienceMark)
print(studentOne.average())