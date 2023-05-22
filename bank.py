#python
class Student:
    name="Miriam"
    age=27
    school="Akirachix"
    nationality="Kenyan"

    def __init__(self,name,age,nationality):
     self.name=name
     self.age=age
     self.nationality=nationality

    def greet_student(self):
     return f"Hello{Student.name}, welcome to {self.school}, proudly{self.nationality}"