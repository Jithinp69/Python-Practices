class ClassInPython:
    name ="ABC"
    age = 12

    def fistFunc(self):
        print(self.name)

class SecondClass:
    def __init__(self, studentID, studentName):
        self.studentID = studentID
        self.studentName = studentName

    def secondFunc(self):
        print(self.studentID)
        print(self.studentName)


object1 = ClassInPython()
# print(object1.name)
# print(object1.age)
object1.fistFunc()

obj2 = SecondClass(101, "Roy")
obj2.secondFunc()