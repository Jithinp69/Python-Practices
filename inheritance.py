class SecondClassinPython:
    def __init__(self, studentID, studentName):
        self.studentID = studentID
        self.studentName = studentName
    
    def printStudentDetails(self):
        print(self.studentID)
        print(self.studentName)

class SecondChildClass(SecondClassinPython):
    pass

object2 = SecondClassinPython(2,"DEF")
object2.printStudentDetails()

objectSecondChildClass = SecondChildClass(3,"EFG")
objectSecondChildClass.printStudentDetails()

del object2.studentName
object2.printStudentDetails()

