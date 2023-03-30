class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    def study(self):
        print(f"{self.name} is studying {self.major}.")
    
    def get_age(self):
        return self.age

    def set_major(self, major):
        self.major = major
