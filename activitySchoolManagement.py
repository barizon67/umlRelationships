class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.get_age()}")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")

#Reflection: Accessing __age through get_age() method is a good practice to maintain encapsulation. The Student class inherits from Person and can access the display_info() method to show the student's information. The study() method is specific to the Student class, demonstrating polymorphism.
student1 = Student("Lina", 20)
student1.display_info()
student1.study()