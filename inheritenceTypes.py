# types of inheritence

# Types of inheritance in Python

class FirstClass:
    def firstPrintFunction(self):
        print("This is First Class")

# Second Class is a Single Inheritance
class SecondClass(FirstClass):
    def secondPrintFunction(self):
        print("This is Second Class")

class ThirdClass:
    def thirdFunction(self):
        print("This is Third Function")

# Fourth Class is a multi-level inheritance
class FourthClass(SecondClass):
    def FourthFunction(self):
        print("This is Fourth Function")

# Multiple inheritance
class FifthClass(FirstClass,ThirdClass):
    def fifthFunction(self):
        print("This is Fifth Function")

class SixthClass(FirstClass):
    def sixthFunction(self):
        print("This is Sixth Function")


object2 = SecondClass()
object4 = FourthClass()
object5 = FifthClass()
object6 = SixthClass()

# print(isinstance(object2, FirstClass))
# print(isinstance(object4, FirstClass))
# print(isinstance(object5, FirstClass))
# print(isinstance(object6, FirstClass))

object2.secondPrintFunction()
