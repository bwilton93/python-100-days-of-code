class Person:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

  def formatted_output(self):
    print(f'{self.name} is {self.age} years old')
