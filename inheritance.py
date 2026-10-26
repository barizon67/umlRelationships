class Animal:
  def __init__(self, name):
    self.name = name

  def speak(self):
    pass

class Dog(Animal):
  def speak(self):
    return f"{self.name} barks."

if __name__ == "__main__":
  dog = Dog("Vinir")
  print(dog.speak())