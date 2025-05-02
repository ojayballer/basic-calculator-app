class Person():
    def __init__(self):
        pass
    def __str__(self):
        return" person object"
class student(Person):
    def __init__(self):
        super().__init__()
        
    def __str__(self):
        return"Student object"
omojire=student()
jire=Person()
print(omojire.__str__())
print(jire.__str__())