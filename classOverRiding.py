# class ParentClass:
#     def __init__(self):
#         print("inside parent")

# class ChildClass(ParentClass):
#     pass
#     def __init__(self):
#         print("inside child class")


# # school = ParentClass()
# division = ChildClass()

# Override example

class ParentClass:
    def __init__(self):
        print("This is a Parent Class")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        print("This is a Child Class")


# school = ParentClass()
division = ChildClass()
